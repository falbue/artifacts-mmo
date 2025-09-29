from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_status import AccountStatus






T = TypeVar("T", bound="AccountLeaderboardSchema")



@_attrs_define
class AccountLeaderboardSchema:
    """ 
        Attributes:
            position (int): Position in the leaderboard.
            account (str): Account name.
            status (AccountStatus):
            achievements_points (int): Achievements points.
            gold (int): Gold in the account.
     """

    position: int
    account: str
    status: AccountStatus
    achievements_points: int
    gold: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        position = self.position

        account = self.account

        status = self.status.value

        achievements_points = self.achievements_points

        gold = self.gold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "position": position,
            "account": account,
            "status": status,
            "achievements_points": achievements_points,
            "gold": gold,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position")

        account = d.pop("account")

        status = AccountStatus(d.pop("status"))




        achievements_points = d.pop("achievements_points")

        gold = d.pop("gold")

        account_leaderboard_schema = cls(
            position=position,
            account=account,
            status=status,
            achievements_points=achievements_points,
            gold=gold,
        )


        account_leaderboard_schema.additional_properties = d
        return account_leaderboard_schema

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
