import contextlib
import copy
import functools
import itertools
import typing


@contextlib.contextmanager
def reset_changes(mapping: typing.MutableMapping):
    before = copy.deepcopy(mapping)
    yield mapping
    mapping.update(before)


ObjectT = typing.TypeVar('ObjectT', bound=object)
P = typing.ParamSpec('P')
T = typing.TypeVar('T')


def _get_lazy_field_name(func_name: str):
    return f'_lazyfield_{func_name}'


def lazy_field(
    func: typing.Callable[typing.Concatenate[ObjectT, P], T]
) -> typing.Callable[typing.Concatenate[ObjectT, P], T]:
    name = _get_lazy_field_name(func.__name__)

    @functools.wraps(func)
    def inner(self: ObjectT, *args: P.args, **kwargs: P.kwargs):
        try:
            result = typing.cast(T, object.__getattribute__(self, name))
        except AttributeError:
            result = func(self, *args, **kwargs)
            object.__setattr__(self, name, result)
        return result

    return inner


def update_field(target: object, val: typing.Any, func: typing.Callable):
    name = _get_lazy_field_name(func.__name__)
    object.__setattr__(target, name, val)


def reset_field(target: object, func: typing.Callable):
    name = _get_lazy_field_name(func.__name__)
    object.__delattr__(target, name)


def async_lazy_field(
    func: typing.Callable[
        typing.Concatenate[ObjectT, P],
        typing.Coroutine[typing.Any, typing.Any, T],
    ]
) -> typing.Callable[
    typing.Concatenate[ObjectT, P], typing.Coroutine[typing.Any, typing.Any, T]
]:
    name = _get_lazy_field_name(func.__name__)

    @functools.wraps(func)
    async def inner(self: ObjectT, *args: P.args, **kwargs: P.kwargs):
        try:
            result = typing.cast(T, object.__getattribute__(self, name))
        except AttributeError:
            result = await func(self, *args, **kwargs)
            object.__setattr__(self, name, result)
        return result

    return inner


def merge_dicts(
    left: typing.Mapping[str, typing.Any],
    right: typing.Mapping[str, typing.Any],
    priority: typing.Literal['right', 'left'] = 'left',
) -> typing.Mapping[str, typing.Any]:
    output = dict(left) | right
    for key, lvalue in left.items():
        if key not in right:
            continue
        rvalue = right[key]
        if type(lvalue) is not type(rvalue) or not isinstance(
            lvalue, (list, set, tuple, typing.Mapping)
        ):
            output[key] = lvalue if priority == 'left' else rvalue
        elif isinstance(lvalue, typing.Mapping):
            output[key] = merge_dicts(lvalue, rvalue, priority)
        else:
            typ = type(lvalue)
            output[key] = typ(itertools.chain(lvalue, rvalue))
    return output
