from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_status import AccountStatus
from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="AccountDetails")



@_attrs_define
class AccountDetails:
    """ 
        Attributes:
            username (str): Username.
            member (bool): Member status.
            status (AccountStatus):
            skins (list[Any]): Skins owned.
            achievements_points (int): Achievement points.
            banned (bool): Banned.
            badges (Union[Unset, list[Any]]): Account badges.
            ban_reason (Union[Unset, str]): Ban reason.
     """

    username: str
    member: bool
    status: AccountStatus
    skins: list[Any]
    achievements_points: int
    banned: bool
    badges: Union[Unset, list[Any]] = UNSET
    ban_reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        username = self.username

        member = self.member

        status = self.status.value

        skins = self.skins



        achievements_points = self.achievements_points

        banned = self.banned

        badges: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.badges, Unset):
            badges = self.badges



        ban_reason = self.ban_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "username": username,
            "member": member,
            "status": status,
            "skins": skins,
            "achievements_points": achievements_points,
            "banned": banned,
        })
        if badges is not UNSET:
            field_dict["badges"] = badges
        if ban_reason is not UNSET:
            field_dict["ban_reason"] = ban_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        member = d.pop("member")

        status = AccountStatus(d.pop("status"))




        skins = cast(list[Any], d.pop("skins"))


        achievements_points = d.pop("achievements_points")

        banned = d.pop("banned")

        badges = cast(list[Any], d.pop("badges", UNSET))


        ban_reason = d.pop("ban_reason", UNSET)

        account_details = cls(
            username=username,
            member=member,
            status=status,
            skins=skins,
            achievements_points=achievements_points,
            banned=banned,
            badges=badges,
            ban_reason=ban_reason,
        )


        account_details.additional_properties = d
        return account_details

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
