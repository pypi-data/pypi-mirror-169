from enum import Enum


class ModerationTargetTypeEnum(str, Enum):
    ARTIST = "artist"

    def __str__(self) -> str:
        return str(self.value)
