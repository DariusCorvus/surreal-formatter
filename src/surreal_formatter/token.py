from typing import Protocol


class Token(Protocol):
    type: str
    value: str


def upper(token: Token) -> Token:
    token.value = token.value.upper()
    return token


def lower(token: Token) -> Token:
    token.value = token.value.lower()
    return token
