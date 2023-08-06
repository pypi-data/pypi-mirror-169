from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="License")


@attr.s(auto_attribs=True)
class License:
    """
    Attributes:
        id (str):
        url (str):
        code (str):
        name (str):
        redistribute (bool):
        derivative (bool):
        commercial (bool):
        attribution (bool):
        copyleft (bool):
    """

    id: str
    url: str
    code: str
    name: str
    redistribute: bool
    derivative: bool
    commercial: bool
    attribution: bool
    copyleft: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        code = self.code
        name = self.name
        redistribute = self.redistribute
        derivative = self.derivative
        commercial = self.commercial
        attribution = self.attribution
        copyleft = self.copyleft

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "code": code,
                "name": name,
                "redistribute": redistribute,
                "derivative": derivative,
                "commercial": commercial,
                "attribution": attribution,
                "copyleft": copyleft,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        code = d.pop("code")

        name = d.pop("name")

        redistribute = d.pop("redistribute")

        derivative = d.pop("derivative")

        commercial = d.pop("commercial")

        attribution = d.pop("attribution")

        copyleft = d.pop("copyleft")

        license_ = cls(
            id=id,
            url=url,
            code=code,
            name=name,
            redistribute=redistribute,
            derivative=derivative,
            commercial=commercial,
            attribution=attribution,
            copyleft=copyleft,
        )

        license_.additional_properties = d
        return license_

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
