from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.data_page_resource_schema import DataPageResourceSchema
from ...models.gathering_skill import GatheringSkill
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    skill: Union[Unset, GatheringSkill] = UNSET,
    drop: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["min_level"] = min_level

    params["max_level"] = max_level

    json_skill: Union[Unset, str] = UNSET
    if not isinstance(skill, Unset):
        json_skill = skill.value

    params["skill"] = json_skill

    params["drop"] = drop

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/resources",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DataPageResourceSchema]:
    if response.status_code == 200:
        response_200 = DataPageResourceSchema.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DataPageResourceSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    skill: Union[Unset, GatheringSkill] = UNSET,
    drop: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageResourceSchema]:
    """ Get All Resources

     Fetch resources details.

    Args:
        min_level (Union[Unset, int]): Skill minimum level.
        max_level (Union[Unset, int]): Skill maximum level.
        skill (Union[Unset, GatheringSkill]):
        drop (Union[Unset, str]): Item code of the drop.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageResourceSchema]
     """


    kwargs = _get_kwargs(
        min_level=min_level,
max_level=max_level,
skill=skill,
drop=drop,
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
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    skill: Union[Unset, GatheringSkill] = UNSET,
    drop: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageResourceSchema]:
    """ Get All Resources

     Fetch resources details.

    Args:
        min_level (Union[Unset, int]): Skill minimum level.
        max_level (Union[Unset, int]): Skill maximum level.
        skill (Union[Unset, GatheringSkill]):
        drop (Union[Unset, str]): Item code of the drop.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageResourceSchema
     """


    return sync_detailed(
        client=client,
min_level=min_level,
max_level=max_level,
skill=skill,
drop=drop,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    skill: Union[Unset, GatheringSkill] = UNSET,
    drop: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageResourceSchema]:
    """ Get All Resources

     Fetch resources details.

    Args:
        min_level (Union[Unset, int]): Skill minimum level.
        max_level (Union[Unset, int]): Skill maximum level.
        skill (Union[Unset, GatheringSkill]):
        drop (Union[Unset, str]): Item code of the drop.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageResourceSchema]
     """


    kwargs = _get_kwargs(
        min_level=min_level,
max_level=max_level,
skill=skill,
drop=drop,
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
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    skill: Union[Unset, GatheringSkill] = UNSET,
    drop: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageResourceSchema]:
    """ Get All Resources

     Fetch resources details.

    Args:
        min_level (Union[Unset, int]): Skill minimum level.
        max_level (Union[Unset, int]): Skill maximum level.
        skill (Union[Unset, GatheringSkill]):
        drop (Union[Unset, str]): Item code of the drop.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageResourceSchema
     """


    return (await asyncio_detailed(
        client=client,
min_level=min_level,
max_level=max_level,
skill=skill,
drop=drop,
page=page,
size=size,

    )).parsed
