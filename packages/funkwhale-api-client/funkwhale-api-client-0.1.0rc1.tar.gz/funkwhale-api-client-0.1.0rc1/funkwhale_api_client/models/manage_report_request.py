import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.manage_base_actor_request import ManageBaseActorRequest
from ..models.manage_base_note_request import ManageBaseNoteRequest
from ..models.manage_report_request_target import ManageReportRequestTarget
from ..models.report_type_enum import ReportTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageReportRequest")


@attr.s(auto_attribs=True)
class ManageReportRequest:
    """
    Attributes:
        type (ReportTypeEnum):
        target (ManageReportRequestTarget):
        is_handled (Union[Unset, bool]):
        assigned_to (Union[Unset, None, ManageBaseActorRequest]):
        target_owner (Union[Unset, ManageBaseActorRequest]):
        submitter (Union[Unset, ManageBaseActorRequest]):
        notes (Union[Unset, None, List[ManageBaseNoteRequest]]):
    """

    type: ReportTypeEnum
    target: ManageReportRequestTarget
    is_handled: Union[Unset, bool] = UNSET
    assigned_to: Union[Unset, None, ManageBaseActorRequest] = UNSET
    target_owner: Union[Unset, ManageBaseActorRequest] = UNSET
    submitter: Union[Unset, ManageBaseActorRequest] = UNSET
    notes: Union[Unset, None, List[ManageBaseNoteRequest]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        target = self.target.to_dict()

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
                "type": type,
                "target": target,
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

    def to_multipart(self) -> Dict[str, Any]:
        type = (None, str(self.type.value).encode(), "text/plain")

        target = (None, json.dumps(self.target.to_dict()).encode(), "application/json")

        is_handled = (
            self.is_handled
            if isinstance(self.is_handled, Unset)
            else (None, str(self.is_handled).encode(), "text/plain")
        )
        assigned_to: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.assigned_to, Unset):
            assigned_to = (
                (None, json.dumps(self.assigned_to.to_dict()).encode(), "application/json")
                if self.assigned_to
                else None
            )

        target_owner: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.target_owner, Unset):
            target_owner = (None, json.dumps(self.target_owner.to_dict()).encode(), "application/json")

        submitter: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.submitter, Unset):
            submitter = (None, json.dumps(self.submitter.to_dict()).encode(), "application/json")

        notes: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.notes, Unset):
            if self.notes is None:
                notes = None
            else:
                _temp_notes = []
                for notes_item_data in self.notes:
                    notes_item = notes_item_data.to_dict()

                    _temp_notes.append(notes_item)
                notes = (None, json.dumps(_temp_notes).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "type": type,
                "target": target,
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
        type = ReportTypeEnum(d.pop("type"))

        target = ManageReportRequestTarget.from_dict(d.pop("target"))

        is_handled = d.pop("is_handled", UNSET)

        _assigned_to = d.pop("assigned_to", UNSET)
        assigned_to: Union[Unset, None, ManageBaseActorRequest]
        if _assigned_to is None:
            assigned_to = None
        elif isinstance(_assigned_to, Unset):
            assigned_to = UNSET
        else:
            assigned_to = ManageBaseActorRequest.from_dict(_assigned_to)

        _target_owner = d.pop("target_owner", UNSET)
        target_owner: Union[Unset, ManageBaseActorRequest]
        if isinstance(_target_owner, Unset):
            target_owner = UNSET
        else:
            target_owner = ManageBaseActorRequest.from_dict(_target_owner)

        _submitter = d.pop("submitter", UNSET)
        submitter: Union[Unset, ManageBaseActorRequest]
        if isinstance(_submitter, Unset):
            submitter = UNSET
        else:
            submitter = ManageBaseActorRequest.from_dict(_submitter)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = ManageBaseNoteRequest.from_dict(notes_item_data)

            notes.append(notes_item)

        manage_report_request = cls(
            type=type,
            target=target,
            is_handled=is_handled,
            assigned_to=assigned_to,
            target_owner=target_owner,
            submitter=submitter,
            notes=notes,
        )

        manage_report_request.additional_properties = d
        return manage_report_request

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
