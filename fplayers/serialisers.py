from rest_framework import serializers,routers

from fplayers.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    salary = serializers.IntegerField(min_value=0)

    class Meta:
        model = Player
        fields = '__all__'
