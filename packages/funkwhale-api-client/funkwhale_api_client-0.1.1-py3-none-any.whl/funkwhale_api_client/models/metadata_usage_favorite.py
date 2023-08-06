from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.total_count import TotalCount

T = TypeVar("T", bound="MetadataUsageFavorite")


@attr.s(auto_attribs=True)
class MetadataUsageFavorite:
    """
    Attributes:
        tracks (TotalCount):
    """

    tracks: TotalCount
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tracks = self.tracks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tracks": tracks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tracks = TotalCount.from_dict(d.pop("tracks"))

        metadata_usage_favorite = cls(
            tracks=tracks,
        )

        metadata_usage_favorite.additional_properties = d
        return metadata_usage_favorite

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
