from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Endpoints")


@attr.s(auto_attribs=True)
class Endpoints:
    """
    Attributes:
        known_nodes (Union[Unset, str]):
        channels (Union[Unset, str]):
        libraries (Union[Unset, str]):
    """

    known_nodes: Union[Unset, str] = UNSET
    channels: Union[Unset, str] = UNSET
    libraries: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        known_nodes = self.known_nodes
        channels = self.channels
        libraries = self.libraries

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if known_nodes is not UNSET:
            field_dict["knownNodes"] = known_nodes
        if channels is not UNSET:
            field_dict["channels"] = channels
        if libraries is not UNSET:
            field_dict["libraries"] = libraries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        known_nodes = d.pop("knownNodes", UNSET)

        channels = d.pop("channels", UNSET)

        libraries = d.pop("libraries", UNSET)

        endpoints = cls(
            known_nodes=known_nodes,
            channels=channels,
            libraries=libraries,
        )

        endpoints.additional_properties = d
        return endpoints

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
