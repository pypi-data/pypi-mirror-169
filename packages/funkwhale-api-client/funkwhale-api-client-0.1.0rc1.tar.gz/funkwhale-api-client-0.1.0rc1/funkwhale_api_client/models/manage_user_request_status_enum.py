from enum import Enum


class ManageUserRequestStatusEnum(str, Enum):
    PENDING = "pending"
    REFUSED = "refused"
    APPROVED = "approved"

    def __str__(self) -> str:
        return str(self.value)
