from __future__ import annotations
import dataclasses
from dataclasses import dataclass, field
from typing import *  # type: ignore
import sys
import contextlib
import dataclasses
import sys

__all__ = ["hyperparam", "hyperparams_from", "print_hyperparam_template"]


def hyperparam() -> Any:
    return HyperparamDescriptor()


@contextlib.contextmanager
def hyperparams_from(config: object):
    _tmp = HyperparamDescriptor.config
    HyperparamDescriptor.config = config
    yield
    HyperparamDescriptor.config = _tmp


def print_hyperparam_template(
    filepath: Optional[str] = None, header="# type: ignore\nfrom typing import *\n"
) -> None:
    file = open(filepath, "w") if filepath is not None else sys.stdout

    print(header, file=file)

    for cls, annotations in _annotations_by_class.items():
        # print("#", cls.__name__, file=file)
        for name, annotation in annotations.items():
            print(name + ":", annotation, file=file)
        print(file=file)

    if filepath is not None:
        file.close()


class HyperparamDescriptor:
    config: Optional[object] = None

    def __init__(self):
        self.field = field(default_factory=lambda: getattr(self.config, self.name))
        self.exception = None

    def __set_name__(self, owner, name):
        self.name = name

        if name not in owner.__annotations__:
            raise InvalidHyperparameter(
                f"Missing type annotation for hyperparameter `{name}`."
            )

        if owner not in _annotations_by_class:
            _annotations_by_class[owner] = {}

        anot = owner.__annotations__[name]
        for cls, annotations in _annotations_by_class.items():
            if name in annotations and anot != annotations[name]:
                raise InvalidHyperparameter(
                    f"Hyperparameter name `{name}` is already used with a different type annotation.\n({owner.__qualname__} uses `{anot}` but {cls.__qualname__} uses `{annotations[name]}`)"
                )
            else:
                annotations[name] = anot

        _annotations_by_class[owner][name] = anot

    def __get__(self, obj, objtype=None):
        print(obj, objtype)
        print(dataclasses.is_dataclass(objtype))
        return self.field


_annotations_by_class = {}


class InvalidHyperparameter(Exception):
    pass


_excepthook = sys.excepthook


def excepthook(type, value, tb):
    if isinstance(value.__cause__, InvalidHyperparameter):
        _excepthook(
            type,
            value.__cause__.with_traceback(value.__traceback__),
            value.__traceback__,
        )
    else:
        _excepthook(type, value, tb)


sys.excepthook = excepthook


if __name__ == "__main__":
    @dataclass
    class X:
        x: int = hyperparam()

    class Y:
        x: int = hyperparam()

    # import configA
    # with hyperparams_from(configA):
    #     X()
