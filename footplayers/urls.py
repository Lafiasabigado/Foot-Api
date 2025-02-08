from tkinter.font import names

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tutorial.urls import router
from footplayers import settings
from fplayers.views import PlayerViewset
from django.urls import path,re_path
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

router = DefaultRouter()
router.register(r'player',PlayerViewset,basename="player")

schema_view = get_schema_view(
    openapi.Info(
        title="Football Players API",
        default_version="v1",
        description="Une API pour gérer des joueurs de football",
    ),
    public=True,
    permission_classes=(AllowAny),
)



urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    path("api-auth",include('rest_framework.urls')),
    path('',include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
