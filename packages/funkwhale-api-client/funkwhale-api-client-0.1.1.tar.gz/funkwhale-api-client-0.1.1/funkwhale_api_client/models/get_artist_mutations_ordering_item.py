from enum import Enum


class GetArtistMutationsOrderingItem(str, Enum):
    VALUE_0 = "-creation_date"
    VALUE_1 = "-id"
    VALUE_2 = "-modification_date"
    VALUE_3 = "-name"
    VALUE_4 = "-random"
    VALUE_5 = "-related"
    CREATION_DATE = "creation_date"
    ID = "id"
    MODIFICATION_DATE = "modification_date"
    NAME = "name"
    RANDOM = "random"
    RELATED = "related"

    def __str__(self) -> str:
        return str(self.value)
