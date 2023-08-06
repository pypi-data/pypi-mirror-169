from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ReportType")


@attr.s(auto_attribs=True)
class ReportType:
    """
    Attributes:
        type (str):
        label (str):
        anonymous (bool):
    """

    type: str
    label: str
    anonymous: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        label = self.label
        anonymous = self.anonymous

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "label": label,
                "anonymous": anonymous,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        label = d.pop("label")

        anonymous = d.pop("anonymous")

        report_type = cls(
            type=type,
            label=label,
            anonymous=anonymous,
        )

        report_type.additional_properties = d
        return report_type

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
