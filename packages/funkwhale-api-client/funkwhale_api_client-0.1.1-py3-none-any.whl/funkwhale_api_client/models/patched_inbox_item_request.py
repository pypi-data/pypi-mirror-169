import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.activity_request import ActivityRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedInboxItemRequest")


@attr.s(auto_attribs=True)
class PatchedInboxItemRequest:
    """
    Attributes:
        activity (Union[Unset, ActivityRequest]):
        is_read (Union[Unset, bool]):
    """

    activity: Union[Unset, ActivityRequest] = UNSET
    is_read: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        activity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        is_read = self.is_read

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity is not UNSET:
            field_dict["activity"] = activity
        if is_read is not UNSET:
            field_dict["is_read"] = is_read

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        activity: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.activity, Unset):
            activity = (None, json.dumps(self.activity.to_dict()).encode(), "application/json")

        is_read = self.is_read if isinstance(self.is_read, Unset) else (None, str(self.is_read).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if activity is not UNSET:
            field_dict["activity"] = activity
        if is_read is not UNSET:
            field_dict["is_read"] = is_read

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _activity = d.pop("activity", UNSET)
        activity: Union[Unset, ActivityRequest]
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = ActivityRequest.from_dict(_activity)

        is_read = d.pop("is_read", UNSET)

        patched_inbox_item_request = cls(
            activity=activity,
            is_read=is_read,
        )

        patched_inbox_item_request.additional_properties = d
        return patched_inbox_item_request

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
