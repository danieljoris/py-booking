import pytest

from src.domain.entities.entity import Entity


class TestEntity:
    def test_entity_initialization(self):
        entity = Entity()
        assert entity.id is not None
        assert isinstance(entity.id, str)

    def test_entity_equality_with_different_instances(self):
        entity1 = Entity()
        entity2 = Entity()
        assert entity1 != entity2
        assert entity1.id != entity2.id

    def test_entity_equality_with_same_instance(self):
        entity = Entity()
        assert entity == entity

    def test_entity_equality_with_non_entity(self):
        entity = Entity()
        non_entity = object()
        assert entity != non_entity

    def test_entity_hash(self):
        entity = Entity()
        assert hash(entity) == hash(entity.id)

    def test_entity_different_hashes_for_different_ids(self):
        entity1 = Entity()
        entity2 = Entity()
        assert hash(entity1) != hash(entity2)

    def test_entity_unique_ids(self):
        entity1 = Entity()
        entity2 = Entity()
        assert entity1.id != entity2.id
