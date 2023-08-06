import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.manage_base_actor_request import ManageBaseActorRequest
from ..models.manage_user_request_status_enum import ManageUserRequestStatusEnum
from ..models.manage_user_request_type_enum import ManageUserRequestTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedManageUserRequestRequest")


@attr.s(auto_attribs=True)
class PatchedManageUserRequestRequest:
    """
    Attributes:
        type (Union[Unset, ManageUserRequestTypeEnum]):
        status (Union[Unset, ManageUserRequestStatusEnum]):
        assigned_to (Union[Unset, ManageBaseActorRequest]):
        submitter (Union[Unset, ManageBaseActorRequest]):
    """

    type: Union[Unset, ManageUserRequestTypeEnum] = UNSET
    status: Union[Unset, ManageUserRequestStatusEnum] = UNSET
    assigned_to: Union[Unset, ManageBaseActorRequest] = UNSET
    submitter: Union[Unset, ManageBaseActorRequest] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        assigned_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_to, Unset):
            assigned_to = self.assigned_to.to_dict()

        submitter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.submitter, Unset):
            submitter = self.submitter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if assigned_to is not UNSET:
            field_dict["assigned_to"] = assigned_to
        if submitter is not UNSET:
            field_dict["submitter"] = submitter

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        type: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.type, Unset):
            type = (None, str(self.type.value).encode(), "text/plain")

        status: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        assigned_to: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.assigned_to, Unset):
            assigned_to = (None, json.dumps(self.assigned_to.to_dict()).encode(), "application/json")

        submitter: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.submitter, Unset):
            submitter = (None, json.dumps(self.submitter.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if assigned_to is not UNSET:
            field_dict["assigned_to"] = assigned_to
        if submitter is not UNSET:
            field_dict["submitter"] = submitter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, ManageUserRequestTypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ManageUserRequestTypeEnum(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ManageUserRequestStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ManageUserRequestStatusEnum(_status)

        _assigned_to = d.pop("assigned_to", UNSET)
        assigned_to: Union[Unset, ManageBaseActorRequest]
        if isinstance(_assigned_to, Unset):
            assigned_to = UNSET
        else:
            assigned_to = ManageBaseActorRequest.from_dict(_assigned_to)

        _submitter = d.pop("submitter", UNSET)
        submitter: Union[Unset, ManageBaseActorRequest]
        if isinstance(_submitter, Unset):
            submitter = UNSET
        else:
            submitter = ManageBaseActorRequest.from_dict(_submitter)

        patched_manage_user_request_request = cls(
            type=type,
            status=status,
            assigned_to=assigned_to,
            submitter=submitter,
        )

        patched_manage_user_request_request.additional_properties = d
        return patched_manage_user_request_request

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
