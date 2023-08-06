import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageTag")


@attr.s(auto_attribs=True)
class ManageTag:
    """
    Attributes:
        id (int):
        name (str):
        tracks_count (int):
        albums_count (int):
        artists_count (int):
        creation_date (Union[Unset, datetime.datetime]):
    """

    id: int
    name: str
    tracks_count: int
    albums_count: int
    artists_count: int
    creation_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        tracks_count = self.tracks_count
        albums_count = self.albums_count
        artists_count = self.artists_count
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "tracks_count": tracks_count,
                "albums_count": albums_count,
                "artists_count": artists_count,
            }
        )
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        tracks_count = d.pop("tracks_count")

        albums_count = d.pop("albums_count")

        artists_count = d.pop("artists_count")

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        manage_tag = cls(
            id=id,
            name=name,
            tracks_count=tracks_count,
            albums_count=albums_count,
            artists_count=artists_count,
            creation_date=creation_date,
        )

        manage_tag.additional_properties = d
        return manage_tag

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
