from rest_framework import serializers,routers

from fplayers.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["firstname","lastname","nationality","date_of_birthday","club",'image',"goals",
                  "assists","position"]
