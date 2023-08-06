from enum import Enum


class FederationChoiceEnum(str, Enum):
    PERSON = "Person"
    TOMBSTONE = "Tombstone"
    APPLICATION = "Application"
    GROUP = "Group"
    ORGANIZATION = "Organization"
    SERVICE = "Service"

    def __str__(self) -> str:
        return str(self.value)
