from enum import Enum


class ModerationGetRequestsType(str, Enum):
    SIGNUP = "signup"

    def __str__(self) -> str:
        return str(self.value)
