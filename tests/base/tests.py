from django.contrib.auth import get_user_model
from django.test import TestCase, Client

UserModel = get_user_model()


class SellYourPhoneTestCase(TestCase):
    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='valentin@abv.bg', password='12345qwe')
