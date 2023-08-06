import enum


class StrEnum(str, enum.Enum):
    @staticmethod
    def _generate_next_value(name: str, *_, **__kwds__):
        return name.lower()

    def __str__(self):
        return self.value


class Env(StrEnum):
    LOCAL = enum.auto()
    DEV = enum.auto()
    QA = enum.auto()
    PROD = enum.auto()
    TEST = enum.auto()
