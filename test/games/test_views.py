import pytest


@pytest.mark.django_db
class TestPlayerView:
    def test_player_view_lists_players(
        self, api_client, player_factory, play_time_factory
    ):
        [p1, p2] = player_factory.create_batch(2)
        p1_played = [play_time_factory(player=p1).game.title for _ in range(3)]
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
        players = player_factory.create_batch(20)
        for player in players:
            play_time_factory.create_batch(20, player=player)

        with django_assert_max_num_queries(2):
            api_client.get("/games/players", format="json").json()
