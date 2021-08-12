from django.urls import reverse

from sell_your_phone.phones.models import Phone, Like
from tests.base.mixins import PhoneTestUtils, UserTestUtils
from tests.base.tests import SellYourPhoneTestCase


class PhoneDetailsTest(PhoneTestUtils, UserTestUtils, SellYourPhoneTestCase):
    def test_get_phone_details__when_phone_exists_and_is_owner__should_return_details_for_owner(self):
        self.client.force_login(self.user)
        phone = self.create_phone(
            brand='Test',
            phone_model=Phone.BRAND_CHOICE_SAMSUNG,
            year=5,
            description='desc',
            memory=64,
            price=200,
            contact_number=+35912345678,
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('phone details', kwargs={
            'pk': phone.id,
        }))

        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_get_phone_details__when_phone_exists_and_not_owner_and_not_liked__should_return_details_for_not_owner(self):
        self.client.force_login(self.user)
        phone_seller = self.create_user(email='random@abv.bg', password='12345qwe')
        phone = self.create_phone(
            brand='Test',
            phone_model=Phone.BRAND_CHOICE_SAMSUNG,
            year=5,
            description='desc',
            memory=64,
            price=200,
            contact_number=+35912345678,
            image='path/to/image.png',
            user=phone_seller,
        )

        response = self.client.get(reverse('phone details', kwargs={
            'pk': phone.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_get_phone_details__when_phone_exists_and_not_owner_and_liked__should_return_details_for_not_owner(self):
        self.client.force_login(self.user)
        phone_seller = self.create_user(email='random@abv.bg', password='12345qwe')
        phone = self.create_phone_with_like(
            like_user=self.user,
            brand='Test',
            phone_model=Phone.BRAND_CHOICE_SAMSUNG,
            year=5,
            description='desc',
            memory=64,
            price=200,
            contact_number=+35912345678,
            image='path/to/image.png',
            user=phone_seller,
        )

        response = self.client.get(reverse('phone details', kwargs={
            'pk': phone.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])
