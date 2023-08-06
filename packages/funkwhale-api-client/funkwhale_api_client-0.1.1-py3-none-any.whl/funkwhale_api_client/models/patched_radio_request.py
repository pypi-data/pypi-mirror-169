import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.patched_radio_request_config import PatchedRadioRequestConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRadioRequest")


@attr.s(auto_attribs=True)
class PatchedRadioRequest:
    """
    Attributes:
        is_public (Union[Unset, bool]):
        name (Union[Unset, str]):
        config (Union[Unset, PatchedRadioRequestConfig]):
        description (Union[Unset, str]):
    """

    is_public: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    config: Union[Unset, PatchedRadioRequestConfig] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_public = self.is_public
        name = self.name
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if name is not UNSET:
            field_dict["name"] = name
        if config is not UNSET:
            field_dict["config"] = config
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        is_public = (
            self.is_public if isinstance(self.is_public, Unset) else (None, str(self.is_public).encode(), "text/plain")
        )
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        config: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.config, Unset):
            config = (None, json.dumps(self.config.to_dict()).encode(), "application/json")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if name is not UNSET:
            field_dict["name"] = name
        if config is not UNSET:
            field_dict["config"] = config
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_public = d.pop("is_public", UNSET)

        name = d.pop("name", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, PatchedRadioRequestConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PatchedRadioRequestConfig.from_dict(_config)

        description = d.pop("description", UNSET)

        patched_radio_request = cls(
            is_public=is_public,
            name=name,
            config=config,
            description=description,
        )

        patched_radio_request.additional_properties = d
        return patched_radio_request

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
