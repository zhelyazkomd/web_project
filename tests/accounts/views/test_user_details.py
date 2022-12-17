from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from tests.common.base_test import BaseTestCase

UserModel = get_user_model()


class UserDetailsViewTests(BaseTestCase):
    USER_DATA = {
        'email': 'Zhelyazko@dimitrov.com',
        'password': 'Sad2@sad_!',
    }

    def test_user_details__when_user_is_owner_expect_true(self):
        user = self.create_and_login_user(self.USER_DATA)
        response = self.client.get(reverse_lazy('details profile', kwargs={'pk': user.pk}))
        self.assertTrue(response.context['request_user_email'])

    def test_user_details__when_user_is_not_empty_full_name_expect_true(self):
        user = self.create_and_login_user(self.USER_DATA)
        response = self.client.get(reverse_lazy('details profile', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['request_user_full_name'])
