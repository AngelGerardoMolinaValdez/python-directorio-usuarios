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

from inputs.delete import get_user_data_for_delete_it
from errors.users.delete import *


class TestDeleteUserFromDirectory(TestCase):


    def test_empty_id(self):
        with patch(
                'builtins.input',
                return_value=""
        ):
            response, message = get_user_data_for_delete_it()

            self.assertEqual(response, UserIDEmpty)


    def test_not_valid_id(self):
        with patch(
                'builtins.input',
                return_value="asdaf"
        ):
            response, message = get_user_data_for_delete_it()

            self.assertEqual(response, UserIDShouldBeANumber)


    def test_valid_id(self):
        with patch(
                'builtins.input',
                return_value="2"
        ):
            response, message = get_user_data_for_delete_it()

            self.assertEqual(response, "2")


if __name__ == "__main__":
    main()
