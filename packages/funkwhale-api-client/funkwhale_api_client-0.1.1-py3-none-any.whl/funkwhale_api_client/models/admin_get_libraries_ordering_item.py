from enum import Enum


class AdminGetLibrariesOrderingItem(str, Enum):
    VALUE_0 = "-creation_date"
    VALUE_1 = "-followers_count"
    VALUE_2 = "-uploads_count"
    CREATION_DATE = "creation_date"
    FOLLOWERS_COUNT = "followers_count"
    UPLOADS_COUNT = "uploads_count"

    def __str__(self) -> str:
        return str(self.value)
