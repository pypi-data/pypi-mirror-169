import json
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.radio_request_config import RadioRequestConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="RadioRequest")


@attr.s(auto_attribs=True)
class RadioRequest:
    """
    Attributes:
        name (str):
        config (RadioRequestConfig):
        is_public (Union[Unset, bool]):
        description (Union[Unset, str]):
    """

    name: str
    config: RadioRequestConfig
    is_public: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        config = self.config.to_dict()

        is_public = self.is_public
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "config": config,
            }
        )
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        config = (None, json.dumps(self.config.to_dict()).encode(), "application/json")

        is_public = (
            self.is_public if isinstance(self.is_public, Unset) else (None, str(self.is_public).encode(), "text/plain")
        )
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
                "config": config,
            }
        )
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        config = RadioRequestConfig.from_dict(d.pop("config"))

        is_public = d.pop("is_public", UNSET)

        description = d.pop("description", UNSET)

        radio_request = cls(
            name=name,
            config=config,
            is_public=is_public,
            description=description,
        )

        radio_request.additional_properties = d
        return radio_request

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
