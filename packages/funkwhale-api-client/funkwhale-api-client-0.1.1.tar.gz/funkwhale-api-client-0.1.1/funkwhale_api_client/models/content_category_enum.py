from enum import Enum


class ContentCategoryEnum(str, Enum):
    MUSIC = "music"
    PODCAST = "podcast"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
