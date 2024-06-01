from aiohttp import ClientResponse


class GithubOAuth2Error(Exception):
    pass


class HTTPException(GithubOAuth2Error):
    def __init__(
        self,
        response: ClientResponse,
        data: dict | None = None,
    ) -> None:
        self.status_code: int = response.status
        self.message: str = data.get('message', '') if data else ''
