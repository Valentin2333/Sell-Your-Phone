from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator

UserModel = get_user_model()


class Phone(models.Model):
    BRAND_CHOICE_APPLE = 'Apple'
    BRAND_CHOICE_SAMSUNG = 'Samsung'
    BRAND_CHOICE_HUAWEI = 'Huawei'
    BRAND_CHOICE_XIAOMI = 'Xiaomi'
    BRAND_CHOICE_ONEPLUS = 'One Plus'
    BRAND_CHOICE_GOOGLE = 'Google'
    BRAND_CHOICE_NOKIA = 'Nokia'

    BRAND_CHOICES = (
        (BRAND_CHOICE_APPLE, 'Apple'),
        (BRAND_CHOICE_SAMSUNG, 'Samsung'),
        (BRAND_CHOICE_HUAWEI, 'Huawei'),
        (BRAND_CHOICE_XIAOMI, 'Xiaomi'),
        (BRAND_CHOICE_ONEPLUS, 'One Plus'),
        (BRAND_CHOICE_GOOGLE, 'Google'),
        (BRAND_CHOICE_NOKIA, 'Nokia'),
    )

    brand = models.CharField(max_length=8, choices=BRAND_CHOICES)
    phone_model = models.CharField(max_length=12)
    year = models.PositiveIntegerField()
    description = models.TextField()
    memory = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    contact_number = models.CharField(validators=[phone_number_regex], max_length=16)
    image = models.ImageField(
        upload_to='phones',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Comment(models.Model):
    phone = models.ForeignKey(
        Phone,
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=50)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    phone = models.ForeignKey(
        Phone,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
