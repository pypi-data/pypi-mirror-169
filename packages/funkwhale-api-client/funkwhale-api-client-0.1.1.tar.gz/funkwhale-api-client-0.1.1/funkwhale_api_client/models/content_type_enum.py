from enum import Enum


class ContentTypeEnum(str, Enum):
    TEXTHTML = "text/html"
    TEXTMARKDOWN = "text/markdown"
    TEXTPLAIN = "text/plain"

    def __str__(self) -> str:
        return str(self.value)
