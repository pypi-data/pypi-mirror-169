# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['funkwhale_api_client',
 'funkwhale_api_client.api',
 'funkwhale_api_client.api.activity',
 'funkwhale_api_client.api.albums',
 'funkwhale_api_client.api.artists',
 'funkwhale_api_client.api.attachments',
 'funkwhale_api_client.api.auth',
 'funkwhale_api_client.api.channels',
 'funkwhale_api_client.api.favorites',
 'funkwhale_api_client.api.federation',
 'funkwhale_api_client.api.history',
 'funkwhale_api_client.api.instance',
 'funkwhale_api_client.api.libraries',
 'funkwhale_api_client.api.licenses',
 'funkwhale_api_client.api.listen',
 'funkwhale_api_client.api.manage',
 'funkwhale_api_client.api.moderation',
 'funkwhale_api_client.api.oauth',
 'funkwhale_api_client.api.oembed',
 'funkwhale_api_client.api.playlists',
 'funkwhale_api_client.api.plugins',
 'funkwhale_api_client.api.radios',
 'funkwhale_api_client.api.rate_limit',
 'funkwhale_api_client.api.search',
 'funkwhale_api_client.api.stream',
 'funkwhale_api_client.api.subscriptions',
 'funkwhale_api_client.api.tags',
 'funkwhale_api_client.api.text_preview',
 'funkwhale_api_client.api.tracks',
 'funkwhale_api_client.api.uploads',
 'funkwhale_api_client.api.users',
 'funkwhale_api_client.models']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.3.0', 'httpx>=0.15.4,<0.24.0', 'python-dateutil>=2.8.0,<3.0.0']

setup_kwargs = {
    'name': 'funkwhale-api-client',
    'version': '0.1.0rc1',
    'description': 'A client library for accessing Funkwhale API',
    'long_description': '# funkwhale-api-client\nA client library for accessing Funkwhale API\n\n## Usage\nFirst, create a client:\n\n```python\nfrom funkwhale_api_client import Client\n\nclient = Client(base_url="https://api.example.com")\n```\n\nIf the endpoints you\'re going to hit require authentication, use `AuthenticatedClient` instead:\n\n```python\nfrom funkwhale_api_client import AuthenticatedClient\n\nclient = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")\n```\n\nNow call your endpoint and use your models:\n\n```python\nfrom funkwhale_api_client.models import MyDataModel\nfrom funkwhale_api_client.api.my_tag import get_my_data_model\nfrom funkwhale_api_client.types import Response\n\nmy_data: MyDataModel = get_my_data_model.sync(client=client)\n# or if you need more info (e.g. status_code)\nresponse: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)\n```\n\nOr do the same thing with an async version:\n\n```python\nfrom funkwhale_api_client.models import MyDataModel\nfrom funkwhale_api_client.api.my_tag import get_my_data_model\nfrom funkwhale_api_client.types import Response\n\nmy_data: MyDataModel = await get_my_data_model.asyncio(client=client)\nresponse: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)\n```\n\nBy default, when you\'re calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.\n\n```python\nclient = AuthenticatedClient(\n    base_url="https://internal_api.example.com", \n    token="SuperSecretToken",\n    verify_ssl="/path/to/certificate_bundle.pem",\n)\n```\n\nYou can also disable certificate validation altogether, but beware that **this is a security risk**.\n\n```python\nclient = AuthenticatedClient(\n    base_url="https://internal_api.example.com", \n    token="SuperSecretToken", \n    verify_ssl=False\n)\n```\n\nThings to know:\n1. Every path/method combo becomes a Python module with four functions:\n    1. `sync`: Blocking request that returns parsed data (if successful) or `None`\n    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.\n    1. `asyncio`: Like `sync` but async instead of blocking\n    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking\n\n1. All path/query params, and bodies become method arguments.\n1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)\n1. Any endpoint which did not have a tag will be in `funkwhale_api_client.api.default`\n\n## Building / publishing this Client\nThis project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:\n1. Update the metadata in pyproject.toml (e.g. authors, version)\n1. If you\'re using a private repository, configure it with Poetry\n    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`\n    1. `poetry config http-basic.<your-repository-name> <username> <password>`\n1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`\n\nIf you want to install this client into another project without publishing it (e.g. for development) then:\n1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project\n1. If that project is not using Poetry:\n    1. Build a wheel with `poetry build -f wheel`\n    1. Install that wheel from the other project `pip install <path-to-wheel>`\n\n\n## Contributing\n\n### Run tests\n\nTo run the tests, run `poetry run pytest`.\n\n### How to write test cases\n\nThere are two things to test: The models and the API functions.\n\nLets imagine you want to write a test case for the endpoint `/api/v1/albums`\nfocusing on the models for now. Since this endpoint lists the Albums, the\ncorrect API call is in `api/albums/albums_list.py`. Check the function called\n`_parse_response()`. The model used to parse the response is called\n`PaginatedAlbumList`, which we will run tests against. Now curl the endpoint you\nwant to write tests for and put the response into `tests/data/albums.json`. Now\nwe can load this json file, load it with the model and do some assertions. The\nexample is available in `tests/unit/test_model_paginated_album_list.py`.\n',
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
