import json
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaylistAddManyRequest")


@attr.s(auto_attribs=True)
class PlaylistAddManyRequest:
    """
    Attributes:
        tracks (List[int]):
        allow_duplicates (Union[Unset, bool]):
    """

    tracks: List[int]
    allow_duplicates: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tracks = self.tracks

        allow_duplicates = self.allow_duplicates

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tracks": tracks,
            }
        )
        if allow_duplicates is not UNSET:
            field_dict["allow_duplicates"] = allow_duplicates

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        _temp_tracks = self.tracks
        tracks = (None, json.dumps(_temp_tracks).encode(), "application/json")

        allow_duplicates = (
            self.allow_duplicates
            if isinstance(self.allow_duplicates, Unset)
            else (None, str(self.allow_duplicates).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "tracks": tracks,
            }
        )
        if allow_duplicates is not UNSET:
            field_dict["allow_duplicates"] = allow_duplicates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tracks = cast(List[int], d.pop("tracks"))

        allow_duplicates = d.pop("allow_duplicates", UNSET)

        playlist_add_many_request = cls(
            tracks=tracks,
            allow_duplicates=allow_duplicates,
        )

        playlist_add_many_request.additional_properties = d
        return playlist_add_many_request

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
