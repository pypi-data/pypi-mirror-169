from enum import Enum


class GetUploadsImportStatusItem(str, Enum):
    DRAFT = "draft"
    ERRORED = "errored"
    FINISHED = "finished"
    PENDING = "pending"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
