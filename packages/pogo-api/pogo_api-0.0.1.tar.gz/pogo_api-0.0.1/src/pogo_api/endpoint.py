from typing import Callable, Coroutine

from pogo_api.http import Method
from pogo_api.route import Route


class _Endpoint:
    method = Method.GET
    endpoint: Callable[..., Coroutine]

    def __init__(self) -> None:
        self._name = self.__class__.__name__

    @property
    def path(self) -> str:
        name = self._name.lower()
        return f"/{name}"

    @property
    def route(self) -> Route:
        return Route(
            path=self.path,
            method=self.method,
            endpoint=self.endpoint,
            tag=self._name,
        )


class DeleteEndpoint(_Endpoint):
    method = Method.DELETE


class GetEndpoint(_Endpoint):
    method = Method.GET


class PatchEndpoint(_Endpoint):
    method = Method.PATCH


class PostEndpoint(_Endpoint):
    method = Method.POST


class PutEndpoint(_Endpoint):
    method = Method.PUT


class UpdateEndpoint(_Endpoint):
    method = Method.UPDATE
