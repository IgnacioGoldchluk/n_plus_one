import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register
from test.games.factories import PlayerFactory, GameFactory, PlayTimeFactory


register(PlayerFactory)
register(GameFactory)
register(PlayTimeFactory)


@pytest.fixture
def api_client():
    return APIClient()
