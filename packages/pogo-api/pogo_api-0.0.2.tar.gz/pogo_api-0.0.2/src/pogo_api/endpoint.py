from typing import Callable, Coroutine

from pogo_api.http import Method
from pogo_api.route import Route


class Endpoint:
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


class DeleteEndpoint(Endpoint):
    method = Method.DELETE


class GetEndpoint(Endpoint):
    method = Method.GET


class PatchEndpoint(Endpoint):
    method = Method.PATCH


class PostEndpoint(Endpoint):
    method = Method.POST


class PutEndpoint(Endpoint):
    method = Method.PUT


class UpdateEndpoint(Endpoint):
    method = Method.UPDATE
