from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.metadata_usage_favorite import MetadataUsageFavorite
from ..models.total_count import TotalCount

T = TypeVar("T", bound="MetadataUsage")


@attr.s(auto_attribs=True)
class MetadataUsage:
    """
    Attributes:
        favorites (MetadataUsageFavorite):
        listenings (TotalCount):
        downloads (TotalCount):
    """

    favorites: MetadataUsageFavorite
    listenings: TotalCount
    downloads: TotalCount
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        favorites = self.favorites.to_dict()

        listenings = self.listenings.to_dict()

        downloads = self.downloads.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "favorites": favorites,
                "listenings": listenings,
                "downloads": downloads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        favorites = MetadataUsageFavorite.from_dict(d.pop("favorites"))

        listenings = TotalCount.from_dict(d.pop("listenings"))

        downloads = TotalCount.from_dict(d.pop("downloads"))

        metadata_usage = cls(
            favorites=favorites,
            listenings=listenings,
            downloads=downloads,
        )

        metadata_usage.additional_properties = d
        return metadata_usage

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
