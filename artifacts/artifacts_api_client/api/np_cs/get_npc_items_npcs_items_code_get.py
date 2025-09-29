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
    code: str,
    *,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/npcs/items/{code}".format(code=code,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, DataPageNPCItem]]:
    if response.status_code == 200:
        response_200 = DataPageNPCItem.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, DataPageNPCItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[Union[Any, DataPageNPCItem]]:
    """ Get Npc Items

     Retrieve the items list of a NPC. If the NPC has items to buy, sell or trade, they will be
    displayed.

    Args:
        code (str): The code of the NPC.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataPageNPCItem]]
     """


    kwargs = _get_kwargs(
        code=code,
page=page,
size=size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[Union[Any, DataPageNPCItem]]:
    """ Get Npc Items

     Retrieve the items list of a NPC. If the NPC has items to buy, sell or trade, they will be
    displayed.

    Args:
        code (str): The code of the NPC.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataPageNPCItem]
     """


    return sync_detailed(
        code=code,
client=client,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[Union[Any, DataPageNPCItem]]:
    """ Get Npc Items

     Retrieve the items list of a NPC. If the NPC has items to buy, sell or trade, they will be
    displayed.

    Args:
        code (str): The code of the NPC.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataPageNPCItem]]
     """


    kwargs = _get_kwargs(
        code=code,
page=page,
size=size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[Union[Any, DataPageNPCItem]]:
    """ Get Npc Items

     Retrieve the items list of a NPC. If the NPC has items to buy, sell or trade, they will be
    displayed.

    Args:
        code (str): The code of the NPC.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataPageNPCItem]
     """


    return (await asyncio_detailed(
        code=code,
client=client,
page=page,
size=size,

    )).parsed
