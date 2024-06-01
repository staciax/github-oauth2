import urllib.parse


def oauth2_url(
    client_id: str,
    *,
    scope: str | None = None,
    redirect_uri: str | None = None,
    state: str | None = None,
) -> str:
    params = {
        'client_id': client_id,
    }
    if scope:
        params['scope'] = scope
    if redirect_uri:
        params['redirect_uri'] = redirect_uri
    if state:
        params['state'] = state

    base_url = 'https://github.com/login/oauth/authorize'
    return base_url + '?' + urllib.parse.urlencode(params)
