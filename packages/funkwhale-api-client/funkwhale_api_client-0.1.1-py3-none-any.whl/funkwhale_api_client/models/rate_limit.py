from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.ident import Ident
from ..models.scopes import Scopes

T = TypeVar("T", bound="RateLimit")


@attr.s(auto_attribs=True)
class RateLimit:
    """
    Attributes:
        enabled (bool):
        ident (Ident):
        scopes (List[Scopes]):
    """

    enabled: bool
    ident: Ident
    scopes: List[Scopes]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        ident = self.ident.to_dict()

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.to_dict()

            scopes.append(scopes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "ident": ident,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        ident = Ident.from_dict(d.pop("ident"))

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = Scopes.from_dict(scopes_item_data)

            scopes.append(scopes_item)

        rate_limit = cls(
            enabled=enabled,
            ident=ident,
            scopes=scopes,
        )

        rate_limit.additional_properties = d
        return rate_limit

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
