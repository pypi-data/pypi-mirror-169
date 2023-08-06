import asyncio
from datetime import timedelta
import os
import tempfile
from typing import List, Optional

import aiohttp
from tqdm import tqdm

from anyscale.cli_logger import BlockLogger
from anyscale.client.openapi_client.models import (
    LogDownloadConfig,
    LogDownloadRequest,
    LogDownloadResult,
    LogFileChunk,
    LogFilter,
)
from anyscale.controllers.base_controller import BaseController
from anyscale.utils.logs_utils import LogGroup


class LogsController(BaseController):
    def __init__(
        self, log: BlockLogger = BlockLogger(), initialize_auth_api_client: bool = True
    ):
        super().__init__(initialize_auth_api_client=initialize_auth_api_client)
        self.log = log

    def render_logs(
        self, log_group: LogGroup, parallelism: int, read_timeout: timedelta,
    ):
        self._download_or_stdout(
            log_group=log_group,
            parallelism=parallelism,
            read_timeout=read_timeout,
            write_to_stdout=True,
        )

    def get_logs_for_tail(
        self,
        filter: LogFilter,
        page_size: Optional[int],
        ttl_seconds: Optional[int],
        timeout: timedelta,
    ):
        chunks = self._list_log_chunks(
            log_filter=filter,
            page_size=page_size,
            ttl_seconds=ttl_seconds,
            timeout=timeout,
        )
        groups = self._group_log_chunk_list(chunks=chunks)
        return groups

    def download_logs(
        self,
        # Provide filters
        filter: LogFilter,
        # List files config
        page_size: Optional[int],
        ttl_seconds: Optional[int],
        timeout: timedelta,
        read_timeout: timedelta,
        # Download config
        parallelism: int,
        download_dir: Optional[str] = None,
    ):
        log_chunks: List[LogFileChunk] = self._list_log_chunks(
            log_filter=filter,
            page_size=page_size,
            ttl_seconds=ttl_seconds,
            timeout=timeout,
        )
        log_group: LogGroup = self._group_log_chunk_list(log_chunks)
        self._download_or_stdout(
            download_dir=download_dir,
            read_timeout=read_timeout,
            parallelism=parallelism,
            log_group=log_group,
        )

    def _download_or_stdout(
        self,
        log_group: LogGroup,
        parallelism: int,
        read_timeout: timedelta,
        download_dir: Optional[str] = None,
        write_to_stdout: bool = False,
    ):
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Download all files to a temporary directory.
            asyncio.run(
                # TODO (shomilj): Add efficient tailing method here.
                self._download_files(
                    base_folder=tmp_dir,
                    log_chunks=log_group.get_chunks(),
                    parallelism=parallelism,
                    read_timeout=read_timeout,
                )
            )

            for log_file in tqdm(
                log_group.get_files(),
                desc="Downloading files.",
                disable=write_to_stdout,
            ):
                chunks = log_file.get_chunks()
                if write_to_stdout:
                    # Write to standard out
                    for chunk in chunks:
                        with open(
                            os.path.join(tmp_dir, chunk.chunk_name), "r"
                        ) as source:
                            print(source.read())
                else:
                    # Write to destination files
                    real_path = os.path.join(
                        download_dir or "", log_file.get_target_path()
                    )
                    real_dir = os.path.dirname(real_path)
                    if not os.path.exists(real_dir):
                        os.makedirs(real_dir)

                    chunks_written = 0
                    with open(real_path, "w") as dest:
                        for chunk in tqdm(chunks, desc=log_file.get_name()):
                            downloaded_chunk_path = os.path.join(
                                tmp_dir, chunk.chunk_name
                            )
                            if not os.path.exists(downloaded_chunk_path):
                                print("Download failed for file: ", chunk.chunk_name)
                                continue
                            with open(downloaded_chunk_path, "r") as source:
                                for line in source:
                                    dest.write(line)
                            chunks_written += 1

                    if chunks_written == 0:
                        os.remove(real_path)

    def _group_log_chunk_list(self, chunks: List[LogFileChunk]) -> LogGroup:
        # This has to happen locally because it happens after we retrieve all file metadata through the paginated
        # backend API for listing S3/GCS buckets.
        group = LogGroup()
        for chunk in chunks:
            group.insert_chunk(chunk=chunk)
        return group

    def _list_log_chunks(
        self,
        log_filter: LogFilter,
        page_size: Optional[int],
        ttl_seconds: Optional[int],
        timeout: timedelta,
    ) -> List[LogFileChunk]:
        next_page_token: Optional[str] = None
        all_log_chunks: List[LogFileChunk] = []

        while True:
            request = LogDownloadRequest(
                filter=log_filter,
                config=LogDownloadConfig(
                    next_page_token=next_page_token,
                    page_size=page_size,
                    ttl_seconds=ttl_seconds,
                ),
            )
            result: LogDownloadResult = self.api_client.get_log_files_api_v2_logs_get_log_files_post(
                log_download_request=request, _request_timeout=timeout
            ).result
            all_log_chunks.extend(result.log_chunks)
            if result.next_page_token is None:
                break
            next_page_token = result.next_page_token

        return all_log_chunks

    async def _download_file(
        self,
        sem: asyncio.Semaphore,
        pos: int,
        file_name: str,
        url: str,
        size: int,
        session: aiohttp.ClientSession,
        read_timeout: timedelta,
    ) -> None:
        async with sem:
            download_dir = os.path.dirname(file_name)
            if download_dir and not os.path.exists(download_dir):
                os.makedirs(download_dir)

            timeout = aiohttp.ClientTimeout(
                total=None, sock_connect=30, sock_read=read_timeout.seconds
            )
            async with session.get(url, timeout=timeout) as response:
                if response.status == 200:
                    with open(file_name, "wb") as fhand:
                        async for chunk in response.content.iter_chunked(1024):
                            fhand.write(chunk)
                else:
                    self.log.error(
                        f"Unable to download file {file_name}! response: [{response.status}, {await response.text()}]"
                    )

    async def _download_files(
        self,
        base_folder: Optional[str],
        log_chunks: List[LogFileChunk],
        parallelism: int,
        read_timeout: timedelta,
    ) -> List[str]:
        sem = asyncio.Semaphore(parallelism)
        downloads = []
        connector = aiohttp.TCPConnector(limit_per_host=parallelism)
        paths = []
        async with aiohttp.ClientSession(connector=connector) as session:
            for pos, log_chunk in enumerate(log_chunks):
                path = os.path.join(base_folder or "", log_chunk.chunk_name.lstrip("/"))
                paths.append(path)
                downloads.append(
                    asyncio.create_task(
                        self._download_file(
                            sem,
                            pos,
                            path,
                            log_chunk.chunk_url,
                            log_chunk.size,
                            session,
                            read_timeout,
                        )
                    )
                )

            await asyncio.gather(*downloads)
        return paths
