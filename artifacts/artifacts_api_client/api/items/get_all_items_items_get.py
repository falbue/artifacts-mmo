from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.craft_skill import CraftSkill
from ...models.data_page_item_schema import DataPageItemSchema
from ...models.item_type import ItemType
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    name: Union[Unset, str] = UNSET,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    type_: Union[Unset, ItemType] = UNSET,
    craft_skill: Union[Unset, CraftSkill] = UNSET,
    craft_material: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["name"] = name

    params["min_level"] = min_level

    params["max_level"] = max_level

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_craft_skill: Union[Unset, str] = UNSET
    if not isinstance(craft_skill, Unset):
        json_craft_skill = craft_skill.value

    params["craft_skill"] = json_craft_skill

    params["craft_material"] = craft_material

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/items",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DataPageItemSchema]:
    if response.status_code == 200:
        response_200 = DataPageItemSchema.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DataPageItemSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[Unset, str] = UNSET,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    type_: Union[Unset, ItemType] = UNSET,
    craft_skill: Union[Unset, CraftSkill] = UNSET,
    craft_material: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageItemSchema]:
    """ Get All Items

     Fetch items details.

    Args:
        name (Union[Unset, str]): Name of the item.
        min_level (Union[Unset, int]): Minimum level items.
        max_level (Union[Unset, int]): Maximum level items.
        type_ (Union[Unset, ItemType]):
        craft_skill (Union[Unset, CraftSkill]):
        craft_material (Union[Unset, str]): Item code of items used as material for crafting.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageItemSchema]
     """


    kwargs = _get_kwargs(
        name=name,
min_level=min_level,
max_level=max_level,
type_=type_,
craft_skill=craft_skill,
craft_material=craft_material,
page=page,
size=size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[Unset, str] = UNSET,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    type_: Union[Unset, ItemType] = UNSET,
    craft_skill: Union[Unset, CraftSkill] = UNSET,
    craft_material: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageItemSchema]:
    """ Get All Items

     Fetch items details.

    Args:
        name (Union[Unset, str]): Name of the item.
        min_level (Union[Unset, int]): Minimum level items.
        max_level (Union[Unset, int]): Maximum level items.
        type_ (Union[Unset, ItemType]):
        craft_skill (Union[Unset, CraftSkill]):
        craft_material (Union[Unset, str]): Item code of items used as material for crafting.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageItemSchema
     """


    return sync_detailed(
        client=client,
name=name,
min_level=min_level,
max_level=max_level,
type_=type_,
craft_skill=craft_skill,
craft_material=craft_material,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[Unset, str] = UNSET,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    type_: Union[Unset, ItemType] = UNSET,
    craft_skill: Union[Unset, CraftSkill] = UNSET,
    craft_material: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageItemSchema]:
    """ Get All Items

     Fetch items details.

    Args:
        name (Union[Unset, str]): Name of the item.
        min_level (Union[Unset, int]): Minimum level items.
        max_level (Union[Unset, int]): Maximum level items.
        type_ (Union[Unset, ItemType]):
        craft_skill (Union[Unset, CraftSkill]):
        craft_material (Union[Unset, str]): Item code of items used as material for crafting.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageItemSchema]
     """


    kwargs = _get_kwargs(
        name=name,
min_level=min_level,
max_level=max_level,
type_=type_,
craft_skill=craft_skill,
craft_material=craft_material,
page=page,
size=size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[Unset, str] = UNSET,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    type_: Union[Unset, ItemType] = UNSET,
    craft_skill: Union[Unset, CraftSkill] = UNSET,
    craft_material: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageItemSchema]:
    """ Get All Items

     Fetch items details.

    Args:
        name (Union[Unset, str]): Name of the item.
        min_level (Union[Unset, int]): Minimum level items.
        max_level (Union[Unset, int]): Maximum level items.
        type_ (Union[Unset, ItemType]):
        craft_skill (Union[Unset, CraftSkill]):
        craft_material (Union[Unset, str]): Item code of items used as material for crafting.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageItemSchema
     """


    return (await asyncio_detailed(
        client=client,
name=name,
min_level=min_level,
max_level=max_level,
type_=type_,
craft_skill=craft_skill,
craft_material=craft_material,
page=page,
size=size,

    )).parsed
