import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateApplication")


@attr.s(auto_attribs=True)
class CreateApplication:
    """
    Attributes:
        client_id (str):
        name (str):
        client_secret (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        scopes (Union[Unset, str]):  Default: 'read'.
        redirect_uris (Union[Unset, str]): Allowed URIs list, space separated
    """

    client_id: str
    name: str
    client_secret: str
    created: datetime.datetime
    updated: datetime.datetime
    scopes: Union[Unset, str] = "read"
    redirect_uris: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        name = self.name
        client_secret = self.client_secret
        created = self.created.isoformat()

        updated = self.updated.isoformat()

        scopes = self.scopes
        redirect_uris = self.redirect_uris

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "name": name,
                "client_secret": client_secret,
                "created": created,
                "updated": updated,
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
        client_id = d.pop("client_id")

        name = d.pop("name")

        client_secret = d.pop("client_secret")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        scopes = d.pop("scopes", UNSET)

        redirect_uris = d.pop("redirect_uris", UNSET)

        create_application = cls(
            client_id=client_id,
            name=name,
            client_secret=client_secret,
            created=created,
            updated=updated,
            scopes=scopes,
            redirect_uris=redirect_uris,
        )

        create_application.additional_properties = d
        return create_application

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
