from enum import Enum


class ManageTargetTypeEnum(str, Enum):
    DOMAIN = "domain"
    ACTOR = "actor"

    def __str__(self) -> str:
        return str(self.value)
