from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GlobalPreference")


@attr.s(auto_attribs=True)
class GlobalPreference:
    """
    Attributes:
        section (str):
        name (str):
        identifier (str):
        default (str):
        value (str):
        verbose_name (str):
        help_text (str):
        additional_data (str):
        field (str):
    """

    section: str
    name: str
    identifier: str
    default: str
    value: str
    verbose_name: str
    help_text: str
    additional_data: str
    field: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        section = self.section
        name = self.name
        identifier = self.identifier
        default = self.default
        value = self.value
        verbose_name = self.verbose_name
        help_text = self.help_text
        additional_data = self.additional_data
        field = self.field

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "section": section,
                "name": name,
                "identifier": identifier,
                "default": default,
                "value": value,
                "verbose_name": verbose_name,
                "help_text": help_text,
                "additional_data": additional_data,
                "field": field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        section = d.pop("section")

        name = d.pop("name")

        identifier = d.pop("identifier")

        default = d.pop("default")

        value = d.pop("value")

        verbose_name = d.pop("verbose_name")

        help_text = d.pop("help_text")

        additional_data = d.pop("additional_data")

        field = d.pop("field")

        global_preference = cls(
            section=section,
            name=name,
            identifier=identifier,
            default=default,
            value=value,
            verbose_name=verbose_name,
            help_text=help_text,
            additional_data=additional_data,
            field=field,
        )

        global_preference.additional_properties = d
        return global_preference

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
