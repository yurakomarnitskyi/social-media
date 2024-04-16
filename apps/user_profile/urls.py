"""
Routing for user profile.
"""
from django.urls import path, include
from user_profile import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user_profile', views.ProfileViews)


app_name = 'user_profile'


urlpatterns = [
    path('', include(router.urls))
]