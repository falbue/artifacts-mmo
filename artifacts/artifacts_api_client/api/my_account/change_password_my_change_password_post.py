from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.change_password import ChangePassword
from ...models.response_schema import ResponseSchema
from typing import cast



def _get_kwargs(
    *,
    body: ChangePassword,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/my/change_password",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ResponseSchema]]:
    if response.status_code == 200:
        response_200 = ResponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 458:
        response_458 = cast(Any, None)
        return response_458

    if response.status_code == 459:
        response_459 = cast(Any, None)
        return response_459

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ResponseSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ChangePassword,

) -> Response[Union[Any, ResponseSchema]]:
    """ Change Password

     Change your account password. Changing the password reset the account token.

    Args:
        body (ChangePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ResponseSchema]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: ChangePassword,

) -> Optional[Union[Any, ResponseSchema]]:
    """ Change Password

     Change your account password. Changing the password reset the account token.

    Args:
        body (ChangePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ResponseSchema]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ChangePassword,

) -> Response[Union[Any, ResponseSchema]]:
    """ Change Password

     Change your account password. Changing the password reset the account token.

    Args:
        body (ChangePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ResponseSchema]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ChangePassword,

) -> Optional[Union[Any, ResponseSchema]]:
    """ Change Password

     Change your account password. Changing the password reset the account token.

    Args:
        body (ChangePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ResponseSchema]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
