from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.action_type import ActionType
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="CooldownSchema")



@_attrs_define
class CooldownSchema:
    """ 
        Attributes:
            total_seconds (int): The total seconds of the cooldown.
            remaining_seconds (int): The remaining seconds of the cooldown.
            started_at (datetime.datetime): The start of the cooldown.
            expiration (datetime.datetime): The expiration of the cooldown.
            reason (ActionType):
     """

    total_seconds: int
    remaining_seconds: int
    started_at: datetime.datetime
    expiration: datetime.datetime
    reason: ActionType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total_seconds = self.total_seconds

        remaining_seconds = self.remaining_seconds

        started_at = self.started_at.isoformat()

        expiration = self.expiration.isoformat()

        reason = self.reason.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total_seconds": total_seconds,
            "remaining_seconds": remaining_seconds,
            "started_at": started_at,
            "expiration": expiration,
            "reason": reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_seconds = d.pop("total_seconds")

        remaining_seconds = d.pop("remaining_seconds")

        started_at = isoparse(d.pop("started_at"))




        expiration = isoparse(d.pop("expiration"))




        reason = ActionType(d.pop("reason"))




        cooldown_schema = cls(
            total_seconds=total_seconds,
            remaining_seconds=remaining_seconds,
            started_at=started_at,
            expiration=expiration,
            reason=reason,
        )


        cooldown_schema.additional_properties = d
        return cooldown_schema

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
