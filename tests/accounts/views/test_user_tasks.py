from django.urls import reverse

from sell_your_phone.accounts.models import SellYourPhoneUser, Profile
from tests.base.tests import SellYourPhoneTestCase
from tests.base.mixins import UserTestUtils


class UserTasksTest(UserTestUtils, SellYourPhoneTestCase):
    def test_register(self):
        new_user = self.create_user(email='random@abv.bg', password='12345qwe')

        response = self.client.post(reverse('register user'))

        self.assertEqual(200, response.status_code)

        user_exists = SellYourPhoneUser.objects.filter(
            id=new_user.id,
        ).exists()

        profile_exists = Profile.objects.filter(
            user_id=new_user.id,
        ).exists()

        self.assertTrue(user_exists, profile_exists)

    def test_login(self):
        response = self.client.post(reverse('log in user'))
        self.assertEqual(200, response.status_code)

    def test_logout(self):
        response = self.client.post(reverse('log out user'))
        self.assertEqual(302, response.status_code)