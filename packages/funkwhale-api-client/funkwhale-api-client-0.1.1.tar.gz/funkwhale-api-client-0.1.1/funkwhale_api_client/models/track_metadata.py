from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackMetadata")


@attr.s(auto_attribs=True)
class TrackMetadata:
    """
    Attributes:
        album (str):
        artists (str):
        title (Union[Unset, None, str]):
        position (Union[Unset, None, str]):
        disc_number (Union[Unset, None, str]):
        copyright_ (Union[Unset, None, str]):
        license_ (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        tags (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        cover_data (Union[Unset, str]):
    """

    album: str
    artists: str
    title: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, str] = UNSET
    disc_number: Union[Unset, None, str] = UNSET
    copyright_: Union[Unset, None, str] = UNSET
    license_: Union[Unset, None, str] = UNSET
    mbid: Union[Unset, None, str] = UNSET
    tags: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    cover_data: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album = self.album
        artists = self.artists
        title = self.title
        position = self.position
        disc_number = self.disc_number
        copyright_ = self.copyright_
        license_ = self.license_
        mbid = self.mbid
        tags = self.tags
        description = self.description
        cover_data = self.cover_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "album": album,
                "artists": artists,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if position is not UNSET:
            field_dict["position"] = position
        if disc_number is not UNSET:
            field_dict["disc_number"] = disc_number
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if license_ is not UNSET:
            field_dict["license"] = license_
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if tags is not UNSET:
            field_dict["tags"] = tags
        if description is not UNSET:
            field_dict["description"] = description
        if cover_data is not UNSET:
            field_dict["cover_data"] = cover_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        album = d.pop("album")

        artists = d.pop("artists")

        title = d.pop("title", UNSET)

        position = d.pop("position", UNSET)

        disc_number = d.pop("disc_number", UNSET)

        copyright_ = d.pop("copyright", UNSET)

        license_ = d.pop("license", UNSET)

        mbid = d.pop("mbid", UNSET)

        tags = d.pop("tags", UNSET)

        description = d.pop("description", UNSET)

        cover_data = d.pop("cover_data", UNSET)

        track_metadata = cls(
            album=album,
            artists=artists,
            title=title,
            position=position,
            disc_number=disc_number,
            copyright_=copyright_,
            license_=license_,
            mbid=mbid,
            tags=tags,
            description=description,
            cover_data=cover_data,
        )

        track_metadata.additional_properties = d
        return track_metadata

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
