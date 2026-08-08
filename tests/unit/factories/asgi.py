from typing import Any


class ReceiveQueue:
    """A fake ASGI `receive` callable backed by a fixed list of
    messages, popped in order — one per `await receive()` call.
    """

    def __init__(self, messages: list[dict[str, Any]]) -> None:
        self._messages = list(messages)

    async def __call__(self) -> dict[str, Any]:
        return self._messages.pop(0)


class SendRecorder:
    """A fake ASGI `send` callable that records every message sent."""

    def __init__(self) -> None:
        self.messages: list[dict[str, Any]] = []

    async def __call__(self, message: dict[str, Any]) -> None:
        self.messages.append(message)


def http_scope(
    *,
    method: str = "GET",
    path: str = "/",
    query_string: bytes = b"",
    headers: list[tuple[bytes, bytes]] | None = None,
) -> dict[str, Any]:
    return {
        "type": "http",
        "method": method,
        "path": path,
        "query_string": query_string,
        "headers": headers or [],
    }


def http_receive(body: bytes = b"") -> ReceiveQueue:
    return ReceiveQueue(
        [{"type": "http.request", "body": body, "more_body": False}]
    )
