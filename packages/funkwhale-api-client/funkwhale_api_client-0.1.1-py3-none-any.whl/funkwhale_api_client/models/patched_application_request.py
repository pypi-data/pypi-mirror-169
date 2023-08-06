from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedApplicationRequest")


@attr.s(auto_attribs=True)
class PatchedApplicationRequest:
    """
    Attributes:
        client_id (Union[Unset, str]):
        name (Union[Unset, str]):
        scopes (Union[Unset, str]):
    """

    client_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    scopes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        name = self.name
        scopes = self.scopes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if name is not UNSET:
            field_dict["name"] = name
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        client_id = (
            self.client_id if isinstance(self.client_id, Unset) else (None, str(self.client_id).encode(), "text/plain")
        )
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        scopes = self.scopes if isinstance(self.scopes, Unset) else (None, str(self.scopes).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if name is not UNSET:
            field_dict["name"] = name
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("client_id", UNSET)

        name = d.pop("name", UNSET)

        scopes = d.pop("scopes", UNSET)

        patched_application_request = cls(
            client_id=client_id,
            name=name,
            scopes=scopes,
        )

        patched_application_request.additional_properties = d
        return patched_application_request

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
