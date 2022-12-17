from tests.common.base_test import BaseTestCase
from web_project.common.models import RegisterEvent
from web_project.events.models import Event


class RegisterUserEventView(BaseTestCase):
    USER_DATA = {
        'email': 'Zhelyazko@dimitrov.com',
        'password': 'Sad2@sad_!',
    }

    def test_register_current_user_for_event__expect_true(self):
        user = self.create_and_login_user(self.USER_DATA)
        create_event = self.create_event(user.pk)

        user_id = user.pk
        event_id = create_event.pk

        self.register_user_for_event(user_id, event_id)

        response = RegisterEvent.objects.filter(event_id=event_id, user_id=user_id).get()

        self.assertTrue(response)

    def test_unregister_current_user_for_event__expect_true(self):
        user = self.create_and_login_user(self.USER_DATA)
        create_event = self.create_event(user.pk)

        user_id = user.pk
        event_id = create_event.pk

        self.register_user_for_event(user_id, event_id)

        response = RegisterEvent.objects.filter(event_id=event_id, user_id=user_id).get()
        response.delete()

        self.assertNotEqual(response, True)
