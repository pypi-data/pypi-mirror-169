from typing import List

from anyscale.client.openapi_client.models import LogFileChunk
from anyscale.client.openapi_client.models.node_type import NodeType


class LogGroupFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.chunks: List[LogFileChunk] = []

    def insert_chunk(self, chunk: LogFileChunk):
        self.chunks.append(chunk)

    def get_chunks(self) -> List[LogFileChunk]:
        return sorted(self.chunks, key=lambda chunk: chunk.chunk_name)

    def get_name(self) -> str:
        return self.file_name

    def get_target_path(self) -> str:
        assert len(self.chunks) >= 1
        sample_chunk = self.chunks[0]
        chunk_path = sample_chunk.chunk_name.lstrip("/")
        # Input is "../../monitor.log/part-one.log"
        # Remove the "/part-one.log"
        return "/".join(chunk_path.split("/")[:-1])

    def get_size(self) -> int:
        return sum([chunk.size for chunk in self.chunks])


class LogGroupNode:
    def __init__(self, node_id: str, node_type: NodeType):
        self.node_id = node_id
        self.node_type = node_type
        self.files: List[LogGroupFile] = []

    def insert_chunk(self, chunk: LogFileChunk):
        for file in self.files:
            if file.file_name == chunk.file_name:
                file.insert_chunk(chunk)
                return
        file = LogGroupFile(file_name=chunk.file_name)
        file.insert_chunk(chunk)
        self.files.append(file)

    def get_files(self) -> List[LogGroupFile]:
        return sorted(self.files, key=lambda file: file.file_name)

    def get_chunks(self) -> List[LogFileChunk]:
        result = []
        for file in self.files:
            result.extend(file.get_chunks())
        return result


class LogGroupSession:
    def __init__(self, session_id: str) -> None:
        self.session_id = session_id
        self.nodes: List[LogGroupNode] = []

    def insert_chunk(self, chunk: LogFileChunk):
        for node in self.nodes:
            if node.node_id == chunk.node_id:
                node.insert_chunk(chunk)
                return
        node = LogGroupNode(node_id=chunk.node_id, node_type=chunk.node_type)
        node.insert_chunk(chunk)
        self.nodes.append(node)

    def get_nodes(self) -> List[LogGroupNode]:
        return sorted(self.nodes, key=lambda node: (node.node_type, node.node_id))

    def get_files(self) -> List[LogGroupFile]:
        result = []
        for node in self.nodes:
            result.extend(node.get_files())
        return result

    def get_chunks(self) -> List[LogFileChunk]:
        result = []
        for node in self.nodes:
            result.extend(node.get_chunks())
        return result


class LogGroup:
    def __init__(self):
        self.sessions: List[LogGroupSession] = []

    def insert_chunk(self, chunk: LogFileChunk):
        for session in self.sessions:
            if session.session_id == chunk.session_id:
                session.insert_chunk(chunk)
                return
        session = LogGroupSession(session_id=chunk.session_id)
        session.insert_chunk(chunk)
        self.sessions.append(session)

    def get_sessions(self) -> List[LogGroupSession]:
        return sorted(self.sessions, key=lambda session: session.session_id)

    def get_files(self) -> List[LogGroupFile]:
        result = []
        for session in self.sessions:
            result.extend(session.get_files())
        return result

    def get_chunks(self) -> List[LogFileChunk]:
        result = []
        for session in self.sessions:
            result.extend(session.get_chunks())
        return result
