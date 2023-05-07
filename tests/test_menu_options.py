from unittest import TestCase, main
from unittest.mock import patch
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from inputs.user import get_user_response
from errors.inputs import *
from model import *


class TestGetUserResponse(TestCase):

    def test_happy_path(self):
        """Prueba que se devuelve el número de respuesta válido cuando se ingresa una respuesta válida"""
        with patch('builtins.input', return_value=str(BusinessOptions.CREATE.value)):
            response = get_user_response()
            self.assertEqual(response, 2)

    def test_response_not_numeric(self):
        """Prueba que se devuelve una excepción `ResponseShouldBeANumberNotLetter` cuando el usuario ingresa una respuesta que no es un número"""
        with patch('builtins.input', return_value='abc'):
            response = get_user_response()
            self.assertIsInstance(
                response, ResponseShouldBeANumberNotLetter)

    def test_option_out_of_range(self):
        """Prueba que se devuelve una excepción `ResponseOutOfRange` cuando el usuario ingresa una respuesta que no está en el rango de opciones"""
        with patch('builtins.input', return_value='10'):
            response = get_user_response()
            self.assertIsInstance(
                response, ResponseOutOfRange)

    def test_stop_execution(self):
        """Prueba que se devuelve una excepción `StopExecution` cuando el usuario ingresa el número de opción para detener la ejecución"""
        with patch('builtins.input', return_value=str(UtilityOptions.CLOSE.value)):
            response = get_user_response()
            self.assertIsInstance(
                response, StopExecution)

    def test_clear_screen(self):
        """Prueba que se devuelve una excepción `ClearScreen` cuando el usuario ingresa el número de opción para limpiar la pantalla"""
        with patch('builtins.input', return_value=str(UtilityOptions.CLEAR.value)):
            response = get_user_response()
            self.assertIsInstance(
                response, ClearScreen)


if __name__ == "__main__":
    main()
