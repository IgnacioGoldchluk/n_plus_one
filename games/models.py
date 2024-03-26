from django.db import models
from .managers import PlayerQuerySet, PlayTimesQuerySet


class Game(models.Model):
    title = models.CharField(max_length=250, null=False)


class Player(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)
    objects = PlayerQuerySet.as_manager()


class PlayTime(models.Model):
    player = models.ForeignKey(
        Player, related_name="playtimes", on_delete=models.CASCADE
    )
    game = models.ForeignKey(Game, related_name="playtimes", on_delete=models.CASCADE)

    hours_played = models.PositiveIntegerField()

    objects = PlayTimesQuerySet.as_manager()
