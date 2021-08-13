import random
from os.path import join

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from sell_your_phone.phones.models import Phone
from sell_your_phone.accounts.models import Profile
from tests.base.tests import SellYourPhoneTestCase


class ProfileDetailsTest(SellYourPhoneTestCase):
    def test_get_details__when_user_logged_in_without_phones__should_get_details(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['phones']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_get_details__when_user_logged_in_with_phones__should_get_details(self):
        phone = Phone.objects.create(
            brand=Phone.BRAND_CHOICE_SAMSUNG,
            phone_model='Test model',
            year=5,
            description='desc',
            memory=64,
            price=200,
            contact_number=+35912345678,
            image='path/to/image.png',
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([phone], list(response.context['phones']))

    def test_post_details__when_user_logged_in_without_image_and_changes_image__should_change_image(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test_image.webp')

        file_name = f'{random.randint(1, 10000)}-test_image.webp'
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpeg')

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': file,
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)
        self.assertTrue(str(profile.profile_image).endswith(file_name))


def test_post_details__when_user_logged_in_with_image_and_changes_image_should_change_image(self):
        path_to_image = 'path/to/image.png'
        profile = Profile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': path_to_image
        })

        self.assertEqual(302, response.status_code)
