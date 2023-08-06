from enum import Enum


class ModerationGetReportsType(str, Enum):
    ILLEGAL_CONTENT = "illegal_content"
    INVALID_METADATA = "invalid_metadata"
    OFFENSIVE_CONTENT = "offensive_content"
    OTHER = "other"
    TAKEDOWN_REQUEST = "takedown_request"

    def __str__(self) -> str:
        return str(self.value)
