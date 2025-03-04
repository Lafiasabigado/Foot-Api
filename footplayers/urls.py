from tkinter.font import names

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tutorial.urls import router
from footplayers import settings
from fplayers.views import PlayerViewset
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

router = DefaultRouter()
router.register(r'',PlayerViewset,basename="player")

schema_view = get_schema_view(
    openapi.Info(
        title="Football Players API",
        default_version="v1",
        description="Une API qui fournit des informations sur les joueurs de football",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    path("accounts/login", auth_views.LoginView.as_view(), name="login"),
    path("api-auth",include('rest_framework.urls')),
    path('player/',include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
