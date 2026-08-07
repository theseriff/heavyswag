from typing import NamedTuple

from heavyswag.constants import HttpMethod, MethodType


class Body[Arg](NamedTuple): ...


class Query[Arg](NamedTuple): ...


class Preambule(NamedTuple):
    url: str
    method: HttpMethod | MethodType
    query: str = ""


class Request(NamedTuple):
    headers: list[tuple[str, str]]
    cookies: list[tuple[str, str]]

