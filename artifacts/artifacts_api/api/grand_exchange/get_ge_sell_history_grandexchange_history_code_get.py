from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.data_page_ge_order_history_schema import DataPageGeOrderHistorySchema
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    code: str,
    *,
    seller: Union[Unset, str] = UNSET,
    buyer: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["seller"] = seller

    params["buyer"] = buyer

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/grandexchange/history/{code}".format(code=code,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, DataPageGeOrderHistorySchema]]:
    if response.status_code == 200:
        response_200 = DataPageGeOrderHistorySchema.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, DataPageGeOrderHistorySchema]]:
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
    seller: Union[Unset, str] = UNSET,
    buyer: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[Union[Any, DataPageGeOrderHistorySchema]]:
    """ Get Ge Sell History

     Fetch the sales history of the item for the last 7 days.

    Args:
        code (str): The code of the item.
        seller (Union[Unset, str]): The seller (account name) of the item.
        buyer (Union[Unset, str]): The buyer (account name) of the item.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataPageGeOrderHistorySchema]]
     """


    kwargs = _get_kwargs(
        code=code,
seller=seller,
buyer=buyer,
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
    seller: Union[Unset, str] = UNSET,
    buyer: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[Union[Any, DataPageGeOrderHistorySchema]]:
    """ Get Ge Sell History

     Fetch the sales history of the item for the last 7 days.

    Args:
        code (str): The code of the item.
        seller (Union[Unset, str]): The seller (account name) of the item.
        buyer (Union[Unset, str]): The buyer (account name) of the item.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataPageGeOrderHistorySchema]
     """


    return sync_detailed(
        code=code,
client=client,
seller=seller,
buyer=buyer,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    seller: Union[Unset, str] = UNSET,
    buyer: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[Union[Any, DataPageGeOrderHistorySchema]]:
    """ Get Ge Sell History

     Fetch the sales history of the item for the last 7 days.

    Args:
        code (str): The code of the item.
        seller (Union[Unset, str]): The seller (account name) of the item.
        buyer (Union[Unset, str]): The buyer (account name) of the item.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataPageGeOrderHistorySchema]]
     """


    kwargs = _get_kwargs(
        code=code,
seller=seller,
buyer=buyer,
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
    seller: Union[Unset, str] = UNSET,
    buyer: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[Union[Any, DataPageGeOrderHistorySchema]]:
    """ Get Ge Sell History

     Fetch the sales history of the item for the last 7 days.

    Args:
        code (str): The code of the item.
        seller (Union[Unset, str]): The seller (account name) of the item.
        buyer (Union[Unset, str]): The buyer (account name) of the item.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataPageGeOrderHistorySchema]
     """


    return (await asyncio_detailed(
        code=code,
client=client,
seller=seller,
buyer=buyer,
page=page,
size=size,

    )).parsed
