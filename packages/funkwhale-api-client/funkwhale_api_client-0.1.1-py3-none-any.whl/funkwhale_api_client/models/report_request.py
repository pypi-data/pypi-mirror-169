import json
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.report_request_target import ReportRequestTarget
from ..models.report_type_enum import ReportTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportRequest")


@attr.s(auto_attribs=True)
class ReportRequest:
    """
    Attributes:
        target (ReportRequestTarget):
        type (ReportTypeEnum):
        summary (Union[Unset, None, str]):
        submitter_email (Union[Unset, None, str]):
    """

    target: ReportRequestTarget
    type: ReportTypeEnum
    summary: Union[Unset, None, str] = UNSET
    submitter_email: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target = self.target.to_dict()

        type = self.type.value

        summary = self.summary
        submitter_email = self.submitter_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target": target,
                "type": type,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary
        if submitter_email is not UNSET:
            field_dict["submitter_email"] = submitter_email

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        target = (None, json.dumps(self.target.to_dict()).encode(), "application/json")

        type = (None, str(self.type.value).encode(), "text/plain")

        summary = self.summary if isinstance(self.summary, Unset) else (None, str(self.summary).encode(), "text/plain")
        submitter_email = (
            self.submitter_email
            if isinstance(self.submitter_email, Unset)
            else (None, str(self.submitter_email).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "target": target,
                "type": type,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary
        if submitter_email is not UNSET:
            field_dict["submitter_email"] = submitter_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target = ReportRequestTarget.from_dict(d.pop("target"))

        type = ReportTypeEnum(d.pop("type"))

        summary = d.pop("summary", UNSET)

        submitter_email = d.pop("submitter_email", UNSET)

        report_request = cls(
            target=target,
            type=type,
            summary=summary,
            submitter_email=submitter_email,
        )

        report_request.additional_properties = d
        return report_request

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
