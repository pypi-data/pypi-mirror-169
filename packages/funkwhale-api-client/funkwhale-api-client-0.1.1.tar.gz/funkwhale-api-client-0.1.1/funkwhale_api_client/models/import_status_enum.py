from enum import Enum


class ImportStatusEnum(str, Enum):
    DRAFT = "draft"
    PENDING = "pending"
    FINISHED = "finished"
    ERRORED = "errored"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
