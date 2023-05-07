import unittest
from test_menu_options import TestGetUserResponse
from test_input_user_create import TestGetInformationFromNewUser
from test_input_user_update import TestUpdateInformationFromUser
from test_input_user_delete import TestDeleteUserFromDirectory
from test_input_user_query import TestGetInformationFromUserQuery

tests = [
    TestGetUserResponse,
    TestGetInformationFromNewUser,
    TestUpdateInformationFromUser,
    TestDeleteUserFromDirectory,
    TestGetInformationFromUserQuery
]

suite = unittest.TestSuite()

for test in tests:
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
