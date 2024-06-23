from typing import Generator

import pytest

from src.domain.entities.host import Host
from src.domain.enums.account_status import EAccountStatus
from src.domain.value_objects.address import Address
from src.domain.value_objects.email import Email
from src.domain.value_objects.phone import Phone


@pytest.fixture
def host() -> Generator[Host, None, None]:
    host = Host(
        name="Daniel",
        email=Email("testemail@gmail.com"),
        phone_number=Phone("+5545999999999"),
        address=Address(
            street="Rua da minha casa",
            city="Curiticity",
            state="Paraná",
            country="Brazil",
            zip_code="12301231",
        ),
        bio="Mussum Ipsum, cacilds vidis litro abertis.",
        profile_picture="/id/1238175891251u.jpg",
    )
    host.update_rating(5)
    yield host
    del host


class TestHost:

    def test_entity_initialization(self, host: Host):
        assert host is not None
        assert host.name == "Daniel"

    def test_should_update_rating_when_update_rating_is_called(self, host: Host):
        new_rating = 4.8

        host.update_rating(new_rating)
        assert host.rating == new_rating

    def test_should_an_error_when_sending_a_rating_outside_the_limits(self, host: Host):

        # Arrange
        valid_rating = 4.5
        new_rating_outside_limit = 5.9
        host.update_rating(valid_rating)

        # Act / Assert
        with pytest.raises(ValueError) as error:
            host.update_rating(new_rating_outside_limit)
            assert error.value == "Rating must be between 0 and 5"

    def test_should_an_error_when_sending_a_invalid_rating_value(self, host: Host):
        # Arrange
        invalid_rating = 12.4

        # Act / Assert
        with pytest.raises(ValueError) as error:
            host.update_rating(invalid_rating)
            assert error.value == "Rating must be between 0 and 5"

    def test_should_update_account_status_to_active_when_activate_is_called(self, host: Host):
        # Act
        host.activate()

        # Assert
        assert host.account_status == EAccountStatus.Active

    def test_should_update_account_status_to_permanently_banned_when_ban_is_called(
        self, host: Host
    ):
        # Arrange / Act
        host.ban()

        # Assert
        assert host.account_status == EAccountStatus.PermanentlyBanned

    def test_should_error_when_activate_is_called_on_permanently_banned_account(
        self,
        host: Host,
    ):
        # Arrange
        host.ban()

        # Act / Assert
        with pytest.raises(ValueError) as error:
            host.activate()
            assert error.value == "A permanently banned user cannot be activated."

    def test_should_update_account_status_to_deactivated_when_deactivate_is_called(
        self, host: Host
    ):
        # Arrange / Act
        host.deactivate()

        # Assert
        assert host.account_status == EAccountStatus.Deactivated
