from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from web_project.accounts.models import Profile

UserModel = get_user_model()


class ProfileModelTests(TestCase):

    def test_profile_save__when_first_name_is_valid__expect_correct_result(self):
        email = 'ZZZZZZ@sad.bg'
        password = 'asdasd@212..sadAASD'
        user = UserModel(
            email=email,
            password=password,

        )

        user.full_clean()
        user.save()

        first_name = 'Zhelyazko'
        last_name = 'Dimitrov'
        age = 26
        user_id = user.pk
        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            age=age,
            user_id=user_id,
        )

        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_first_name_is_not_valid__expect_correct_result(self):
        email = 'ZZZZZZ@sad.bg'
        password = 'asdasd@212..sadAASD'
        user = UserModel(
            email=email,
            password=password,

        )

        user.full_clean()
        user.save()

        first_name = 'Zhelyazko96'
        last_name = 'Dimitrov'
        age = 26
        user_id = user.pk
        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            age=age,
            user_id=user_id,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)
