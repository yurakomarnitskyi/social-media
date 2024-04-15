"""
Rout config.
"""
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shema/', SpectacularAPIView.as_view(), name='api-shema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-shema'), name='api-docs',),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
]