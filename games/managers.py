from django.db import models


class PlayTimesQuerySet(models.QuerySet):
    def with_game(self):
        return self.select_related("game")


class PlayerQuerySet(models.QuerySet):
    def with_playtimes(self):
        from .models import PlayTime

        return self.prefetch_related(
            models.Prefetch("playtimes", queryset=PlayTime.objects.with_game())
        )
