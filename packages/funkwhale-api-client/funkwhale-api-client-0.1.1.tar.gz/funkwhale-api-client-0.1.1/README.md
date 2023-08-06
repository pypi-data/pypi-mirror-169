# funkwhale-api-client

A client library for accessing the Funkwhale API.

> **Note**: This client is under active development and is not considered production-ready.

## Usage

### Endpoint structure

The Funkwhale API client follows the same structure for each available endpoint.

1. Each API path/method combination is representsd by a Python module with four methods:
    1. `sync`: A blocking request that returns parsed data (if successful) or `None`
    2. `sync_detailed`: A blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    3. `asyncio`: An async request that returns parsed data (if successful) or `None`
    4. `asyncio_detailed`: An async request that always returns a `Request`, optionally with `parsed` set if the request was successful.
2. All path/query parameters and bodies are represented by method arguments.
3. If the endpoint contains tags, the first tag is used as a module name for the function
4. Any endpoint which doesn't contain a tag is located in `funkwhale_api_client.api.default`

### Use the library in your project

To get started, create a `Client` in your project.

```python
from funkwhale_api_client import Client

client = Client(base_url="https://api.example.com")
```

If you're interacting with endpoints that require authentication, create an `AuthenticatedClient`.

```python
from funkwhale_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")
```

Next, call the endpoint using the data model and endpoint method.

```python
from funkwhale_api_client.models import MyDataModel
from funkwhale_api_client.api.my_tag import get_my_data_model
from funkwhale_api_client.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# return more information with the sync_detailed method
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Call endpoints asynchronously by using the async methods.

```python
from funkwhale_api_client.models import MyDataModel
from funkwhale_api_client.api.my_tag import get_my_data_model
from funkwhale_api_client.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

### Certificate validation

The library attempts to validate TLS on HTTPS endpoints by default. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether. This is a **security risk** and **is not recommended**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

## Contribute to development

The Funkwhale API client is generated from the Funkwhale OpenAPI schema. If you notice an issue with the API itself, consider contributing to [Funkwhale](https://dev.funkwhale.audio/funkwhale/funkwhale).

### Build / publish the client

This project uses [Poetry](https://python-poetry.org/) to manage dependencies and packaging. Make sure you have it installed before you start.

To publish a new version of the client:

1. Update the metadata in `pyproject.toml` (e.g. authors, version)
2. If you're using a private repository, configure it with Poetry

    ```sh
    poetry config repositories.<your-repository-name> <url-to-your-repository> # Set up your repository
    poetry config http-basic.<your-repository-name> <username> <password> # Configure your credentials
    ```

3. Publish the client:
   1. Publish to PyPI with `poetry publish --build`
   2. Publish to a private repository with `poetry publish --build -r <your-repository-name>`.

If you want to install this client into another project without publishing it (e.g. for development) then:

1. If the project **uses Poetry**, add the client using `poetry add <path-to-this-client>`.
2. If the project doesn't use Poetry:
    1. Build a wheel with `poetry build -f wheel`
    2. Install that wheel from the target project `pip install <path-to-wheel>`

### Create tests

Tests are split into two types: **integration tests** and **model tests**.

#### Integration tests

You can test methods by calling them with a `Client` or `AuthenticatedClient` and expecting a specific result. Check `tests/integration/test_albums.py` for an example.

#### Model tests

You can test models by asserting equality with a response from a Funkwhale server. For example, to test the `/api/v1/albums` endpoint:

1. Find the API call in `api/albums/albums_list.py`
2. Check which model is used in the `_parse_response()` method. In this case `PaginatedAlbumList`
3. Fetch data from the `/api/v1/albums` endpoint using [cURL](https://curl.se/) and save the output to `tests/data/paginated_album_list.json`
4. Create a test to assert equality between the resulting JSON and the `PaginatedAlbumList` model using the model's `from_dict()` method

An example test can be found in `tests/unit/test_model_paginated_album_list.py`.

### Run tests

You can run the whole suite of tests with the following command:

```sh
poetry run pytest
```

### Making a release

Run `poetry version $new_version` to bump the version number in
`pyproject.toml`. Commit the changes.
Now we set a tag using `git tag v$(poetry version -s)` and push everything to
the repository with `git push --tags && git push`. CI will take care for
publishing the new package version to pypi.
