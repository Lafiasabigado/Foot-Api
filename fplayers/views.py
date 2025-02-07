from rest_framework import viewsets

from fplayers.models import Player
from fplayers.serialisers import PlayerSerializer


class PlayerViewset(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
