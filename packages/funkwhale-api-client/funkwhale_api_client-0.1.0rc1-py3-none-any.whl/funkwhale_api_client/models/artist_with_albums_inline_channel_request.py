from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.inline_actor_request import InlineActorRequest

T = TypeVar("T", bound="ArtistWithAlbumsInlineChannelRequest")


@attr.s(auto_attribs=True)
class ArtistWithAlbumsInlineChannelRequest:
    """
    Attributes:
        uuid (str):
        actor (InlineActorRequest):
    """

    uuid: str
    actor: InlineActorRequest
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        actor = self.actor.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "actor": actor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        actor = InlineActorRequest.from_dict(d.pop("actor"))

        artist_with_albums_inline_channel_request = cls(
            uuid=uuid,
            actor=actor,
        )

        artist_with_albums_inline_channel_request.additional_properties = d
        return artist_with_albums_inline_channel_request

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
