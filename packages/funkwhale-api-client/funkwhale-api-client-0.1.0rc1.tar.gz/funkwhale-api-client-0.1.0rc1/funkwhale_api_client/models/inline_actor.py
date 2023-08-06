from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="InlineActor")


@attr.s(auto_attribs=True)
class InlineActor:
    """
    Attributes:
        full_username (str):
        preferred_username (str):
        domain (str):
    """

    full_username: str
    preferred_username: str
    domain: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_username = self.full_username
        preferred_username = self.preferred_username
        domain = self.domain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "full_username": full_username,
                "preferred_username": preferred_username,
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        full_username = d.pop("full_username")

        preferred_username = d.pop("preferred_username")

        domain = d.pop("domain")

        inline_actor = cls(
            full_username=full_username,
            preferred_username=preferred_username,
            domain=domain,
        )

        inline_actor.additional_properties = d
        return inline_actor

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
