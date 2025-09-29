from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.achievement_schema import AchievementSchema





T = TypeVar("T", bound="DataPageAchievementSchema")



@_attrs_define
class DataPageAchievementSchema:
    """ 
        Attributes:
            data (list['AchievementSchema']):
            total (Union[None, int]):
            page (Union[None, int]):
            size (Union[None, int]):
            pages (Union[None, Unset, int]):
     """

    data: list['AchievementSchema']
    total: Union[None, int]
    page: Union[None, int]
    size: Union[None, int]
    pages: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.achievement_schema import AchievementSchema
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        total: Union[None, int]
        total = self.total

        page: Union[None, int]
        page = self.page

        size: Union[None, int]
        size = self.size

        pages: Union[None, Unset, int]
        if isinstance(self.pages, Unset):
            pages = UNSET
        else:
            pages = self.pages


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
            "total": total,
            "page": page,
            "size": size,
        })
        if pages is not UNSET:
            field_dict["pages"] = pages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.achievement_schema import AchievementSchema
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = AchievementSchema.from_dict(data_item_data)



            data.append(data_item)


        def _parse_total(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        total = _parse_total(d.pop("total"))


        def _parse_page(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        page = _parse_page(d.pop("page"))


        def _parse_size(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        size = _parse_size(d.pop("size"))


        def _parse_pages(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pages = _parse_pages(d.pop("pages", UNSET))


        data_page_achievement_schema = cls(
            data=data,
            total=total,
            page=page,
            size=size,
            pages=pages,
        )


        data_page_achievement_schema.additional_properties = d
        return data_page_achievement_schema

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
