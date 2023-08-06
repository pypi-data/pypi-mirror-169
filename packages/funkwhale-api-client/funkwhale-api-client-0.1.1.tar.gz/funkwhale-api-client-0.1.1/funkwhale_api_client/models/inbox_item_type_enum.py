from enum import Enum


class InboxItemTypeEnum(str, Enum):
    TO = "to"
    CC = "cc"

    def __str__(self) -> str:
        return str(self.value)
