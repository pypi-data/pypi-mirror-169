import json
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.moderation_target_request import ModerationTargetRequest

T = TypeVar("T", bound="UserFilterRequest")


@attr.s(auto_attribs=True)
class UserFilterRequest:
    """
    Attributes:
        target (ModerationTargetRequest):
    """

    target: ModerationTargetRequest
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target = self.target.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target": target,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        target = (None, json.dumps(self.target.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target = ModerationTargetRequest.from_dict(d.pop("target"))

        user_filter_request = cls(
            target=target,
        )

        user_filter_request.additional_properties = d
        return user_filter_request

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
