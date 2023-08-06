from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="InlineSubscription")


@attr.s(auto_attribs=True)
class InlineSubscription:
    """
    Attributes:
        uuid (str):
        channel (str):
    """

    uuid: str
    channel: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        channel = self.channel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "channel": channel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        channel = d.pop("channel")

        inline_subscription = cls(
            uuid=uuid,
            channel=channel,
        )

        inline_subscription.additional_properties = d
        return inline_subscription

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
