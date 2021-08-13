from sell_your_phone.phones.models import Phone, Comment
from tests.base.mixins import UserTestUtils, PhoneTestUtils
from tests.base.tests import SellYourPhoneTestCase


class CommentPhoneTests(PhoneTestUtils, UserTestUtils, SellYourPhoneTestCase):
    def test_comment_phone__when_is_not_owner__should_add_comment(self):
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

        comment = Comment(
            text='test comment',
            phone=phone,
            user=self.user,
        )
        comment.save()

        comment_exists = Comment.objects.filter(
            user_id=self.user.id,
            phone_id=phone.id,
        ).exists()

        self.assertTrue(comment_exists)
