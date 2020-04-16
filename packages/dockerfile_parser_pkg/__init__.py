"""A basic parser for Dockerfile 'AST' (kind-of)."""


class Node:
    variant: str = "unknown"
    content: str
    has_continuation: bool

    def __init__(self, content: str):
        """Create the class."""
        self.content = content
        self.has_continuation = "\\" in content
    
    @staticmethod
    def validate(line) -> bool:
        """Checks if the passed line is a usage of this Node."""
        return False


class RunInstructionNode(Node):
    """A `RUN` instruction."""

    variant: str = "RUN"

    @staticmethod
    def validate(line) -> bool:
        return line.startswith("RUN ")


class CopyInstructionNode(Node):
    """A `COPY` instruction."""

    variant: str = "COPY"

    @staticmethod
    def validate(line) -> bool:
        return line.startswith("COPY ")


class EnvironmentInstructionNode(Node):
    """A `ENV` instruction."""

    variant: str = "ENV"

    @staticmethod
    def validate(line) -> bool:
        return line.startswith("ENV ")


class EntrypointInstructionNode(Node):
    """A `ENTRYPOINT` instruction."""

    variant: str = "ENTRYPOINT"

    @staticmethod
    def validate(line) -> bool:
        return line.startswith("ENTRYPOINT ")


class CommandInstructionNode(Node):
    """A `CMD` instruction."""

    variant: str = "CMD"

    @staticmethod
    def validate(line) -> bool:
        return line.startswith("CMD ")


class WorkingDirectoryInstructionNode(Node):
    """A `WORKDIR` instruction."""

    variant: str = "WORKDIR"

    @staticmethod
    def validate(line) -> bool:
        return line.startswith("WORKDIR ")


class LabelInstructionNode(Node):
    """A `LABEL` instruction."""

    variant: str = "LABEL"

    @staticmethod
    def validate(line) -> bool:
        return line.startswith("LABEL ")


ALL_NODES = [
    RunInstructionNode,
    CopyInstructionNode,
    EnvironmentInstructionNode,
    CopyInstructionNode,
    EntrypointInstructionNode,
    CommandInstructionNode,
    WorkingDirectoryInstructionNode,
    LabelInstructionNode,
]


def to_node(line: str) -> Node:
    """Returns the line as a Node."""

    for node in ALL_NODES:
        if node.validate(line):
            return node(line)

    return Node(line)
