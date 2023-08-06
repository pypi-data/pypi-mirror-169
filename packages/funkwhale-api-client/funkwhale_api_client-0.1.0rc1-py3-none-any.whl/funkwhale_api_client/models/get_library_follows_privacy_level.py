from enum import Enum


class GetLibraryFollowsPrivacyLevel(str, Enum):
    EVERYONE = "everyone"
    INSTANCE = "instance"
    ME = "me"

    def __str__(self) -> str:
        return str(self.value)
