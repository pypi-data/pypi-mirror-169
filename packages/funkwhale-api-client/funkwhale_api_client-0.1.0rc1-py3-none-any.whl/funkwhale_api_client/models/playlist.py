import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor
from ..models.privacy_level_enum import PrivacyLevelEnum
from ..models.user_basic import UserBasic
from ..types import UNSET, Unset

T = TypeVar("T", bound="Playlist")


@attr.s(auto_attribs=True)
class Playlist:
    """
    Attributes:
        id (int):
        name (str):
        user (UserBasic):
        modification_date (datetime.datetime):
        creation_date (datetime.datetime):
        tracks_count (int):
        album_covers (List[str]):
        duration (int):
        is_playable (bool):
        actor (APIActor):
        privacy_level (Union[Unset, PrivacyLevelEnum]):
    """

    id: int
    name: str
    user: UserBasic
    modification_date: datetime.datetime
    creation_date: datetime.datetime
    tracks_count: int
    album_covers: List[str]
    duration: int
    is_playable: bool
    actor: APIActor
    privacy_level: Union[Unset, PrivacyLevelEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        user = self.user.to_dict()

        modification_date = self.modification_date.isoformat()

        creation_date = self.creation_date.isoformat()

        tracks_count = self.tracks_count
        album_covers = self.album_covers

        duration = self.duration
        is_playable = self.is_playable
        actor = self.actor.to_dict()

        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "user": user,
                "modification_date": modification_date,
                "creation_date": creation_date,
                "tracks_count": tracks_count,
                "album_covers": album_covers,
                "duration": duration,
                "is_playable": is_playable,
                "actor": actor,
            }
        )
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        user = UserBasic.from_dict(d.pop("user"))

        modification_date = isoparse(d.pop("modification_date"))

        creation_date = isoparse(d.pop("creation_date"))

        tracks_count = d.pop("tracks_count")

        album_covers = cast(List[str], d.pop("album_covers"))

        duration = d.pop("duration")

        is_playable = d.pop("is_playable")

        actor = APIActor.from_dict(d.pop("actor"))

        _privacy_level = d.pop("privacy_level", UNSET)
        privacy_level: Union[Unset, PrivacyLevelEnum]
        if isinstance(_privacy_level, Unset):
            privacy_level = UNSET
        else:
            privacy_level = PrivacyLevelEnum(_privacy_level)

        playlist = cls(
            id=id,
            name=name,
            user=user,
            modification_date=modification_date,
            creation_date=creation_date,
            tracks_count=tracks_count,
            album_covers=album_covers,
            duration=duration,
            is_playable=is_playable,
            actor=actor,
            privacy_level=privacy_level,
        )

        playlist.additional_properties = d
        return playlist

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
