import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.radio_config import RadioConfig
from ..models.user_basic import UserBasic
from ..types import UNSET, Unset

T = TypeVar("T", bound="Radio")


@attr.s(auto_attribs=True)
class Radio:
    """
    Attributes:
        id (int):
        name (str):
        creation_date (datetime.datetime):
        user (UserBasic):
        config (RadioConfig):
        is_public (Union[Unset, bool]):
        description (Union[Unset, str]):
    """

    id: int
    name: str
    creation_date: datetime.datetime
    user: UserBasic
    config: RadioConfig
    is_public: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        creation_date = self.creation_date.isoformat()

        user = self.user.to_dict()

        config = self.config.to_dict()

        is_public = self.is_public
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "creation_date": creation_date,
                "user": user,
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
        id = d.pop("id")

        name = d.pop("name")

        creation_date = isoparse(d.pop("creation_date"))

        user = UserBasic.from_dict(d.pop("user"))

        config = RadioConfig.from_dict(d.pop("config"))

        is_public = d.pop("is_public", UNSET)

        description = d.pop("description", UNSET)

        radio = cls(
            id=id,
            name=name,
            creation_date=creation_date,
            user=user,
            config=config,
            is_public=is_public,
            description=description,
        )

        radio.additional_properties = d
        return radio

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
