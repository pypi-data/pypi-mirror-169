from enum import Enum


class ManageUserRequestTypeEnum(str, Enum):
    SIGNUP = "signup"

    def __str__(self) -> str:
        return str(self.value)
