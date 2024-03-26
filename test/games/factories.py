import factory


class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "games.Player"

    name = factory.Faker("user_name")


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "games.Game"

    title = factory.Faker("sentence", nb_words=3)


class PlayTimeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "games.PlayTime"

    hours_played = factory.Faker("pyint", min_value=1, max_value=9999)
    game = factory.SubFactory(GameFactory)
    player = factory.SubFactory(PlayerFactory)
