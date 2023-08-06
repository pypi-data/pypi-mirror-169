import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.cover_field_urls import CoverFieldUrls

T = TypeVar("T", bound="CoverField")


@attr.s(auto_attribs=True)
class CoverField:
    """
    Attributes:
        uuid (str):
        size (int):
        mimetype (str):
        creation_date (datetime.datetime):
        urls (CoverFieldUrls):
    """

    uuid: str
    size: int
    mimetype: str
    creation_date: datetime.datetime
    urls: CoverFieldUrls
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        size = self.size
        mimetype = self.mimetype
        creation_date = self.creation_date.isoformat()

        urls = self.urls.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "size": size,
                "mimetype": mimetype,
                "creation_date": creation_date,
                "urls": urls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        size = d.pop("size")

        mimetype = d.pop("mimetype")

        creation_date = isoparse(d.pop("creation_date"))

        urls = CoverFieldUrls.from_dict(d.pop("urls"))

        cover_field = cls(
            uuid=uuid,
            size=size,
            mimetype=mimetype,
            creation_date=creation_date,
            urls=urls,
        )

        cover_field.additional_properties = d
        return cover_field

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
