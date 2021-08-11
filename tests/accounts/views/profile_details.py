from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from sell_your_phone.phones.models import Phone
from sell_your_phone.accounts.models import Profile

UserModel = get_user_model()


class SellYourPhoneTestCase(TestCase):
    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')


class ProfileDetailsTest(SellYourPhoneTestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='valentin@abv.bg', password='12345qwe')

    def test_get_details__when_user_logged_in_without_phones__should_get_details(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['phones']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_get_details__when_user_logged_in_with_phones__should_get_details(self):
        phone = Phone.objects.create(
            brand='Test',
            phone_model=Phone.BRAND_CHOICE_SAMSUNG,
            year=5,
            description='desc',
            memory=20,
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
        path_to_image = 'path/to/image.png'
        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': path_to_image
        })

        self.assertEqual(302, response.status_code)

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
