"""
Database Models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):
    """
    Manager for users

    Parameters
    ----------
    BaseUserManager : _type_
        _description_
    """
    def create_user(self, email, password=None, **extra_field):
        """
        Create, Save and return a new user

        Parameters
        ----------
        email : _type_
            _description_
        password : _type_, optional
            _description_, by default None
        """
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save(self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the System

    Parameters
    ----------
    AbstractBaseUser : _type_
        _description_
    PermissionsMixin : _type_
        _description_
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'