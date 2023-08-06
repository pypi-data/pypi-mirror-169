import os
import pathlib
import typing

StrOrPath = str | pathlib.Path
MISSING = object()
T = typing.TypeVar('T')
CastType: typing.TypeAlias = typing.Callable[[typing.Any], typing.Any]
ConfigLike: typing.TypeAlias = typing.Callable[
    [str, CastType, typing.Any], typing.Any
]


class Environ(typing.MutableMapping):
    def __init__(self, environ: typing.MutableMapping = os.environ) -> None:
        self._environ = environ
        self._has_been_read = set[typing.Any]()

    def __getitem__(self, name: str) -> typing.Any:
        self._has_been_read.add(name)
        return self._environ[name]

    def __setitem__(self, name: str, val: typing.Any) -> None:
        if name in self._has_been_read:
            raise EnvironError(
                f'Attempting to set environ[{name!r}], but the value'
                ' has already been read'
            )
        self._environ[name] = val

    def __delitem__(self, name: str) -> None:
        if name in self._has_been_read:
            raise EnvironError(
                f'Attempting to delete environ[{name!r}], but the value'
                ' has already been read'
            )
        del self._environ[name]

    def __iter__(self) -> typing.Iterator:
        return iter(self._environ)

    def __len__(self) -> int:
        return len(self._environ)


environ = Environ()


class Config:
    def __init__(
        self, *, env_file: StrOrPath | None = None, environ: Environ = environ
    ) -> None:
        self._environ = environ
        self._file_vals: dict[str, str] = {}
        if env_file is not None:
            self._read_file(env_file)

    @staticmethod
    def _read_file(env_file: StrOrPath):
        output = {}
        with open(env_file) as stream:
            for line in stream:
                if line.startswith('#') or '=' not in line:
                    continue
                name, value = line.split('=', 1)
                output[name.strip()] = value.strip()
        return output

    def _get_value(self, name: str, default: typing.Any) -> str:
        value = self._environ.get(name, self._file_vals.get(name, default))
        if value is MISSING:
            raise MissingNameError(name)
        return value

    @staticmethod
    def _cast(name: str, value: typing.Any, cast: type | CastType):
        try:
            return cast(value)
        except (TypeError, ValueError) as err:
            raise type(err)(
                f'Config {name} has value {value!r}. Not a valid {cast.__name__}'
            ) from err

    def get(
        self,
        name: str,
        cast: CastType | None = None,
        default: typing.Any = MISSING,
    ):
        value = self._get_value(name, default)
        if cast is None:
            return value
        return self._cast(name, value, cast)

    @typing.overload
    def __call__(
        self,
        name: str,
        cast: typing.Callable[[str], T],
        default: typing.Any = MISSING,
    ) -> T:
        ...

    @typing.overload
    def __call__(
        self, name: str, cast: None = None, default: typing.Any = MISSING
    ) -> typing.Any:
        ...

    def __call__(
        self,
        name: str,
        cast: CastType | None = None,
        default: typing.Any = MISSING,
    ) -> typing.Any:
        return self.get(name, cast, default)


class EnvironError(Exception):
    ...


class MissingNameError(KeyError):
    def __init__(self, name: str) -> None:
        super().__init__(f'Config {name} is missing and has no default.')


class MissingNamesError(KeyError):
    def __init__(self, *names: str) -> None:
        super().__init__(
            f'Config {", ".join(names)!r} is missing and has no default.'
        )
