import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.manage_domain_nodeinfo import ManageDomainNodeinfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageDomain")


@attr.s(auto_attribs=True)
class ManageDomain:
    """
    Attributes:
        name (str):
        creation_date (datetime.datetime):
        actors_count (int):
        outbox_activities_count (int):
        nodeinfo (ManageDomainNodeinfo):
        instance_policy (int):
        nodeinfo_fetch_date (Optional[datetime.datetime]):
        allowed (Union[Unset, None, bool]):
    """

    name: str
    creation_date: datetime.datetime
    actors_count: int
    outbox_activities_count: int
    nodeinfo: ManageDomainNodeinfo
    instance_policy: int
    nodeinfo_fetch_date: Optional[datetime.datetime]
    allowed: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        creation_date = self.creation_date.isoformat()

        actors_count = self.actors_count
        outbox_activities_count = self.outbox_activities_count
        nodeinfo = self.nodeinfo.to_dict()

        instance_policy = self.instance_policy
        nodeinfo_fetch_date = self.nodeinfo_fetch_date.isoformat() if self.nodeinfo_fetch_date else None

        allowed = self.allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "creation_date": creation_date,
                "actors_count": actors_count,
                "outbox_activities_count": outbox_activities_count,
                "nodeinfo": nodeinfo,
                "instance_policy": instance_policy,
                "nodeinfo_fetch_date": nodeinfo_fetch_date,
            }
        )
        if allowed is not UNSET:
            field_dict["allowed"] = allowed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        creation_date = isoparse(d.pop("creation_date"))

        actors_count = d.pop("actors_count")

        outbox_activities_count = d.pop("outbox_activities_count")

        nodeinfo = ManageDomainNodeinfo.from_dict(d.pop("nodeinfo"))

        instance_policy = d.pop("instance_policy")

        _nodeinfo_fetch_date = d.pop("nodeinfo_fetch_date")
        nodeinfo_fetch_date: Optional[datetime.datetime]
        if _nodeinfo_fetch_date is None:
            nodeinfo_fetch_date = None
        else:
            nodeinfo_fetch_date = isoparse(_nodeinfo_fetch_date)

        allowed = d.pop("allowed", UNSET)

        manage_domain = cls(
            name=name,
            creation_date=creation_date,
            actors_count=actors_count,
            outbox_activities_count=outbox_activities_count,
            nodeinfo=nodeinfo,
            instance_policy=instance_policy,
            nodeinfo_fetch_date=nodeinfo_fetch_date,
            allowed=allowed,
        )

        manage_domain.additional_properties = d
        return manage_domain

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
