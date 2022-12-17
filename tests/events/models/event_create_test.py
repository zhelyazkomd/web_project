from tests.common.base_test import BaseTestCase
from web_project.events.models import Event


class EventModelsTests(BaseTestCase):
    USER_DATA = {
        'email': 'Zhelyazko@dimitrov.com',
        'password': 'Sad2@sad_!',
    }

    def test_create_event_by_current_user__expect_true(self):
        user = self.create_and_login_user(self.USER_DATA)
        create_event = self.create_event(user.pk)

        event = Event.objects.filter(event_name=create_event.event_name).get()

        self.assertTrue(event)


