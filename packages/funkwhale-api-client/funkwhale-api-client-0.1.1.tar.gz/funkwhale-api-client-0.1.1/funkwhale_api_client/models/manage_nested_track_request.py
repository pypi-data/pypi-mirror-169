import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageNestedTrackRequest")


@attr.s(auto_attribs=True)
class ManageNestedTrackRequest:
    """
    Attributes:
        title (str):
        domain (str):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        position (Union[Unset, None, int]):
        disc_number (Union[Unset, None, int]):
        copyright_ (Union[Unset, None, str]):
        license_ (Union[Unset, None, str]):
    """

    title: str
    domain: str
    fid: Union[Unset, None, str] = UNSET
    mbid: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    position: Union[Unset, None, int] = UNSET
    disc_number: Union[Unset, None, int] = UNSET
    copyright_: Union[Unset, None, str] = UNSET
    license_: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        domain = self.domain
        fid = self.fid
        mbid = self.mbid
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        position = self.position
        disc_number = self.disc_number
        copyright_ = self.copyright_
        license_ = self.license_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "domain": domain,
            }
        )
        if fid is not UNSET:
            field_dict["fid"] = fid
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if position is not UNSET:
            field_dict["position"] = position
        if disc_number is not UNSET:
            field_dict["disc_number"] = disc_number
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if license_ is not UNSET:
            field_dict["license"] = license_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        domain = d.pop("domain")

        fid = d.pop("fid", UNSET)

        mbid = d.pop("mbid", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        position = d.pop("position", UNSET)

        disc_number = d.pop("disc_number", UNSET)

        copyright_ = d.pop("copyright", UNSET)

        license_ = d.pop("license", UNSET)

        manage_nested_track_request = cls(
            title=title,
            domain=domain,
            fid=fid,
            mbid=mbid,
            creation_date=creation_date,
            position=position,
            disc_number=disc_number,
            copyright_=copyright_,
            license_=license_,
        )

        manage_nested_track_request.additional_properties = d
        return manage_nested_track_request

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
