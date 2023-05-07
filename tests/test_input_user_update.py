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

from inputs.update import get_information_from_update_user_data
from errors.users.create import *
from errors.users.update import *


class TestUpdateInformationFromUser(TestCase):
    def test_valid_values(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '0', 'Angel Molina', '1234567890', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_update_user_data()

            self.assertIsInstance(response, dict)


    def test_empty_name(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '0', '', '1234567890', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_update_user_data()

            self.assertEqual(response, UserNameEmpty)


    def test_not_valid_name(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '0', '656546544', '1234567890', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_update_user_data()

            self.assertEqual(response, UserNameIsOnlyNumbers)


    def test_empty_id(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '', '656546544', '1234567890', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_update_user_data()

            self.assertEqual(response, UserIDEmpty)


    def test_not_valid_id(self):
        with patch(
                'builtins.input',
                side_effect=[
                    'asdfa', '656546544', '1234567890', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_update_user_data()

            self.assertEqual(response, UserIDShouldBeANumber)


    def test_empty_phone(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '0', 'Angel', '', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_update_user_data()

            self.assertEqual(response, PhoneEmpty)


    def test_not_valid_phone(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '0', 'Angel', '56565bye', 'test@example.com', '123 Main St'
                ]
        ):
            response, message = get_information_from_update_user_data()

            self.assertEqual(response, PhoneNumberDoesNotContainOnlyNumbers)


    def test_empty_email(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '0', 'Angel', '6565656565', '', '123 Main St'
                ]
        ):
            response, message = get_information_from_update_user_data()

            self.assertEqual(response, EmailEmpty)


    def test_not_valid_email(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '0', 'Angel', '6565656565', 'angel.com.mx', '123 Main St'
                ]
        ):
            response, message = get_information_from_update_user_data()

            self.assertEqual(response, EmailNotValid)


    def test_empty_address(self):
        with patch(
                'builtins.input',
                side_effect=[
                    '0', 'Angel', '6565656565', 'angel@gmail.com', ''
                ]
        ):
            response, message = get_information_from_update_user_data()

            self.assertEqual(response, AddressEmpty)


if __name__ == "__main__":
    main()
