"""
Serializer for user profile.
"""
from rest_framework import serializers
from core.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for profile fields."""
    class Meta:
        model = Profile
        fields = '__all__'
