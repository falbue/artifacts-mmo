from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.password_reset_confirm_schema import PasswordResetConfirmSchema
from ...models.password_reset_response_schema import PasswordResetResponseSchema
from typing import cast



def _get_kwargs(
    *,
    body: PasswordResetConfirmSchema,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/reset_password",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, PasswordResetResponseSchema]]:
    if response.status_code == 200:
        response_200 = PasswordResetResponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 560:
        response_560 = cast(Any, None)
        return response_560

    if response.status_code == 561:
        response_561 = cast(Any, None)
        return response_561

    if response.status_code == 562:
        response_562 = cast(Any, None)
        return response_562

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, PasswordResetResponseSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PasswordResetConfirmSchema,

) -> Response[Union[Any, PasswordResetResponseSchema]]:
    """ Reset Password

     Reset password with a token. Use /forgot_password to get a token by email.

    Args:
        body (PasswordResetConfirmSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PasswordResetResponseSchema]]
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
    client: Union[AuthenticatedClient, Client],
    body: PasswordResetConfirmSchema,

) -> Optional[Union[Any, PasswordResetResponseSchema]]:
    """ Reset Password

     Reset password with a token. Use /forgot_password to get a token by email.

    Args:
        body (PasswordResetConfirmSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PasswordResetResponseSchema]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PasswordResetConfirmSchema,

) -> Response[Union[Any, PasswordResetResponseSchema]]:
    """ Reset Password

     Reset password with a token. Use /forgot_password to get a token by email.

    Args:
        body (PasswordResetConfirmSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PasswordResetResponseSchema]]
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
    client: Union[AuthenticatedClient, Client],
    body: PasswordResetConfirmSchema,

) -> Optional[Union[Any, PasswordResetResponseSchema]]:
    """ Reset Password

     Reset password with a token. Use /forgot_password to get a token by email.

    Args:
        body (PasswordResetConfirmSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PasswordResetResponseSchema]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
