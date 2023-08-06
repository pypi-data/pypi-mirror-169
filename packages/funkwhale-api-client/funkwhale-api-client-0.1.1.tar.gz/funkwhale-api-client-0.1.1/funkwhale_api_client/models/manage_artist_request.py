import datetime
import json
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.content_category_enum import ContentCategoryEnum
from ..models.cover_field_request import CoverFieldRequest
from ..models.manage_base_actor_request import ManageBaseActorRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageArtistRequest")


@attr.s(auto_attribs=True)
class ManageArtistRequest:
    """
    Attributes:
        name (str):
        domain (str):
        attributed_to (ManageBaseActorRequest):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        cover (Optional[CoverFieldRequest]):
        content_category (Union[Unset, ContentCategoryEnum]):
    """

    name: str
    domain: str
    attributed_to: ManageBaseActorRequest
    cover: Optional[CoverFieldRequest]
    fid: Union[Unset, None, str] = UNSET
    mbid: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    content_category: Union[Unset, ContentCategoryEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        domain = self.domain
        attributed_to = self.attributed_to.to_dict()

        fid = self.fid
        mbid = self.mbid
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        cover = self.cover.to_dict() if self.cover else None

        content_category: Union[Unset, str] = UNSET
        if not isinstance(self.content_category, Unset):
            content_category = self.content_category.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "domain": domain,
                "attributed_to": attributed_to,
                "cover": cover,
            }
        )
        if fid is not UNSET:
            field_dict["fid"] = fid
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if content_category is not UNSET:
            field_dict["content_category"] = content_category

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        domain = self.domain if isinstance(self.domain, Unset) else (None, str(self.domain).encode(), "text/plain")
        attributed_to = (None, json.dumps(self.attributed_to.to_dict()).encode(), "application/json")

        fid = self.fid if isinstance(self.fid, Unset) else (None, str(self.fid).encode(), "text/plain")
        mbid = self.mbid if isinstance(self.mbid, Unset) else (None, str(self.mbid).encode(), "text/plain")
        creation_date: Union[Unset, bytes] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat().encode()

        cover = (None, json.dumps(self.cover.to_dict()).encode(), "application/json") if self.cover else None

        content_category: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.content_category, Unset):
            content_category = (None, str(self.content_category.value).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
                "domain": domain,
                "attributed_to": attributed_to,
                "cover": cover,
            }
        )
        if fid is not UNSET:
            field_dict["fid"] = fid
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if content_category is not UNSET:
            field_dict["content_category"] = content_category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        domain = d.pop("domain")

        attributed_to = ManageBaseActorRequest.from_dict(d.pop("attributed_to"))

        fid = d.pop("fid", UNSET)

        mbid = d.pop("mbid", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _cover = d.pop("cover")
        cover: Optional[CoverFieldRequest]
        if _cover is None:
            cover = None
        else:
            cover = CoverFieldRequest.from_dict(_cover)

        _content_category = d.pop("content_category", UNSET)
        content_category: Union[Unset, ContentCategoryEnum]
        if isinstance(_content_category, Unset):
            content_category = UNSET
        else:
            content_category = ContentCategoryEnum(_content_category)

        manage_artist_request = cls(
            name=name,
            domain=domain,
            attributed_to=attributed_to,
            fid=fid,
            mbid=mbid,
            creation_date=creation_date,
            cover=cover,
            content_category=content_category,
        )

        manage_artist_request.additional_properties = d
        return manage_artist_request

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
