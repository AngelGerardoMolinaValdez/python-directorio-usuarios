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

from inputs.query import get_information_from_user_query
from errors.users.query import *


class TestGetInformationFromUserQuery(TestCase):

    def test_empty_identifier(self):
        with patch('builtins.input', return_value = ""):
            response, type = get_information_from_user_query()

            self.assertEqual(response, UserIdentifierEmpty)


    def test_identifier_by_id(self):
        with patch('builtins.input', return_value = "23"):
            response, type = get_information_from_user_query()

            self.assertEqual(type, "id")


    def test_identifier_by_name(self):
        with patch('builtins.input', return_value = "angel"):
            response, type = get_information_from_user_query()

            self.assertEqual(type, "name")


if __name__ == "__main__":
    main()
