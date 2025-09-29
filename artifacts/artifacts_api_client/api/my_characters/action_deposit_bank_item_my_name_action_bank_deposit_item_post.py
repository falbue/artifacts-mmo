from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bank_item_transaction_response_schema import BankItemTransactionResponseSchema
from ...models.simple_item_schema import SimpleItemSchema
from typing import cast



def _get_kwargs(
    name: str,
    *,
    body: list['SimpleItemSchema'],

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/my/{name}/action/bank/deposit/item".format(name=name,),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)




    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, BankItemTransactionResponseSchema]]:
    if response.status_code == 200:
        response_200 = BankItemTransactionResponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 461:
        response_461 = cast(Any, None)
        return response_461

    if response.status_code == 462:
        response_462 = cast(Any, None)
        return response_462

    if response.status_code == 478:
        response_478 = cast(Any, None)
        return response_478

    if response.status_code == 486:
        response_486 = cast(Any, None)
        return response_486

    if response.status_code == 498:
        response_498 = cast(Any, None)
        return response_498

    if response.status_code == 499:
        response_499 = cast(Any, None)
        return response_499

    if response.status_code == 598:
        response_598 = cast(Any, None)
        return response_598

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, BankItemTransactionResponseSchema]]:
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
    body: list['SimpleItemSchema'],

) -> Response[Union[Any, BankItemTransactionResponseSchema]]:
    """ Action Deposit Bank Item

     Deposit multiple items in a bank on the character's map.
    The cooldown will be 3 seconds multiplied by the number of different items withdrawn.

    Args:
        name (str): Name of your character.
        body (list['SimpleItemSchema']): List of items to deposit in the bank.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BankItemTransactionResponseSchema]]
     """


    kwargs = _get_kwargs(
        name=name,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    body: list['SimpleItemSchema'],

) -> Optional[Union[Any, BankItemTransactionResponseSchema]]:
    """ Action Deposit Bank Item

     Deposit multiple items in a bank on the character's map.
    The cooldown will be 3 seconds multiplied by the number of different items withdrawn.

    Args:
        name (str): Name of your character.
        body (list['SimpleItemSchema']): List of items to deposit in the bank.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BankItemTransactionResponseSchema]
     """


    return sync_detailed(
        name=name,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: list['SimpleItemSchema'],

) -> Response[Union[Any, BankItemTransactionResponseSchema]]:
    """ Action Deposit Bank Item

     Deposit multiple items in a bank on the character's map.
    The cooldown will be 3 seconds multiplied by the number of different items withdrawn.

    Args:
        name (str): Name of your character.
        body (list['SimpleItemSchema']): List of items to deposit in the bank.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BankItemTransactionResponseSchema]]
     """


    kwargs = _get_kwargs(
        name=name,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    body: list['SimpleItemSchema'],

) -> Optional[Union[Any, BankItemTransactionResponseSchema]]:
    """ Action Deposit Bank Item

     Deposit multiple items in a bank on the character's map.
    The cooldown will be 3 seconds multiplied by the number of different items withdrawn.

    Args:
        name (str): Name of your character.
        body (list['SimpleItemSchema']): List of items to deposit in the bank.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BankItemTransactionResponseSchema]
     """


    return (await asyncio_detailed(
        name=name,
client=client,
body=body,

    )).parsed
