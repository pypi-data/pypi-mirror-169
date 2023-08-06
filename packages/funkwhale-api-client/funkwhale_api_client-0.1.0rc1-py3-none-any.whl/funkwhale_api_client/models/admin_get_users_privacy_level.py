from enum import Enum


class AdminGetUsersPrivacyLevel(str, Enum):
    EVERYONE = "everyone"
    FOLLOWERS = "followers"
    INSTANCE = "instance"
    ME = "me"

    def __str__(self) -> str:
        return str(self.value)
