from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FetchRequest")


@attr.s(auto_attribs=True)
class FetchRequest:
    """
    Attributes:
        object_ (str):
        force (Union[Unset, bool]):
    """

    object_: str
    force: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_
        force = self.force

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
            }
        )
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        object_ = self.object_ if isinstance(self.object_, Unset) else (None, str(self.object_).encode(), "text/plain")
        force = self.force if isinstance(self.force, Unset) else (None, str(self.force).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "object": object_,
            }
        )
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = d.pop("object")

        force = d.pop("force", UNSET)

        fetch_request = cls(
            object_=object_,
            force=force,
        )

        fetch_request.additional_properties = d
        return fetch_request

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
