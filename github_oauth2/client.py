import urllib.parse
from typing import Any

import aiohttp

from .errors import HTTPException


class GithubOAuth2Client:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

    async def request(self, method: str, /, url: str, **kwargs: Any) -> Any:
        headers = {
            'Accept': 'application/json',
        }

        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))

        async with aiohttp.ClientSession() as client:
            response = await client.request(
                method=method,
                url=url,
                headers=headers,
                **kwargs,
            )

            data = await response.json()

            if response.status != 200:
                raise HTTPException(response, data)

            return data

    def get_access_token(
        self,
        code: str,
        *,
        scope: str | None = None,
        redirect_uri: str | None = None,
    ) -> Any:
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code,
        }
        if scope:
            params['scope'] = scope
        if redirect_uri:
            params['redirect_uri'] = redirect_uri

        return self.request(
            'POST',
            'https://github.com/login/oauth/access_token' + '?' + urllib.parse.urlencode(params),
            params=params,
        )

    def get_user(self, access_token: str) -> Any:
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        return self.request(
            'GET',
            'https://api.github.com/user',
            headers=headers,
        )

    def get_user_emails(self, access_token: str) -> Any:
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        return self.request(
            'GET',
            'https://api.github.com/user/emails',
            headers=headers,
        )
