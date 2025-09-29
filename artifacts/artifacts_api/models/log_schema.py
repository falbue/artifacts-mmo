from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.log_type import LogType
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
import datetime






T = TypeVar("T", bound="LogSchema")



@_attrs_define
class LogSchema:
    """ 
        Attributes:
            character (str): Character name.
            account (str): Account character.
            type_ (LogType):
            description (str): Description of action.
            content (Any): Content of action.
            cooldown (int): Cooldown in seconds.
            cooldown_expiration (Union[None, datetime.datetime]): Datetime of cooldown expiration.
            created_at (datetime.datetime): Datetime of creation.
     """

    character: str
    account: str
    type_: LogType
    description: str
    content: Any
    cooldown: int
    cooldown_expiration: Union[None, datetime.datetime]
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        character = self.character

        account = self.account

        type_ = self.type_.value

        description = self.description

        content = self.content

        cooldown = self.cooldown

        cooldown_expiration: Union[None, str]
        if isinstance(self.cooldown_expiration, datetime.datetime):
            cooldown_expiration = self.cooldown_expiration.isoformat()
        else:
            cooldown_expiration = self.cooldown_expiration

        created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "character": character,
            "account": account,
            "type": type_,
            "description": description,
            "content": content,
            "cooldown": cooldown,
            "cooldown_expiration": cooldown_expiration,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        character = d.pop("character")

        account = d.pop("account")

        type_ = LogType(d.pop("type"))




        description = d.pop("description")

        content = d.pop("content")

        cooldown = d.pop("cooldown")

        def _parse_cooldown_expiration(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cooldown_expiration_type_0 = isoparse(data)



                return cooldown_expiration_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        cooldown_expiration = _parse_cooldown_expiration(d.pop("cooldown_expiration"))


        created_at = isoparse(d.pop("created_at"))




        log_schema = cls(
            character=character,
            account=account,
            type_=type_,
            description=description,
            content=content,
            cooldown=cooldown,
            cooldown_expiration=cooldown_expiration,
            created_at=created_at,
        )


        log_schema.additional_properties = d
        return log_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
