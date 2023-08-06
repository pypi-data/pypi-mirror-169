from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationRequest")


@attr.s(auto_attribs=True)
class ApplicationRequest:
    """
    Attributes:
        scopes (str):
        client_id (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    scopes: str
    client_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scopes = self.scopes
        client_id = self.client_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scopes": scopes,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        scopes = self.scopes if isinstance(self.scopes, Unset) else (None, str(self.scopes).encode(), "text/plain")
        client_id = (
            self.client_id if isinstance(self.client_id, Unset) else (None, str(self.client_id).encode(), "text/plain")
        )
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "scopes": scopes,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scopes = d.pop("scopes")

        client_id = d.pop("client_id", UNSET)

        name = d.pop("name", UNSET)

        application_request = cls(
            scopes=scopes,
            client_id=client_id,
            name=name,
        )

        application_request.additional_properties = d
        return application_request

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
