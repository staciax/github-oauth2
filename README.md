# Github OAuth2 Client 
A simple Github OAuth2 client for Python.

## Installation
```bash
pip install git+https://github.com/staciax/github-oauth2.git
```

## Quick Example with FastAPI
```python
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from github_oauth2 import GithubOAuth2Client
from github_oauth2.utils import oauth2_url

app = FastAPI()

github_client_id = 'client_id'
github_client_secret = 'client_secret'


@app.get('/github-login')
async def github_login() -> RedirectResponse:
    url = oauth2_url(client_id=github_client_id, scope='user:email')
    return RedirectResponse(url, status_code=302)


@app.get('/github-code')
async def github_code(code: str) -> dict:
    client = GithubOAuth2Client(
        client_id=github_client_id,
        client_secret=github_client_secret,
    )
    data = await client.get_access_token(code=code, scope='user:email')
    user = await client.get_user(access_token=data['access_token'])

    return user

```

## License
MIT