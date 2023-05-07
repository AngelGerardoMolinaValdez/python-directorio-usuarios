import sys
import os
from unittest import TestCase, main
from unittest.mock import patch

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from inputs.create import get_information_from_new_user
from errors.users.create import *


class TestGetInformationFromNewUser(TestCase):

    def test_valid_response(self):
        with patch(
                'builtins.input',
                side_effect=[
                    'Angel Molina', '1234567890', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_new_user()

            self.assertIsInstance(response, dict)


    def test_empty_name(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '', '1234567890', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_new_user()

            self.assertEqual(response, UserNameEmpty)


    def test_not_valid_name(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '656546544', '1234567890', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_new_user()

            self.assertEqual(response, UserNameIsOnlyNumbers)


    def test_empty_phone(self):
        with patch(
                'builtins.input',
                side_effect=[
                    'Angel', '', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_new_user()

            self.assertEqual(response, PhoneEmpty)


    def test_not_valid_phone(self):
        with patch(
                'builtins.input',
                side_effect=[
                    'Angel', '56565bye', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_new_user()

            self.assertEqual(response, PhoneNumberDoesNotContainOnlyNumbers)


    def test_empty_email(self):
        with patch(
                'builtins.input',
                side_effect=[
                    'Angel', '6565656565', '', '123 Main St'
                ]
        ):
            response, message = get_information_from_new_user()

            self.assertEqual(response, EmailEmpty)


    def test_not_valid_email(self):
        with patch(
                'builtins.input',
                side_effect=[
                    'Angel', '6565656565', 'angel.com.mx', '123 Main St'
                ]
        ):
            response, message = get_information_from_new_user()

            self.assertEqual(response, EmailNotValid)


    def test_empty_address(self):
        with patch(
                'builtins.input',
                side_effect=[
                    'Angel', '6565656565', 'angel@gmail.com', ''
                ]
        ):
            response, message = get_information_from_new_user()

            self.assertEqual(response, AddressEmpty)


if __name__ == "__main__":
    main()
