import pytest
from django.db.utils import IntegrityError

from games.models import Game, Player, PlayTime


@pytest.mark.django_db
class TestGame:
    def test_creates_game(self):
        game = Game.objects.create(title="Deus Ex")
        assert game.title == "Deus Ex"

    def test_fails_to_create_game_with_no_title(self):
        with pytest.raises(IntegrityError):
            Game.objects.create(title=None)


@pytest.mark.django_db
class TestPlayer:
    def test_creates_player(self):
        player = Player.objects.create(name="player")
        assert player.name == "player"

    def test_fails_to_create_player_with_empty_name(self):
        with pytest.raises(IntegrityError):
            Player.objects.create(name=None)

    def test_fails_if_duplicate_player_name(self):
        dup_name = "player_name"
        p1 = Player.objects.create(name=dup_name)
        with pytest.raises(IntegrityError):
            Player.objects.create(name=dup_name)


@pytest.mark.django_db
class TestPlayTime:
    def test_creates_playtime_with_game_and_player(self, player_factory, game_factory):
        play_time = PlayTime.objects.create(
            player=player_factory(),
            game=game_factory(),
            hours_played=5,
        )

        assert play_time.hours_played == 5
        assert play_time.player is not None
        assert play_time.game is not None
