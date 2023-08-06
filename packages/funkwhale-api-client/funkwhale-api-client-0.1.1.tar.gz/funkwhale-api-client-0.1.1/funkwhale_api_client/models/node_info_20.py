from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.metadata import Metadata
from ..models.services import Services
from ..models.software import Software
from ..models.usage import Usage
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeInfo20")


@attr.s(auto_attribs=True)
class NodeInfo20:
    """
    Attributes:
        version (str):
        software (Software):
        protocols (List[Any]):
        open_registrations (bool):
        usage (Usage):
        metadata (Metadata):
        services (Union[Unset, Services]):
    """

    version: str
    software: Software
    protocols: List[Any]
    open_registrations: bool
    usage: Usage
    metadata: Metadata
    services: Union[Unset, Services] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        software = self.software.to_dict()

        protocols = self.protocols

        open_registrations = self.open_registrations
        usage = self.usage.to_dict()

        metadata = self.metadata.to_dict()

        services: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.services, Unset):
            services = self.services.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "software": software,
                "protocols": protocols,
                "openRegistrations": open_registrations,
                "usage": usage,
                "metadata": metadata,
            }
        )
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version")

        software = Software.from_dict(d.pop("software"))

        protocols = cast(List[Any], d.pop("protocols"))

        open_registrations = d.pop("openRegistrations")

        usage = Usage.from_dict(d.pop("usage"))

        metadata = Metadata.from_dict(d.pop("metadata"))

        _services = d.pop("services", UNSET)
        services: Union[Unset, Services]
        if isinstance(_services, Unset):
            services = UNSET
        else:
            services = Services.from_dict(_services)

        node_info_20 = cls(
            version=version,
            software=software,
            protocols=protocols,
            open_registrations=open_registrations,
            usage=usage,
            metadata=metadata,
            services=services,
        )

        node_info_20.additional_properties = d
        return node_info_20

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
