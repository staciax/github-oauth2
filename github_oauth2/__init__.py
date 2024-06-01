"""
GitHub OAuth2
~~~~~~~~~~~~~~~~~~~
A basic GitHub OAuth2 client for Python.
:copyright: (c) 2024-present STACiA
:license: MIT, see LICENSE for more details.
"""

__title__ = 'github-oauth2'
__author__ = 'STACiA'
__license__ = 'MIT'
__copyright__ = 'Copyright 2024-present STACiA'
__version__ = '0.0.1a'

from . import utils as utils
from .client import GithubOAuth2Client as GithubOAuth2Client
from .errors import GithubOAuth2Error as GithubOAuth2Error, HTTPException as HTTPException
