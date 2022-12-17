from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.common.base_test import BaseTestCase

UserModel = get_user_model()


class ProfileCreateViewTests(BaseTestCase):
    def test_create_profile__when_user_is_logged_in__expect_to_create_profile(self):
        credentials = {
            'email': 'zhelyzko@dimitrov.com',
            'password': 'asdgdsf@@asdas2!',
        }

        self.create_and_login_user(credentials)

        response = self.client.post(
            reverse('sign up'),
            data=credentials,
        )

        created_profile = UserModel.objects.filter(email=credentials['email']).get()

        self.assertIsNotNone(created_profile)
        self.assertEqual(200, response.status_code)
