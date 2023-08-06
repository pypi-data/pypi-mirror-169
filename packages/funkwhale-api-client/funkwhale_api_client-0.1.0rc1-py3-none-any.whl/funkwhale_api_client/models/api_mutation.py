import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor
from ..models.api_mutation_payload import APIMutationPayload
from ..models.api_mutation_previous_state import APIMutationPreviousState
from ..models.api_mutation_target import APIMutationTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="APIMutation")


@attr.s(auto_attribs=True)
class APIMutation:
    """
    Attributes:
        fid (str):
        uuid (str):
        type (str):
        creation_date (datetime.datetime):
        created_by (APIActor):
        payload (APIMutationPayload):
        target (APIMutationTarget):
        applied_date (Union[Unset, None, datetime.datetime]):
        is_approved (Union[Unset, None, bool]):
        is_applied (Optional[bool]):
        approved_by (Optional[int]):
        summary (Union[Unset, None, str]):
        previous_state (Optional[APIMutationPreviousState]):
    """

    fid: str
    uuid: str
    type: str
    creation_date: datetime.datetime
    created_by: APIActor
    payload: APIMutationPayload
    target: APIMutationTarget
    is_applied: Optional[bool]
    approved_by: Optional[int]
    previous_state: Optional[APIMutationPreviousState]
    applied_date: Union[Unset, None, datetime.datetime] = UNSET
    is_approved: Union[Unset, None, bool] = UNSET
    summary: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fid = self.fid
        uuid = self.uuid
        type = self.type
        creation_date = self.creation_date.isoformat()

        created_by = self.created_by.to_dict()

        payload = self.payload.to_dict()

        target = self.target.to_dict()

        applied_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.applied_date, Unset):
            applied_date = self.applied_date.isoformat() if self.applied_date else None

        is_approved = self.is_approved
        is_applied = self.is_applied
        approved_by = self.approved_by
        summary = self.summary
        previous_state = self.previous_state.to_dict() if self.previous_state else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fid": fid,
                "uuid": uuid,
                "type": type,
                "creation_date": creation_date,
                "created_by": created_by,
                "payload": payload,
                "target": target,
                "is_applied": is_applied,
                "approved_by": approved_by,
                "previous_state": previous_state,
            }
        )
        if applied_date is not UNSET:
            field_dict["applied_date"] = applied_date
        if is_approved is not UNSET:
            field_dict["is_approved"] = is_approved
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fid = d.pop("fid")

        uuid = d.pop("uuid")

        type = d.pop("type")

        creation_date = isoparse(d.pop("creation_date"))

        created_by = APIActor.from_dict(d.pop("created_by"))

        payload = APIMutationPayload.from_dict(d.pop("payload"))

        target = APIMutationTarget.from_dict(d.pop("target"))

        _applied_date = d.pop("applied_date", UNSET)
        applied_date: Union[Unset, None, datetime.datetime]
        if _applied_date is None:
            applied_date = None
        elif isinstance(_applied_date, Unset):
            applied_date = UNSET
        else:
            applied_date = isoparse(_applied_date)

        is_approved = d.pop("is_approved", UNSET)

        is_applied = d.pop("is_applied")

        approved_by = d.pop("approved_by")

        summary = d.pop("summary", UNSET)

        _previous_state = d.pop("previous_state")
        previous_state: Optional[APIMutationPreviousState]
        if _previous_state is None:
            previous_state = None
        else:
            previous_state = APIMutationPreviousState.from_dict(_previous_state)

        api_mutation = cls(
            fid=fid,
            uuid=uuid,
            type=type,
            creation_date=creation_date,
            created_by=created_by,
            payload=payload,
            target=target,
            applied_date=applied_date,
            is_approved=is_approved,
            is_applied=is_applied,
            approved_by=approved_by,
            summary=summary,
            previous_state=previous_state,
        )

        api_mutation.additional_properties = d
        return api_mutation

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
