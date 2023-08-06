from enum import Enum


class GetAlbumMutationsOrderingItem(str, Enum):
    VALUE_0 = "-artist__modification_date"
    VALUE_1 = "-creation_date"
    VALUE_2 = "-random"
    VALUE_3 = "-related"
    VALUE_4 = "-release_date"
    VALUE_5 = "-title"
    ARTIST_MODIFICATION_DATE = "artist__modification_date"
    CREATION_DATE = "creation_date"
    RANDOM = "random"
    RELATED = "related"
    RELEASE_DATE = "release_date"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
