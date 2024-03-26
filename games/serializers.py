from rest_framework import serializers

from .models import Game, Player, PlayTime


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["title"]


class PlayTimeSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta:
        model = PlayTime
        fields = ["hours_played", "game"]


class PlayerSerializer(serializers.ModelSerializer):
    playtimes = PlayTimeSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ["name", "playtimes"]
