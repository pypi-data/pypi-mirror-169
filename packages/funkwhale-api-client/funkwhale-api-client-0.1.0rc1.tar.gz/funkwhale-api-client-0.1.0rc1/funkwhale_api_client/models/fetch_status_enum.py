from enum import Enum


class FetchStatusEnum(str, Enum):
    PENDING = "pending"
    ERRORED = "errored"
    FINISHED = "finished"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
