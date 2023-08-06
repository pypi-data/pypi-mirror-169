from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateApplicationRequest")


@attr.s(auto_attribs=True)
class CreateApplicationRequest:
    """
    Attributes:
        name (str):
        scopes (Union[Unset, str]):  Default: 'read'.
        redirect_uris (Union[Unset, str]): Allowed URIs list, space separated
    """

    name: str
    scopes: Union[Unset, str] = "read"
    redirect_uris: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        scopes = self.scopes
        redirect_uris = self.redirect_uris

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        scopes = self.scopes if isinstance(self.scopes, Unset) else (None, str(self.scopes).encode(), "text/plain")
        redirect_uris = (
            self.redirect_uris
            if isinstance(self.redirect_uris, Unset)
            else (None, str(self.redirect_uris).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
            }
        )
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        scopes = d.pop("scopes", UNSET)

        redirect_uris = d.pop("redirect_uris", UNSET)

        create_application_request = cls(
            name=name,
            scopes=scopes,
            redirect_uris=redirect_uris,
        )

        create_application_request.additional_properties = d
        return create_application_request

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
