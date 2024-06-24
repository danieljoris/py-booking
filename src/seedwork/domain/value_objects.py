from abc import ABC, ABCMeta
from dataclasses import dataclass


class ImmutableMeta(ABCMeta):
    def __new__(cls, name, bases, class_dict):
        cls_instance = super().__new__(cls, name, bases, class_dict)
        return dataclass(frozen=True)(cls_instance)


class ValueObject(ABC, metaclass=ImmutableMeta):
    def __eq__(self, other):
        if not isinstance(other, ValueObject):
            return False
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(frozenset(self.__dict__.items()))

    def __repr__(self):
        attributes = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"
