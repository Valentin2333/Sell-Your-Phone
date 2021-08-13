from django.urls import reverse

from sell_your_phone.phones.models import Phone, Like
from tests.base.mixins import UserTestUtils, PhoneTestUtils
from tests.base.tests import SellYourPhoneTestCase


class LikePhoneTests(PhoneTestUtils, UserTestUtils, SellYourPhoneTestCase):
    def test_like_phone__when_phone_not_liked__should_create_like(self):
        self.client.force_login(self.user)
        phone_seller = self.create_user(email='random@abv.bg', password='12345qwe')
        phone = self.create_phone(
            brand=Phone.BRAND_CHOICE_SAMSUNG,
            phone_model='Test model',
            year=5,
            description='desc',
            memory=64,
            price=200,
            contact_number=+35912345678,
            image='path/to/image.png',
            user=phone_seller,
        )

        response = self.client.post(reverse('like phone', kwargs={
            'pk': phone.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            phone_id=phone.id,
        ).exists()

        self.assertTrue(like_exists)

    def test_like_phone__when_phone_already_liked__should_delete_like(self):
        self.client.force_login(self.user)
        phone_seller = self.create_user(email='random@abv.bg', password='12345qwe')
        phone = self.create_phone_with_like(
            like_user=self.user,
            brand=Phone.BRAND_CHOICE_SAMSUNG,
            phone_model='Test model',
            year=5,
            description='desc',
            memory=64,
            price=200,
            contact_number=+35912345678,
            image='path/to/image.png',
            user=phone_seller,
        )

        response = self.client.post(reverse('like phone', kwargs={
            'pk': phone.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            phone_id=phone.id,
        ).exists()

        self.assertFalse(like_exists)
