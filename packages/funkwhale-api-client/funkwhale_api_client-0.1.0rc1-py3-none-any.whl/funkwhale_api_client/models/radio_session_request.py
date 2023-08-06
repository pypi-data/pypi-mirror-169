import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.radio_session_request_config import RadioSessionRequestConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="RadioSessionRequest")


@attr.s(auto_attribs=True)
class RadioSessionRequest:
    """
    Attributes:
        radio_type (str):
        related_object_id (Union[Unset, None, str]):
        user (Union[Unset, None, int]):
        creation_date (Union[Unset, datetime.datetime]):
        custom_radio (Union[Unset, None, int]):
        config (Union[Unset, None, RadioSessionRequestConfig]):
    """

    radio_type: str
    related_object_id: Union[Unset, None, str] = UNSET
    user: Union[Unset, None, int] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    custom_radio: Union[Unset, None, int] = UNSET
    config: Union[Unset, None, RadioSessionRequestConfig] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        radio_type = self.radio_type
        related_object_id = self.related_object_id
        user = self.user
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        custom_radio = self.custom_radio
        config: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict() if self.config else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "radio_type": radio_type,
            }
        )
        if related_object_id is not UNSET:
            field_dict["related_object_id"] = related_object_id
        if user is not UNSET:
            field_dict["user"] = user
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if custom_radio is not UNSET:
            field_dict["custom_radio"] = custom_radio
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        radio_type = (
            self.radio_type
            if isinstance(self.radio_type, Unset)
            else (None, str(self.radio_type).encode(), "text/plain")
        )
        related_object_id = (
            self.related_object_id
            if isinstance(self.related_object_id, Unset)
            else (None, str(self.related_object_id).encode(), "text/plain")
        )
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        creation_date: Union[Unset, bytes] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat().encode()

        custom_radio = (
            self.custom_radio
            if isinstance(self.custom_radio, Unset)
            else (None, str(self.custom_radio).encode(), "text/plain")
        )
        config: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.config, Unset):
            config = (None, json.dumps(self.config.to_dict()).encode(), "application/json") if self.config else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "radio_type": radio_type,
            }
        )
        if related_object_id is not UNSET:
            field_dict["related_object_id"] = related_object_id
        if user is not UNSET:
            field_dict["user"] = user
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if custom_radio is not UNSET:
            field_dict["custom_radio"] = custom_radio
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        radio_type = d.pop("radio_type")

        related_object_id = d.pop("related_object_id", UNSET)

        user = d.pop("user", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        custom_radio = d.pop("custom_radio", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, None, RadioSessionRequestConfig]
        if _config is None:
            config = None
        elif isinstance(_config, Unset):
            config = UNSET
        else:
            config = RadioSessionRequestConfig.from_dict(_config)

        radio_session_request = cls(
            radio_type=radio_type,
            related_object_id=related_object_id,
            user=user,
            creation_date=creation_date,
            custom_radio=custom_radio,
            config=config,
        )

        radio_session_request.additional_properties = d
        return radio_session_request

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
