import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.manage_base_actor_request import ManageBaseActorRequest
from ..models.manage_user_request_status_enum import ManageUserRequestStatusEnum
from ..models.manage_user_request_type_enum import ManageUserRequestTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageUserRequestRequest")


@attr.s(auto_attribs=True)
class ManageUserRequestRequest:
    """
    Attributes:
        type (ManageUserRequestTypeEnum):
        assigned_to (ManageBaseActorRequest):
        submitter (ManageBaseActorRequest):
        status (Union[Unset, ManageUserRequestStatusEnum]):
    """

    type: ManageUserRequestTypeEnum
    assigned_to: ManageBaseActorRequest
    submitter: ManageBaseActorRequest
    status: Union[Unset, ManageUserRequestStatusEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        assigned_to = self.assigned_to.to_dict()

        submitter = self.submitter.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "assigned_to": assigned_to,
                "submitter": submitter,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        type = (None, str(self.type.value).encode(), "text/plain")

        assigned_to = (None, json.dumps(self.assigned_to.to_dict()).encode(), "application/json")

        submitter = (None, json.dumps(self.submitter.to_dict()).encode(), "application/json")

        status: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "type": type,
                "assigned_to": assigned_to,
                "submitter": submitter,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ManageUserRequestTypeEnum(d.pop("type"))

        assigned_to = ManageBaseActorRequest.from_dict(d.pop("assigned_to"))

        submitter = ManageBaseActorRequest.from_dict(d.pop("submitter"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, ManageUserRequestStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ManageUserRequestStatusEnum(_status)

        manage_user_request_request = cls(
            type=type,
            assigned_to=assigned_to,
            submitter=submitter,
            status=status,
        )

        manage_user_request_request.additional_properties = d
        return manage_user_request_request

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
