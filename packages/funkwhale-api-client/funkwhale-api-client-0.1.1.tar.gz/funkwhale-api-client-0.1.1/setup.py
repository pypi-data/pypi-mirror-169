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
    'version': '0.1.1',
    'description': 'A client library for accessing Funkwhale API',
    'long_description': '# funkwhale-api-client\n\nA client library for accessing the Funkwhale API.\n\n> **Note**: This client is under active development and is not considered production-ready.\n\n## Usage\n\n### Endpoint structure\n\nThe Funkwhale API client follows the same structure for each available endpoint.\n\n1. Each API path/method combination is representsd by a Python module with four methods:\n    1. `sync`: A blocking request that returns parsed data (if successful) or `None`\n    2. `sync_detailed`: A blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.\n    3. `asyncio`: An async request that returns parsed data (if successful) or `None`\n    4. `asyncio_detailed`: An async request that always returns a `Request`, optionally with `parsed` set if the request was successful.\n2. All path/query parameters and bodies are represented by method arguments.\n3. If the endpoint contains tags, the first tag is used as a module name for the function\n4. Any endpoint which doesn\'t contain a tag is located in `funkwhale_api_client.api.default`\n\n### Use the library in your project\n\nTo get started, create a `Client` in your project.\n\n```python\nfrom funkwhale_api_client import Client\n\nclient = Client(base_url="https://api.example.com")\n```\n\nIf you\'re interacting with endpoints that require authentication, create an `AuthenticatedClient`.\n\n```python\nfrom funkwhale_api_client import AuthenticatedClient\n\nclient = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")\n```\n\nNext, call the endpoint using the data model and endpoint method.\n\n```python\nfrom funkwhale_api_client.models import MyDataModel\nfrom funkwhale_api_client.api.my_tag import get_my_data_model\nfrom funkwhale_api_client.types import Response\n\nmy_data: MyDataModel = get_my_data_model.sync(client=client)\n# return more information with the sync_detailed method\nresponse: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)\n```\n\nCall endpoints asynchronously by using the async methods.\n\n```python\nfrom funkwhale_api_client.models import MyDataModel\nfrom funkwhale_api_client.api.my_tag import get_my_data_model\nfrom funkwhale_api_client.types import Response\n\nmy_data: MyDataModel = await get_my_data_model.asyncio(client=client)\nresponse: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)\n```\n\n### Certificate validation\n\nThe library attempts to validate TLS on HTTPS endpoints by default. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.\n\n```python\nclient = AuthenticatedClient(\n    base_url="https://internal_api.example.com", \n    token="SuperSecretToken",\n    verify_ssl="/path/to/certificate_bundle.pem",\n)\n```\n\nYou can also disable certificate validation altogether. This is a **security risk** and **is not recommended**.\n\n```python\nclient = AuthenticatedClient(\n    base_url="https://internal_api.example.com", \n    token="SuperSecretToken", \n    verify_ssl=False\n)\n```\n\n## Contribute to development\n\nThe Funkwhale API client is generated from the Funkwhale OpenAPI schema. If you notice an issue with the API itself, consider contributing to [Funkwhale](https://dev.funkwhale.audio/funkwhale/funkwhale).\n\n### Build / publish the client\n\nThis project uses [Poetry](https://python-poetry.org/) to manage dependencies and packaging. Make sure you have it installed before you start.\n\nTo publish a new version of the client:\n\n1. Update the metadata in `pyproject.toml` (e.g. authors, version)\n2. If you\'re using a private repository, configure it with Poetry\n\n    ```sh\n    poetry config repositories.<your-repository-name> <url-to-your-repository> # Set up your repository\n    poetry config http-basic.<your-repository-name> <username> <password> # Configure your credentials\n    ```\n\n3. Publish the client:\n   1. Publish to PyPI with `poetry publish --build`\n   2. Publish to a private repository with `poetry publish --build -r <your-repository-name>`.\n\nIf you want to install this client into another project without publishing it (e.g. for development) then:\n\n1. If the project **uses Poetry**, add the client using `poetry add <path-to-this-client>`.\n2. If the project doesn\'t use Poetry:\n    1. Build a wheel with `poetry build -f wheel`\n    2. Install that wheel from the target project `pip install <path-to-wheel>`\n\n### Create tests\n\nTests are split into two types: **integration tests** and **model tests**.\n\n#### Integration tests\n\nYou can test methods by calling them with a `Client` or `AuthenticatedClient` and expecting a specific result. Check `tests/integration/test_albums.py` for an example.\n\n#### Model tests\n\nYou can test models by asserting equality with a response from a Funkwhale server. For example, to test the `/api/v1/albums` endpoint:\n\n1. Find the API call in `api/albums/albums_list.py`\n2. Check which model is used in the `_parse_response()` method. In this case `PaginatedAlbumList`\n3. Fetch data from the `/api/v1/albums` endpoint using [cURL](https://curl.se/) and save the output to `tests/data/paginated_album_list.json`\n4. Create a test to assert equality between the resulting JSON and the `PaginatedAlbumList` model using the model\'s `from_dict()` method\n\nAn example test can be found in `tests/unit/test_model_paginated_album_list.py`.\n\n### Run tests\n\nYou can run the whole suite of tests with the following command:\n\n```sh\npoetry run pytest\n```\n\n### Making a release\n\nRun `poetry version $new_version` to bump the version number in\n`pyproject.toml`. Commit the changes.\nNow we set a tag using `git tag v$(poetry version -s)` and push everything to\nthe repository with `git push --tags && git push`. CI will take care for\npublishing the new package version to pypi.\n',
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
