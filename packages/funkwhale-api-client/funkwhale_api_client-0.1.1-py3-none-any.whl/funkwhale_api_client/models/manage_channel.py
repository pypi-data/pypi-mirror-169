import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.manage_artist import ManageArtist
from ..models.manage_base_actor import ManageBaseActor
from ..models.manage_channel_metadata import ManageChannelMetadata

T = TypeVar("T", bound="ManageChannel")


@attr.s(auto_attribs=True)
class ManageChannel:
    """
    Attributes:
        id (int):
        uuid (str):
        creation_date (datetime.datetime):
        artist (ManageArtist):
        attributed_to (ManageBaseActor):
        actor (ManageBaseActor):
        metadata (ManageChannelMetadata):
        rss_url (Optional[str]):
    """

    id: int
    uuid: str
    creation_date: datetime.datetime
    artist: ManageArtist
    attributed_to: ManageBaseActor
    actor: ManageBaseActor
    metadata: ManageChannelMetadata
    rss_url: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        uuid = self.uuid
        creation_date = self.creation_date.isoformat()

        artist = self.artist.to_dict()

        attributed_to = self.attributed_to.to_dict()

        actor = self.actor.to_dict()

        metadata = self.metadata.to_dict()

        rss_url = self.rss_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "creation_date": creation_date,
                "artist": artist,
                "attributed_to": attributed_to,
                "actor": actor,
                "metadata": metadata,
                "rss_url": rss_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        uuid = d.pop("uuid")

        creation_date = isoparse(d.pop("creation_date"))

        artist = ManageArtist.from_dict(d.pop("artist"))

        attributed_to = ManageBaseActor.from_dict(d.pop("attributed_to"))

        actor = ManageBaseActor.from_dict(d.pop("actor"))

        metadata = ManageChannelMetadata.from_dict(d.pop("metadata"))

        rss_url = d.pop("rss_url")

        manage_channel = cls(
            id=id,
            uuid=uuid,
            creation_date=creation_date,
            artist=artist,
            attributed_to=attributed_to,
            actor=actor,
            metadata=metadata,
            rss_url=rss_url,
        )

        manage_channel.additional_properties = d
        return manage_channel

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
