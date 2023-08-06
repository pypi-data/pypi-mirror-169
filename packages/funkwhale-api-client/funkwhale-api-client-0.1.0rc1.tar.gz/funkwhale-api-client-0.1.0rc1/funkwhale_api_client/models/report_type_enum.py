from enum import Enum


class ReportTypeEnum(str, Enum):
    TAKEDOWN_REQUEST = "takedown_request"
    INVALID_METADATA = "invalid_metadata"
    ILLEGAL_CONTENT = "illegal_content"
    OFFENSIVE_CONTENT = "offensive_content"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
