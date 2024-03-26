from rest_framework import generics

from .models import Player
from .serializers import PlayerSerializer


class PlayerView(generics.ListAPIView):
    queryset = Player.objects.with_playtimes()
    serializer_class = PlayerSerializer
