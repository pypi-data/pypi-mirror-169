import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor
from ..models.channel_metadata import ChannelMetadata
from ..models.simple_artist import SimpleArtist
from ..types import UNSET, Unset

T = TypeVar("T", bound="Channel")


@attr.s(auto_attribs=True)
class Channel:
    """
    Attributes:
        artist (SimpleArtist):
        attributed_to (APIActor):
        actor (APIActor):
        rss_url (str):
        url (str):
        downloads_count (int):
        uuid (Union[Unset, str]):
        creation_date (Union[Unset, datetime.datetime]):
        metadata (Union[Unset, ChannelMetadata]):
    """

    artist: SimpleArtist
    attributed_to: APIActor
    actor: APIActor
    rss_url: str
    url: str
    downloads_count: int
    uuid: Union[Unset, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    metadata: Union[Unset, ChannelMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artist = self.artist.to_dict()

        attributed_to = self.attributed_to.to_dict()

        actor = self.actor.to_dict()

        rss_url = self.rss_url
        url = self.url
        downloads_count = self.downloads_count
        uuid = self.uuid
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "artist": artist,
                "attributed_to": attributed_to,
                "actor": actor,
                "rss_url": rss_url,
                "url": url,
                "downloads_count": downloads_count,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        artist = SimpleArtist.from_dict(d.pop("artist"))

        attributed_to = APIActor.from_dict(d.pop("attributed_to"))

        actor = APIActor.from_dict(d.pop("actor"))

        rss_url = d.pop("rss_url")

        url = d.pop("url")

        downloads_count = d.pop("downloads_count")

        uuid = d.pop("uuid", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ChannelMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ChannelMetadata.from_dict(_metadata)

        channel = cls(
            artist=artist,
            attributed_to=attributed_to,
            actor=actor,
            rss_url=rss_url,
            url=url,
            downloads_count=downloads_count,
            uuid=uuid,
            creation_date=creation_date,
            metadata=metadata,
        )

        channel.additional_properties = d
        return channel

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
