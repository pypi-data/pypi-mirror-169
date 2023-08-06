import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Application")


@attr.s(auto_attribs=True)
class Application:
    """
    Attributes:
        scopes (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        client_id (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    scopes: str
    created: datetime.datetime
    updated: datetime.datetime
    client_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scopes = self.scopes
        created = self.created.isoformat()

        updated = self.updated.isoformat()

        client_id = self.client_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scopes": scopes,
                "created": created,
                "updated": updated,
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

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        client_id = d.pop("client_id", UNSET)

        name = d.pop("name", UNSET)

        application = cls(
            scopes=scopes,
            created=created,
            updated=updated,
            client_id=client_id,
            name=name,
        )

        application.additional_properties = d
        return application

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
