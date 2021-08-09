from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from sell_your_phone.accounts.managers import SellYourPhoneUserManager


class SellYourPhoneUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = SellYourPhoneUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        SellYourPhoneUser,
        on_delete=models.CASCADE,
        primary_key=False
    )


from .signals import *
