from enum import Enum


class LibraryPrivacyLevelEnum(str, Enum):
    ME = "me"
    INSTANCE = "instance"
    EVERYONE = "everyone"

    def __str__(self) -> str:
        return str(self.value)
