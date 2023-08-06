from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Scopes")


@attr.s(auto_attribs=True)
class Scopes:
    """
    Attributes:
        id (str):
        rate (str):
        description (str):
        limit (int):
        duration (int):
        remaining (int):
        available (int):
        available_seconds (int):
        reset (int):
        reset_seconds (int):
    """

    id: str
    rate: str
    description: str
    limit: int
    duration: int
    remaining: int
    available: int
    available_seconds: int
    reset: int
    reset_seconds: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        rate = self.rate
        description = self.description
        limit = self.limit
        duration = self.duration
        remaining = self.remaining
        available = self.available
        available_seconds = self.available_seconds
        reset = self.reset
        reset_seconds = self.reset_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rate": rate,
                "description": description,
                "limit": limit,
                "duration": duration,
                "remaining": remaining,
                "available": available,
                "available_seconds": available_seconds,
                "reset": reset,
                "reset_seconds": reset_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        rate = d.pop("rate")

        description = d.pop("description")

        limit = d.pop("limit")

        duration = d.pop("duration")

        remaining = d.pop("remaining")

        available = d.pop("available")

        available_seconds = d.pop("available_seconds")

        reset = d.pop("reset")

        reset_seconds = d.pop("reset_seconds")

        scopes = cls(
            id=id,
            rate=rate,
            description=description,
            limit=limit,
            duration=duration,
            remaining=remaining,
            available=available,
            available_seconds=available_seconds,
            reset=reset,
            reset_seconds=reset_seconds,
        )

        scopes.additional_properties = d
        return scopes

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
