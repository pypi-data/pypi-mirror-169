from enum import Enum


class AdminGetAccountsType(str, Enum):
    APPLICATION = "Application"
    GROUP = "Group"
    ORGANIZATION = "Organization"
    PERSON = "Person"
    SERVICE = "Service"
    TOMBSTONE = "Tombstone"

    def __str__(self) -> str:
        return str(self.value)
