from collections.abc import Callable

OriginalMigrationFunc = Callable[[], None]


class StageId(tuple[int, ...]):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, int):
            return cls((v,))
        if isinstance(v, str):
            if v.lower() == "none":
                return cls(())
            return cls(tuple(int(x) for x in v.split(".")))
        if isinstance(v, (tuple, list)):
            return cls(v)
        raise ValueError(f"Invalid stage: {v}")

    def __str__(self):
        if self == ():
            return "None"
        else:
            return ".".join(str(component) for component in self)

    def __repr__(self):
        return f"Stage({super().__repr__()})"
