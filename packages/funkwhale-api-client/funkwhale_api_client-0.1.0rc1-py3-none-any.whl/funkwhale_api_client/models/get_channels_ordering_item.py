from enum import Enum


class GetChannelsOrderingItem(str, Enum):
    VALUE_0 = "-creation_date"
    VALUE_1 = "-modification_date"
    VALUE_2 = "-random"
    CREATION_DATE = "creation_date"
    MODIFICATION_DATE = "modification_date"
    RANDOM = "random"

    def __str__(self) -> str:
        return str(self.value)
