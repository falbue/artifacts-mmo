from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_status import AccountStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="MyAccountDetails")



@_attrs_define
class MyAccountDetails:
    """ 
        Attributes:
            username (str): Username.
            email (str): Email.
            member (bool): Member status.
            status (AccountStatus):
            skins (list[Any]): Skins owned.
            gems (int): Gems.
            achievements_points (int): Achievement points.
            banned (bool): Banned.
            member_expiration (Union[None, Unset, datetime.datetime]): Member expiration date.
            badges (Union[Unset, list[Any]]): Account badges.
            ban_reason (Union[Unset, str]): Ban reason.
     """

    username: str
    email: str
    member: bool
    status: AccountStatus
    skins: list[Any]
    gems: int
    achievements_points: int
    banned: bool
    member_expiration: Union[None, Unset, datetime.datetime] = UNSET
    badges: Union[Unset, list[Any]] = UNSET
    ban_reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        username = self.username

        email = self.email

        member = self.member

        status = self.status.value

        skins = self.skins



        gems = self.gems

        achievements_points = self.achievements_points

        banned = self.banned

        member_expiration: Union[None, Unset, str]
        if isinstance(self.member_expiration, Unset):
            member_expiration = UNSET
        elif isinstance(self.member_expiration, datetime.datetime):
            member_expiration = self.member_expiration.isoformat()
        else:
            member_expiration = self.member_expiration

        badges: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.badges, Unset):
            badges = self.badges



        ban_reason = self.ban_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "username": username,
            "email": email,
            "member": member,
            "status": status,
            "skins": skins,
            "gems": gems,
            "achievements_points": achievements_points,
            "banned": banned,
        })
        if member_expiration is not UNSET:
            field_dict["member_expiration"] = member_expiration
        if badges is not UNSET:
            field_dict["badges"] = badges
        if ban_reason is not UNSET:
            field_dict["ban_reason"] = ban_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        email = d.pop("email")

        member = d.pop("member")

        status = AccountStatus(d.pop("status"))




        skins = cast(list[Any], d.pop("skins"))


        gems = d.pop("gems")

        achievements_points = d.pop("achievements_points")

        banned = d.pop("banned")

        def _parse_member_expiration(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                member_expiration_type_0 = isoparse(data)



                return member_expiration_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        member_expiration = _parse_member_expiration(d.pop("member_expiration", UNSET))


        badges = cast(list[Any], d.pop("badges", UNSET))


        ban_reason = d.pop("ban_reason", UNSET)

        my_account_details = cls(
            username=username,
            email=email,
            member=member,
            status=status,
            skins=skins,
            gems=gems,
            achievements_points=achievements_points,
            banned=banned,
            member_expiration=member_expiration,
            badges=badges,
            ban_reason=ban_reason,
        )


        my_account_details.additional_properties = d
        return my_account_details

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
