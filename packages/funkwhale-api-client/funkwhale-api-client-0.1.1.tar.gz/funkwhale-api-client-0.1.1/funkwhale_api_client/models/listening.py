import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor
from ..models.track import Track
from ..models.user_basic import UserBasic
from ..types import UNSET, Unset

T = TypeVar("T", bound="Listening")


@attr.s(auto_attribs=True)
class Listening:
    """
    Attributes:
        id (int):
        user (UserBasic):
        track (Track):
        actor (APIActor):
        creation_date (Union[Unset, None, datetime.datetime]):
    """

    id: int
    user: UserBasic
    track: Track
    actor: APIActor
    creation_date: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user = self.user.to_dict()

        track = self.track.to_dict()

        actor = self.actor.to_dict()

        creation_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat() if self.creation_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user": user,
                "track": track,
                "actor": actor,
            }
        )
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        user = UserBasic.from_dict(d.pop("user"))

        track = Track.from_dict(d.pop("track"))

        actor = APIActor.from_dict(d.pop("actor"))

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, None, datetime.datetime]
        if _creation_date is None:
            creation_date = None
        elif isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        listening = cls(
            id=id,
            user=user,
            track=track,
            actor=actor,
            creation_date=creation_date,
        )

        listening.additional_properties = d
        return listening

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
