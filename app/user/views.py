"""
Views for the user API
"""
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """
    Create a new user in the system

    Parameters
    ----------
    generics : _type_
        _description_
    """
    serializer_class = UserSerializer