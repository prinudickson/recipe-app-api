"""
Serializers for the user API View
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user object

    Parameters
    ----------
    serializers : _type_
        _description_
    """

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """
        create and return a user with encrypted password

        Parameters
        ----------
        validated_data : _type_
            _description_
        """
        return get_user_model().objects.create_user(**validated_data)