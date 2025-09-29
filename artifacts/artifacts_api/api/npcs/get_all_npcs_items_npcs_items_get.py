from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.data_page_npc_item import DataPageNPCItem
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    code: Union[Unset, str] = UNSET,
    npc: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["code"] = code

    params["npc"] = npc

    params["currency"] = currency

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/npcs/items",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DataPageNPCItem]:
    if response.status_code == 200:
        response_200 = DataPageNPCItem.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DataPageNPCItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    code: Union[Unset, str] = UNSET,
    npc: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageNPCItem]:
    """ Get All Npcs Items

     Retrieve the list of all NPC items.

    Args:
        code (Union[Unset, str]): The code of the item.
        npc (Union[Unset, str]): The code of the npc.
        currency (Union[Unset, str]): The code of the currency.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageNPCItem]
     """


    kwargs = _get_kwargs(
        code=code,
npc=npc,
currency=currency,
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
    code: Union[Unset, str] = UNSET,
    npc: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageNPCItem]:
    """ Get All Npcs Items

     Retrieve the list of all NPC items.

    Args:
        code (Union[Unset, str]): The code of the item.
        npc (Union[Unset, str]): The code of the npc.
        currency (Union[Unset, str]): The code of the currency.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageNPCItem
     """


    return sync_detailed(
        client=client,
code=code,
npc=npc,
currency=currency,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    code: Union[Unset, str] = UNSET,
    npc: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageNPCItem]:
    """ Get All Npcs Items

     Retrieve the list of all NPC items.

    Args:
        code (Union[Unset, str]): The code of the item.
        npc (Union[Unset, str]): The code of the npc.
        currency (Union[Unset, str]): The code of the currency.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageNPCItem]
     """


    kwargs = _get_kwargs(
        code=code,
npc=npc,
currency=currency,
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
    code: Union[Unset, str] = UNSET,
    npc: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageNPCItem]:
    """ Get All Npcs Items

     Retrieve the list of all NPC items.

    Args:
        code (Union[Unset, str]): The code of the item.
        npc (Union[Unset, str]): The code of the npc.
        currency (Union[Unset, str]): The code of the currency.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageNPCItem
     """


    return (await asyncio_detailed(
        client=client,
code=code,
npc=npc,
currency=currency,
page=page,
size=size,

    )).parsed
