import json
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.manage_note_request_target import ManageNoteRequestTarget
from ..types import Unset

T = TypeVar("T", bound="ManageNoteRequest")


@attr.s(auto_attribs=True)
class ManageNoteRequest:
    """
    Attributes:
        summary (str):
        target (ManageNoteRequestTarget):
    """

    summary: str
    target: ManageNoteRequestTarget
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        summary = self.summary
        target = self.target.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
                "target": target,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        summary = self.summary if isinstance(self.summary, Unset) else (None, str(self.summary).encode(), "text/plain")
        target = (None, json.dumps(self.target.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "summary": summary,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        summary = d.pop("summary")

        target = ManageNoteRequestTarget.from_dict(d.pop("target"))

        manage_note_request = cls(
            summary=summary,
            target=target,
        )

        manage_note_request.additional_properties = d
        return manage_note_request

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
