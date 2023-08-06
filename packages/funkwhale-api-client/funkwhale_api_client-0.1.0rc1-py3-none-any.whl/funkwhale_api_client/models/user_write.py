import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.content import Content
from ..models.privacy_level_enum import PrivacyLevelEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserWrite")


@attr.s(auto_attribs=True)
class UserWrite:
    """
    Attributes:
        name (Union[Unset, str]):
        privacy_level (Union[Unset, PrivacyLevelEnum]):
        instance_support_message_display_date (Union[Unset, None, datetime.datetime]):
        funkwhale_support_message_display_date (Union[Unset, None, datetime.datetime]):
        summary (Union[Unset, None, Content]):
    """

    name: Union[Unset, str] = UNSET
    privacy_level: Union[Unset, PrivacyLevelEnum] = UNSET
    instance_support_message_display_date: Union[Unset, None, datetime.datetime] = UNSET
    funkwhale_support_message_display_date: Union[Unset, None, datetime.datetime] = UNSET
    summary: Union[Unset, None, Content] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        instance_support_message_display_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.instance_support_message_display_date, Unset):
            instance_support_message_display_date = (
                self.instance_support_message_display_date.isoformat()
                if self.instance_support_message_display_date
                else None
            )

        funkwhale_support_message_display_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.funkwhale_support_message_display_date, Unset):
            funkwhale_support_message_display_date = (
                self.funkwhale_support_message_display_date.isoformat()
                if self.funkwhale_support_message_display_date
                else None
            )

        summary: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict() if self.summary else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level
        if instance_support_message_display_date is not UNSET:
            field_dict["instance_support_message_display_date"] = instance_support_message_display_date
        if funkwhale_support_message_display_date is not UNSET:
            field_dict["funkwhale_support_message_display_date"] = funkwhale_support_message_display_date
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _privacy_level = d.pop("privacy_level", UNSET)
        privacy_level: Union[Unset, PrivacyLevelEnum]
        if isinstance(_privacy_level, Unset):
            privacy_level = UNSET
        else:
            privacy_level = PrivacyLevelEnum(_privacy_level)

        _instance_support_message_display_date = d.pop("instance_support_message_display_date", UNSET)
        instance_support_message_display_date: Union[Unset, None, datetime.datetime]
        if _instance_support_message_display_date is None:
            instance_support_message_display_date = None
        elif isinstance(_instance_support_message_display_date, Unset):
            instance_support_message_display_date = UNSET
        else:
            instance_support_message_display_date = isoparse(_instance_support_message_display_date)

        _funkwhale_support_message_display_date = d.pop("funkwhale_support_message_display_date", UNSET)
        funkwhale_support_message_display_date: Union[Unset, None, datetime.datetime]
        if _funkwhale_support_message_display_date is None:
            funkwhale_support_message_display_date = None
        elif isinstance(_funkwhale_support_message_display_date, Unset):
            funkwhale_support_message_display_date = UNSET
        else:
            funkwhale_support_message_display_date = isoparse(_funkwhale_support_message_display_date)

        _summary = d.pop("summary", UNSET)
        summary: Union[Unset, None, Content]
        if _summary is None:
            summary = None
        elif isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = Content.from_dict(_summary)

        user_write = cls(
            name=name,
            privacy_level=privacy_level,
            instance_support_message_display_date=instance_support_message_display_date,
            funkwhale_support_message_display_date=funkwhale_support_message_display_date,
            summary=summary,
        )

        user_write.additional_properties = d
        return user_write

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
