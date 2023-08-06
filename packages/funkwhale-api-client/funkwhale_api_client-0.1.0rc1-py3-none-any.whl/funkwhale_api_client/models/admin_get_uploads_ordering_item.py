from enum import Enum


class AdminGetUploadsOrderingItem(str, Enum):
    VALUE_0 = "-accessed_date"
    VALUE_1 = "-bitrate"
    VALUE_2 = "-creation_date"
    VALUE_3 = "-duration"
    VALUE_4 = "-modification_date"
    VALUE_5 = "-size"
    ACCESSED_DATE = "accessed_date"
    BITRATE = "bitrate"
    CREATION_DATE = "creation_date"
    DURATION = "duration"
    MODIFICATION_DATE = "modification_date"
    SIZE = "size"

    def __str__(self) -> str:
        return str(self.value)
