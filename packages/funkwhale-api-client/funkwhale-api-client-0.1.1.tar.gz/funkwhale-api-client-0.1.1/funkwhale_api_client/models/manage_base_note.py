import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.manage_base_actor import ManageBaseActor

T = TypeVar("T", bound="ManageBaseNote")


@attr.s(auto_attribs=True)
class ManageBaseNote:
    """
    Attributes:
        id (int):
        uuid (str):
        creation_date (datetime.datetime):
        summary (str):
        author (ManageBaseActor):
    """

    id: int
    uuid: str
    creation_date: datetime.datetime
    summary: str
    author: ManageBaseActor
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        uuid = self.uuid
        creation_date = self.creation_date.isoformat()

        summary = self.summary
        author = self.author.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "creation_date": creation_date,
                "summary": summary,
                "author": author,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        uuid = d.pop("uuid")

        creation_date = isoparse(d.pop("creation_date"))

        summary = d.pop("summary")

        author = ManageBaseActor.from_dict(d.pop("author"))

        manage_base_note = cls(
            id=id,
            uuid=uuid,
            creation_date=creation_date,
            summary=summary,
            author=author,
        )

        manage_base_note.additional_properties = d
        return manage_base_note

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
