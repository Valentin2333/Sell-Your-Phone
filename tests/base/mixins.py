from django.contrib.auth import get_user_model

from sell_your_phone.phones.models import Phone, Like

UserModel = get_user_model()


class PhoneTestUtils:
    def create_phone(self, **kwargs):
        return Phone.objects.create(**kwargs)

    def create_phone_with_like(self, like_user, **kwargs):
        phone = self.create_phone(**kwargs)
        Like.objects.create(
            phone=phone,
            user=like_user,
        )
        return phone


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)
