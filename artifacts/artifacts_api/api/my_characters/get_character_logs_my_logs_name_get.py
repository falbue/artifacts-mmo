from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.data_page_log_schema import DataPageLogSchema
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    name: str,
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
        "url": "/my/logs/{name}".format(name=name,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, DataPageLogSchema]]:
    if response.status_code == 200:
        response_200 = DataPageLogSchema.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 498:
        response_498 = cast(Any, None)
        return response_498

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, DataPageLogSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[Union[Any, DataPageLogSchema]]:
    """ Get Character Logs

     History of the last actions of your character.

    Args:
        name (str): Name of your character.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataPageLogSchema]]
     """


    kwargs = _get_kwargs(
        name=name,
page=page,
size=size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[Union[Any, DataPageLogSchema]]:
    """ Get Character Logs

     History of the last actions of your character.

    Args:
        name (str): Name of your character.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataPageLogSchema]
     """


    return sync_detailed(
        name=name,
client=client,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[Union[Any, DataPageLogSchema]]:
    """ Get Character Logs

     History of the last actions of your character.

    Args:
        name (str): Name of your character.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataPageLogSchema]]
     """


    kwargs = _get_kwargs(
        name=name,
page=page,
size=size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[Union[Any, DataPageLogSchema]]:
    """ Get Character Logs

     History of the last actions of your character.

    Args:
        name (str): Name of your character.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataPageLogSchema]
     """


    return (await asyncio_detailed(
        name=name,
client=client,
page=page,
size=size,

    )).parsed
