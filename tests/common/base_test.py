from django.contrib.auth import get_user_model
from django.test import TestCase

from web_project.accounts.models import Profile
from web_project.common.models import RegisterEvent
from web_project.events.models import Event

UserModel = get_user_model()


class BaseTestCase(TestCase):

    def create_and_login_user(self, credentials):
        user = UserModel.objects.create_user(**credentials)
        profile = Profile.objects.create(
            first_name='Zhelyazko',
            last_name='Dimitrov',
            age=26,
            user_id=user.pk,
        )
        self.client.login(**credentials)
        return user

    @staticmethod
    def create_event(user_id):
        event = Event(
            event_name="Test",
            event_date='2023-10-10 10:00:00',
            type_of_event='online',
            capacity=15,
            description='AA' * 20,
            user_id=user_id,
        )
        event.full_clean()
        event.save()

        return event

    @staticmethod
    def register_user_for_event(user_id, event_id):
        return RegisterEvent.objects.create(event_id=event_id, user_id=user_id)
