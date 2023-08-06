from enum import Enum


class ModerationGetRequestsStatus(str, Enum):
    APPROVED = "approved"
    PENDING = "pending"
    REFUSED = "refused"

    def __str__(self) -> str:
        return str(self.value)
