from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.privacy_level_enum import PrivacyLevelEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaylistRequest")


@attr.s(auto_attribs=True)
class PlaylistRequest:
    """
    Attributes:
        name (str):
        privacy_level (Union[Unset, PrivacyLevelEnum]):
    """

    name: str
    privacy_level: Union[Unset, PrivacyLevelEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        privacy_level: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = (None, str(self.privacy_level.value).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
            }
        )
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        _privacy_level = d.pop("privacy_level", UNSET)
        privacy_level: Union[Unset, PrivacyLevelEnum]
        if isinstance(_privacy_level, Unset):
            privacy_level = UNSET
        else:
            privacy_level = PrivacyLevelEnum(_privacy_level)

        playlist_request = cls(
            name=name,
            privacy_level=privacy_level,
        )

        playlist_request.additional_properties = d
        return playlist_request

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
