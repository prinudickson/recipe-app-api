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
    def create_user(self, email, password=None, **extra_fields):
        """
        Create, Save and return a new user

        Parameters
        ----------
        email : text
            _description_
        password : text, optional
            _description_, by default None
        """
        if not email:
            raise ValueError('User must have email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Creates and returns a superuser

        Parameters
        ----------
        email : _type_
            _description_
        password : _type_
            _description_
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

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
