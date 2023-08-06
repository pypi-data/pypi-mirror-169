from enum import Enum


class GetTrackLibrariesOrderingItem(str, Enum):
    VALUE_0 = "-album__release_date"
    VALUE_1 = "-album__title"
    VALUE_2 = "-artist__modification_date"
    VALUE_3 = "-artist__name"
    VALUE_4 = "-creation_date"
    VALUE_5 = "-disc_number"
    VALUE_6 = "-position"
    VALUE_7 = "-random"
    VALUE_8 = "-related"
    VALUE_9 = "-size"
    VALUE_10 = "-title"
    ALBUM_RELEASE_DATE = "album__release_date"
    ALBUM_TITLE = "album__title"
    ARTIST_MODIFICATION_DATE = "artist__modification_date"
    ARTIST_NAME = "artist__name"
    CREATION_DATE = "creation_date"
    DISC_NUMBER = "disc_number"
    POSITION = "position"
    RANDOM = "random"
    RELATED = "related"
    SIZE = "size"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
