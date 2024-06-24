import dataclasses

import pytest

from src.seedwork.domain.value_objects import ValueObject


class DummyValueObject(ValueObject):
    a: int
    b: int


class TestValueObject:

    def test_equal_objects_are_equal(self):
        obj1 = DummyValueObject(1, 2)
        obj2 = DummyValueObject(1, 2)
        assert obj1 == obj2

    def test_different_objects_are_not_equal(self):
        obj1 = DummyValueObject(1, 2)
        obj2 = DummyValueObject(2, 3)
        assert obj1 != obj2

    def test_value_object_not_equal_to_different_type(self):
        obj1 = DummyValueObject(1, 2)
        assert obj1 != "a string"

    def test_hash_equal_objects_have_same_hash(self):
        obj1 = DummyValueObject(1, 2)
        obj2 = DummyValueObject(1, 2)
        assert hash(obj1) == hash(obj2)

    def test_repr_is_correct(self):
        obj = DummyValueObject(1, 2)
        assert repr(obj) == "DummyValueObject(a=1, b=2)"

    def test_immutability(self):
        obj = DummyValueObject(1, 2)
        with pytest.raises(dataclasses.FrozenInstanceError):
            obj.a = 10
