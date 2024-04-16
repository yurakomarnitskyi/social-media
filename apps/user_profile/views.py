"""
Views logic for profile.
"""
from core.models import Profile
from user_profile.serializer import ProfileSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ProfileViews(viewsets.ModelViewSet):
   """Logic for user profile."""
   serializer_class = ProfileSerializer
   queryset = Profile.objects.all()