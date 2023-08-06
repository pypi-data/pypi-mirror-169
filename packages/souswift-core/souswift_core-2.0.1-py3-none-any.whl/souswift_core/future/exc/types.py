from typing import TypedDict


class ValidationPayload(TypedDict):
    type_: str
    field: str
    detail: str
    error_key: str | None
