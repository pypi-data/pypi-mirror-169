from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.allow_list_stat import AllowListStat
from ..models.endpoints import Endpoints
from ..models.metadata_usage import MetadataUsage
from ..models.report_type import ReportType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Metadata")


@attr.s(auto_attribs=True)
class Metadata:
    """
    Attributes:
        actor_id (str):
        private (bool):
        short_description (str):
        long_description (str):
        rules (str):
        contact_email (str):
        terms (str):
        node_name (str):
        banner (str):
        default_upload_quota (int):
        library (bool):
        supported_upload_extensions (List[str]):
        allow_list (AllowListStat):
        report_types (List[ReportType]):
        funkwhale_support_message_enabled (bool):
        instance_support_message (str):
        endpoints (Endpoints):
        usage (Union[Unset, MetadataUsage]):
    """

    actor_id: str
    private: bool
    short_description: str
    long_description: str
    rules: str
    contact_email: str
    terms: str
    node_name: str
    banner: str
    default_upload_quota: int
    library: bool
    supported_upload_extensions: List[str]
    allow_list: AllowListStat
    report_types: List[ReportType]
    funkwhale_support_message_enabled: bool
    instance_support_message: str
    endpoints: Endpoints
    usage: Union[Unset, MetadataUsage] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actor_id = self.actor_id
        private = self.private
        short_description = self.short_description
        long_description = self.long_description
        rules = self.rules
        contact_email = self.contact_email
        terms = self.terms
        node_name = self.node_name
        banner = self.banner
        default_upload_quota = self.default_upload_quota
        library = self.library
        supported_upload_extensions = self.supported_upload_extensions

        allow_list = self.allow_list.to_dict()

        report_types = []
        for report_types_item_data in self.report_types:
            report_types_item = report_types_item_data.to_dict()

            report_types.append(report_types_item)

        funkwhale_support_message_enabled = self.funkwhale_support_message_enabled
        instance_support_message = self.instance_support_message
        endpoints = self.endpoints.to_dict()

        usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actorId": actor_id,
                "private": private,
                "shortDescription": short_description,
                "longDescription": long_description,
                "rules": rules,
                "contactEmail": contact_email,
                "terms": terms,
                "nodeName": node_name,
                "banner": banner,
                "defaultUploadQuota": default_upload_quota,
                "library": library,
                "supportedUploadExtensions": supported_upload_extensions,
                "allowList": allow_list,
                "reportTypes": report_types,
                "funkwhaleSupportMessageEnabled": funkwhale_support_message_enabled,
                "instanceSupportMessage": instance_support_message,
                "endpoints": endpoints,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        actor_id = d.pop("actorId")

        private = d.pop("private")

        short_description = d.pop("shortDescription")

        long_description = d.pop("longDescription")

        rules = d.pop("rules")

        contact_email = d.pop("contactEmail")

        terms = d.pop("terms")

        node_name = d.pop("nodeName")

        banner = d.pop("banner")

        default_upload_quota = d.pop("defaultUploadQuota")

        library = d.pop("library")

        supported_upload_extensions = cast(List[str], d.pop("supportedUploadExtensions"))

        allow_list = AllowListStat.from_dict(d.pop("allowList"))

        report_types = []
        _report_types = d.pop("reportTypes")
        for report_types_item_data in _report_types:
            report_types_item = ReportType.from_dict(report_types_item_data)

            report_types.append(report_types_item)

        funkwhale_support_message_enabled = d.pop("funkwhaleSupportMessageEnabled")

        instance_support_message = d.pop("instanceSupportMessage")

        endpoints = Endpoints.from_dict(d.pop("endpoints"))

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, MetadataUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = MetadataUsage.from_dict(_usage)

        metadata = cls(
            actor_id=actor_id,
            private=private,
            short_description=short_description,
            long_description=long_description,
            rules=rules,
            contact_email=contact_email,
            terms=terms,
            node_name=node_name,
            banner=banner,
            default_upload_quota=default_upload_quota,
            library=library,
            supported_upload_extensions=supported_upload_extensions,
            allow_list=allow_list,
            report_types=report_types,
            funkwhale_support_message_enabled=funkwhale_support_message_enabled,
            instance_support_message=instance_support_message,
            endpoints=endpoints,
            usage=usage,
        )

        metadata.additional_properties = d
        return metadata

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
