from enum import Enum


class PrivacyLevelEnum(str, Enum):
    ME = "me"
    FOLLOWERS = "followers"
    INSTANCE = "instance"
    EVERYONE = "everyone"

    def __str__(self) -> str:
        return str(self.value)
