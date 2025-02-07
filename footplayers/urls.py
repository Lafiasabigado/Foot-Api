from tkinter.font import names

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tutorial.urls import router
from footplayers import settings
from fplayers.views import PlayerViewset

router = DefaultRouter()
router.register(r'player',PlayerViewset,basename="player")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth",include('rest_framework.urls')),
    path('',include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
