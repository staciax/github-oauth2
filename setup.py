import re

from setuptools import setup

version = ''
with open('github_oauth2/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)  # type: ignore

setup(version=version)
