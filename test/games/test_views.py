import pytest


@pytest.mark.django_db
class TestPlayerView:
    def test_player_view_lists_players(
        self, api_client, player_factory, play_time_factory
    ):
        [p1, p2] = sorted(player_factory.create_batch(2), key=lambda player: player.name)
        p1_playtimes = play_time_factory.create_batch(3, player=p1)
        p2_playtimes = play_time_factory.create_batch(3, player=p2)

        [p1_data, p2_data] = api_client.get("/games/players", format="json").json()
        assert p1_data["name"] == p1.name
        assert p2_data["name"] == p2.name

        p1_resp_titles = {playtime["game"]["title"] for playtime in p1_data["playtimes"]}
        p1_data_titles = {playtime.game.title for playtime in p1_playtimes}
        assert p1_resp_titles == p1_data_titles

        p2_resp_titles = {playtime["game"]["title"] for playtime in p2_data["playtimes"]}
        p2_data_titles = {playtime.game.title for playtime in p2_playtimes}
        assert p2_resp_titles == p2_data_titles

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
