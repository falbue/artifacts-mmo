from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.equipment_response_schema import EquipmentResponseSchema
from ...models.unequip_schema import UnequipSchema
from typing import cast



def _get_kwargs(
    name: str,
    *,
    body: UnequipSchema,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/my/{name}/action/unequip".format(name=name,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, EquipmentResponseSchema]]:
    if response.status_code == 200:
        response_200 = EquipmentResponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 478:
        response_478 = cast(Any, None)
        return response_478

    if response.status_code == 483:
        response_483 = cast(Any, None)
        return response_483

    if response.status_code == 486:
        response_486 = cast(Any, None)
        return response_486

    if response.status_code == 491:
        response_491 = cast(Any, None)
        return response_491

    if response.status_code == 497:
        response_497 = cast(Any, None)
        return response_497

    if response.status_code == 498:
        response_498 = cast(Any, None)
        return response_498

    if response.status_code == 499:
        response_499 = cast(Any, None)
        return response_499

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, EquipmentResponseSchema]]:
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
    body: UnequipSchema,

) -> Response[Union[Any, EquipmentResponseSchema]]:
    """ Action Unequip Item

     Unequip an item on your character.

    Args:
        name (str): Name of your character.
        body (UnequipSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EquipmentResponseSchema]]
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
    body: UnequipSchema,

) -> Optional[Union[Any, EquipmentResponseSchema]]:
    """ Action Unequip Item

     Unequip an item on your character.

    Args:
        name (str): Name of your character.
        body (UnequipSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EquipmentResponseSchema]
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
    body: UnequipSchema,

) -> Response[Union[Any, EquipmentResponseSchema]]:
    """ Action Unequip Item

     Unequip an item on your character.

    Args:
        name (str): Name of your character.
        body (UnequipSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EquipmentResponseSchema]]
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
    body: UnequipSchema,

) -> Optional[Union[Any, EquipmentResponseSchema]]:
    """ Action Unequip Item

     Unequip an item on your character.

    Args:
        name (str): Name of your character.
        body (UnequipSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EquipmentResponseSchema]
     """


    return (await asyncio_detailed(
        name=name,
client=client,
body=body,

    )).parsed
