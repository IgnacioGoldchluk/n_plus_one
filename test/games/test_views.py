import pytest


@pytest.mark.django_db
class TestPlayerView:
    def test_player_view_lists_players(
        self, api_client, player_factory, play_time_factory
    ):
        p1 = player_factory()
        p1_played = [play_time_factory(player=p1).game.title for _ in range(3)]

        p2 = player_factory()
        p2_played = [play_time_factory(player=p2).game.title for _ in range(3)]

        response = api_client.get("/games/players", format="json").json()
        player_data = next(r for r in response if r["name"] == p1.name)

        playtimes_titles = [p["game"]["title"] for p in player_data["playtimes"]]
        assert all(played in playtimes_titles for played in p1_played)

        player2_data = next(r for r in response if r["name"] == p2.name)
        playtimes_titles = [p["game"]["title"] for p in player2_data["playtimes"]]
        assert all(played in playtimes_titles for played in p2_played)

    def test_player_list_num_queries(
        self,
        api_client,
        player_factory,
        play_time_factory,
        django_assert_max_num_queries,
    ):
        for _ in range(20):
            player = player_factory()
            for _ in range(20):
                play_time_factory(player=player)

        with django_assert_max_num_queries(2):
            api_client.get("/games/players", format="json").json()
