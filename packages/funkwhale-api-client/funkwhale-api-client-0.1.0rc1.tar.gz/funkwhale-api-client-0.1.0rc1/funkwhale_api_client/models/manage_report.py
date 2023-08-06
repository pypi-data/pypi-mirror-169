import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.manage_base_actor import ManageBaseActor
from ..models.manage_base_note import ManageBaseNote
from ..models.manage_report_target import ManageReportTarget
from ..models.manage_report_target_state import ManageReportTargetState
from ..models.report_type_enum import ReportTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageReport")


@attr.s(auto_attribs=True)
class ManageReport:
    """
    Attributes:
        id (int):
        uuid (str):
        fid (str):
        creation_date (datetime.datetime):
        type (ReportTypeEnum):
        target (ManageReportTarget):
        handled_date (Optional[datetime.datetime]):
        summary (Optional[str]):
        target_state (Optional[ManageReportTargetState]):
        is_handled (Union[Unset, bool]):
        assigned_to (Union[Unset, None, ManageBaseActor]):
        target_owner (Union[Unset, ManageBaseActor]):
        submitter (Union[Unset, ManageBaseActor]):
        submitter_email (Optional[str]):
        notes (Union[Unset, None, List[ManageBaseNote]]):
    """

    id: int
    uuid: str
    fid: str
    creation_date: datetime.datetime
    type: ReportTypeEnum
    target: ManageReportTarget
    handled_date: Optional[datetime.datetime]
    summary: Optional[str]
    target_state: Optional[ManageReportTargetState]
    submitter_email: Optional[str]
    is_handled: Union[Unset, bool] = UNSET
    assigned_to: Union[Unset, None, ManageBaseActor] = UNSET
    target_owner: Union[Unset, ManageBaseActor] = UNSET
    submitter: Union[Unset, ManageBaseActor] = UNSET
    notes: Union[Unset, None, List[ManageBaseNote]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        uuid = self.uuid
        fid = self.fid
        creation_date = self.creation_date.isoformat()

        type = self.type.value

        target = self.target.to_dict()

        handled_date = self.handled_date.isoformat() if self.handled_date else None

        summary = self.summary
        target_state = self.target_state.to_dict() if self.target_state else None

        is_handled = self.is_handled
        assigned_to: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_to, Unset):
            assigned_to = self.assigned_to.to_dict() if self.assigned_to else None

        target_owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target_owner, Unset):
            target_owner = self.target_owner.to_dict()

        submitter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.submitter, Unset):
            submitter = self.submitter.to_dict()

        submitter_email = self.submitter_email
        notes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            if self.notes is None:
                notes = None
            else:
                notes = []
                for notes_item_data in self.notes:
                    notes_item = notes_item_data.to_dict()

                    notes.append(notes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "fid": fid,
                "creation_date": creation_date,
                "type": type,
                "target": target,
                "handled_date": handled_date,
                "summary": summary,
                "target_state": target_state,
                "submitter_email": submitter_email,
            }
        )
        if is_handled is not UNSET:
            field_dict["is_handled"] = is_handled
        if assigned_to is not UNSET:
            field_dict["assigned_to"] = assigned_to
        if target_owner is not UNSET:
            field_dict["target_owner"] = target_owner
        if submitter is not UNSET:
            field_dict["submitter"] = submitter
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        uuid = d.pop("uuid")

        fid = d.pop("fid")

        creation_date = isoparse(d.pop("creation_date"))

        type = ReportTypeEnum(d.pop("type"))

        target = ManageReportTarget.from_dict(d.pop("target"))

        _handled_date = d.pop("handled_date")
        handled_date: Optional[datetime.datetime]
        if _handled_date is None:
            handled_date = None
        else:
            handled_date = isoparse(_handled_date)

        summary = d.pop("summary")

        _target_state = d.pop("target_state")
        target_state: Optional[ManageReportTargetState]
        if _target_state is None:
            target_state = None
        else:
            target_state = ManageReportTargetState.from_dict(_target_state)

        is_handled = d.pop("is_handled", UNSET)

        _assigned_to = d.pop("assigned_to", UNSET)
        assigned_to: Union[Unset, None, ManageBaseActor]
        if _assigned_to is None:
            assigned_to = None
        elif isinstance(_assigned_to, Unset):
            assigned_to = UNSET
        else:
            assigned_to = ManageBaseActor.from_dict(_assigned_to)

        _target_owner = d.pop("target_owner", UNSET)
        target_owner: Union[Unset, ManageBaseActor]
        if isinstance(_target_owner, Unset):
            target_owner = UNSET
        else:
            target_owner = ManageBaseActor.from_dict(_target_owner)

        _submitter = d.pop("submitter", UNSET)
        submitter: Union[Unset, ManageBaseActor]
        if isinstance(_submitter, Unset):
            submitter = UNSET
        else:
            submitter = ManageBaseActor.from_dict(_submitter)

        submitter_email = d.pop("submitter_email")

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = ManageBaseNote.from_dict(notes_item_data)

            notes.append(notes_item)

        manage_report = cls(
            id=id,
            uuid=uuid,
            fid=fid,
            creation_date=creation_date,
            type=type,
            target=target,
            handled_date=handled_date,
            summary=summary,
            target_state=target_state,
            is_handled=is_handled,
            assigned_to=assigned_to,
            target_owner=target_owner,
            submitter=submitter,
            submitter_email=submitter_email,
            notes=notes,
        )

        manage_report.additional_properties = d
        return manage_report

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
