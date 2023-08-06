import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor
from ..models.fetch_detail import FetchDetail
from ..models.fetch_status_enum import FetchStatusEnum

T = TypeVar("T", bound="Fetch")


@attr.s(auto_attribs=True)
class Fetch:
    """
    Attributes:
        id (int):
        url (str):
        actor (APIActor):
        status (FetchStatusEnum):
        detail (FetchDetail):
        creation_date (datetime.datetime):
        fetch_date (Optional[datetime.datetime]):
    """

    id: int
    url: str
    actor: APIActor
    status: FetchStatusEnum
    detail: FetchDetail
    creation_date: datetime.datetime
    fetch_date: Optional[datetime.datetime]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        actor = self.actor.to_dict()

        status = self.status.value

        detail = self.detail.to_dict()

        creation_date = self.creation_date.isoformat()

        fetch_date = self.fetch_date.isoformat() if self.fetch_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "actor": actor,
                "status": status,
                "detail": detail,
                "creation_date": creation_date,
                "fetch_date": fetch_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        actor = APIActor.from_dict(d.pop("actor"))

        status = FetchStatusEnum(d.pop("status"))

        detail = FetchDetail.from_dict(d.pop("detail"))

        creation_date = isoparse(d.pop("creation_date"))

        _fetch_date = d.pop("fetch_date")
        fetch_date: Optional[datetime.datetime]
        if _fetch_date is None:
            fetch_date = None
        else:
            fetch_date = isoparse(_fetch_date)

        fetch = cls(
            id=id,
            url=url,
            actor=actor,
            status=status,
            detail=detail,
            creation_date=creation_date,
            fetch_date=fetch_date,
        )

        fetch.additional_properties = d
        return fetch

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
