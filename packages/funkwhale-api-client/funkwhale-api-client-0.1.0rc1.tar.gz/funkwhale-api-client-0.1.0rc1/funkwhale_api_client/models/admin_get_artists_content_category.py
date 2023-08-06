from enum import Enum


class AdminGetArtistsContentCategory(str, Enum):
    MUSIC = "music"
    OTHER = "other"
    PODCAST = "podcast"

    def __str__(self) -> str:
        return str(self.value)
