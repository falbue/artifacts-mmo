from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ge_order_reponse_schema import GEOrderReponseSchema
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/grandexchange/orders/{id}".format(id=id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, GEOrderReponseSchema]]:
    if response.status_code == 200:
        response_200 = GEOrderReponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, GEOrderReponseSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, GEOrderReponseSchema]]:
    """ Get Ge Sell Order

     Retrieve the sell order of a item.

    Args:
        id (str): The id of the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GEOrderReponseSchema]]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, GEOrderReponseSchema]]:
    """ Get Ge Sell Order

     Retrieve the sell order of a item.

    Args:
        id (str): The id of the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GEOrderReponseSchema]
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, GEOrderReponseSchema]]:
    """ Get Ge Sell Order

     Retrieve the sell order of a item.

    Args:
        id (str): The id of the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GEOrderReponseSchema]]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, GEOrderReponseSchema]]:
    """ Get Ge Sell Order

     Retrieve the sell order of a item.

    Args:
        id (str): The id of the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GEOrderReponseSchema]
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
