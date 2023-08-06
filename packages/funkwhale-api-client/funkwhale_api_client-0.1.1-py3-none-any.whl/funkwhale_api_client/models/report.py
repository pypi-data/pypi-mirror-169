import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.report_target import ReportTarget
from ..models.report_type_enum import ReportTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Report")


@attr.s(auto_attribs=True)
class Report:
    """
    Attributes:
        uuid (str):
        creation_date (datetime.datetime):
        is_handled (bool):
        target (ReportTarget):
        type (ReportTypeEnum):
        summary (Union[Unset, None, str]):
        handled_date (Optional[datetime.datetime]):
        submitter_email (Union[Unset, None, str]):
    """

    uuid: str
    creation_date: datetime.datetime
    is_handled: bool
    target: ReportTarget
    type: ReportTypeEnum
    handled_date: Optional[datetime.datetime]
    summary: Union[Unset, None, str] = UNSET
    submitter_email: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        creation_date = self.creation_date.isoformat()

        is_handled = self.is_handled
        target = self.target.to_dict()

        type = self.type.value

        summary = self.summary
        handled_date = self.handled_date.isoformat() if self.handled_date else None

        submitter_email = self.submitter_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "creation_date": creation_date,
                "is_handled": is_handled,
                "target": target,
                "type": type,
                "handled_date": handled_date,
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
        uuid = d.pop("uuid")

        creation_date = isoparse(d.pop("creation_date"))

        is_handled = d.pop("is_handled")

        target = ReportTarget.from_dict(d.pop("target"))

        type = ReportTypeEnum(d.pop("type"))

        summary = d.pop("summary", UNSET)

        _handled_date = d.pop("handled_date")
        handled_date: Optional[datetime.datetime]
        if _handled_date is None:
            handled_date = None
        else:
            handled_date = isoparse(_handled_date)

        submitter_email = d.pop("submitter_email", UNSET)

        report = cls(
            uuid=uuid,
            creation_date=creation_date,
            is_handled=is_handled,
            target=target,
            type=type,
            summary=summary,
            handled_date=handled_date,
            submitter_email=submitter_email,
        )

        report.additional_properties = d
        return report

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
