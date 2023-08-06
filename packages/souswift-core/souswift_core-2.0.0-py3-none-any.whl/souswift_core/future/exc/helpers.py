import asyncio
import functools
import typing

from . import exceptions

T = typing.TypeVar('T')
P = typing.ParamSpec('P')


def raise_on_none(
    target: str,
    *,
    exc_type: type[exceptions.TargetError] = exceptions.NotFoundError
):
    frozen_exc = exc_type(target)

    def outer(func: typing.Callable[P, T | None]) -> typing.Callable[P, T]:
        @functools.wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> T:
            result = func(*args, **kwargs)
            if result is None:
                raise frozen_exc
            return result

        return inner

    return outer


def async_raise_on_none(
    target: str,
    *,
    exc_type: type[exceptions.TargetError] = exceptions.NotFoundError
):
    frozen_exc = exc_type(target)

    def outer(
        func: typing.Callable[
            P, typing.Coroutine[typing.Any, typing.Any, T | None]
        ]
    ) -> typing.Callable[P, typing.Coroutine[typing.Any, typing.Any, T]]:
        @functools.wraps(func)
        async def inner(*args: P.args, **kwargs: P.kwargs) -> T:
            result = await func(*args, **kwargs)
            if result is None:
                raise frozen_exc
            return result

        return inner

    return outer


def forward_to_exc(exc_source: type[Exception], error: exceptions.Error):
    async def async_wrapper(
        func: typing.Callable[P, typing.Coroutine[typing.Any, typing.Any, T]],
        *args: P.args,
        **kwargs: P.kwargs
    ) -> T:
        try:
            return await func(*args, **kwargs)
        except exc_source as exc:
            raise error from exc

    def wrapper(
        func: typing.Callable[P, T], *args: P.args, **kwargs: P.kwargs
    ) -> T:
        try:
            return func(*args, **kwargs)
        except exc_source as exc:
            raise error from exc

    @typing.overload
    def outer(func: typing.Callable[P, T]) -> typing.Callable[P, T]:
        ...

    @typing.overload
    def outer(
        func: typing.Callable[P, typing.Coroutine[typing.Any, typing.Any, T]]
    ) -> typing.Callable[P, typing.Coroutine[typing.Any, typing.Any, T]]:
        ...

    def outer(func: typing.Callable) -> typing.Callable:
        _wrapper_func = (
            async_wrapper if asyncio.iscoroutinefunction(func) else wrapper
        )

        @functools.wraps(func)
        def inner(*args, **kwargs):
            return _wrapper_func(func, *args, **kwargs)

        return inner

    return outer
