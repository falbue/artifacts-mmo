from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.task_type import TaskType
from typing import cast

if TYPE_CHECKING:
  from ..models.rewards_schema import RewardsSchema





T = TypeVar("T", bound="TaskSchema")



@_attrs_define
class TaskSchema:
    """ 
        Attributes:
            code (str): Task objective.
            type_ (TaskType):
            total (int): The total required to complete the task.
            rewards (RewardsSchema):
     """

    code: str
    type_: TaskType
    total: int
    rewards: 'RewardsSchema'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rewards_schema import RewardsSchema
        code = self.code

        type_ = self.type_.value

        total = self.total

        rewards = self.rewards.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "type": type_,
            "total": total,
            "rewards": rewards,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rewards_schema import RewardsSchema
        d = dict(src_dict)
        code = d.pop("code")

        type_ = TaskType(d.pop("type"))




        total = d.pop("total")

        rewards = RewardsSchema.from_dict(d.pop("rewards"))




        task_schema = cls(
            code=code,
            type_=type_,
            total=total,
            rewards=rewards,
        )


        task_schema.additional_properties = d
        return task_schema

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
