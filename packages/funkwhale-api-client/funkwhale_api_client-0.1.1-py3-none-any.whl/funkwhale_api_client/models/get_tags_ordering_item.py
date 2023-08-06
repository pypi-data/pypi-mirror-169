from enum import Enum


class GetTagsOrderingItem(str, Enum):
    VALUE_0 = "-creation_date"
    VALUE_1 = "-length"
    VALUE_2 = "-name"
    CREATION_DATE = "creation_date"
    LENGTH = "length"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
