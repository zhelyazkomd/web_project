from django.core.exceptions import ValidationError

from web_project.core.parameters_validators import validate_is_letters
from django.test import TestCase


class LettersValidatorsTests(TestCase):
    def test_letters_validators__when_is_valid__expect_true(self):
        test_string = 'djangoweb'
        validate_is_letters(test_string)

    def test_letters_validators__when_is_not_valid_with_number__expect_false(self):
        with self.assertRaises(ValidationError) as context:
            test_string = 'djangoweb85'
            validate_is_letters(test_string)
        self.assertIsNotNone(context.exception)

    def test_letters_validators__when_is_not_valid_with_symbol__expect_false(self):
        with self.assertRaises(ValidationError) as context:
            test_string = 'djangoweb@'
            validate_is_letters(test_string)
        self.assertIsNotNone(context.exception)
