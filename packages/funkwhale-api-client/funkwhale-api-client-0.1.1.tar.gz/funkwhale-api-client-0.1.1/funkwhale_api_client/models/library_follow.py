import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor

T = TypeVar("T", bound="LibraryFollow")


@attr.s(auto_attribs=True)
class LibraryFollow:
    """
    Attributes:
        creation_date (datetime.datetime):
        actor (APIActor):
        uuid (str):
        target (str):
        approved (Optional[bool]):
    """

    creation_date: datetime.datetime
    actor: APIActor
    uuid: str
    target: str
    approved: Optional[bool]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_date = self.creation_date.isoformat()

        actor = self.actor.to_dict()

        uuid = self.uuid
        target = self.target
        approved = self.approved

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creation_date": creation_date,
                "actor": actor,
                "uuid": uuid,
                "target": target,
                "approved": approved,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        creation_date = isoparse(d.pop("creation_date"))

        actor = APIActor.from_dict(d.pop("actor"))

        uuid = d.pop("uuid")

        target = d.pop("target")

        approved = d.pop("approved")

        library_follow = cls(
            creation_date=creation_date,
            actor=actor,
            uuid=uuid,
            target=target,
            approved=approved,
        )

        library_follow.additional_properties = d
        return library_follow

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
