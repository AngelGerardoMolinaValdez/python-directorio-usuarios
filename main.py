import os

from views.menu import show_menu
from views.util import show_goodbye_message
from views.errors import show_error_message

from inputs.user import get_user_response

from errors.inputs import *
from errors.connection import *

from model import BusinessOptions
from connection import UsersInformation

from users.create import create_user
from users.query import get_user_information, \
     get_information_from_all_users
from users.delete import delete_user
from users.update import update_user_information


connection_execution = UsersInformation()
status_connection = connection_execution.start("directory.db")
if isinstance(status_connection, DataBaseFileNotExist):
     show_error_message("La base de datos no existe! Configurar una nueva!")
     exit()


while True:
     try:
          show_menu()

          user_response : int | Exception = get_user_response()
          match user_response:
               case BusinessOptions.CREATE.value:
                    log_user_creation, message = create_user()
                    if not isinstance(log_user_creation, dict):
                         raise log_user_creation(message)


               case BusinessOptions.DELETE.value:
                    log_query, message = delete_user()
                    if not isinstance(log_query, str):
                         log_query(message)


               case BusinessOptions.UPDATE.value:
                    log_query, message = update_user_information()
                    if not isinstance(log_query, dict):
                         log_query(message)


               case BusinessOptions.QUERY.value:
                    log_query, message = get_user_information()
                    if not isinstance(log_query, str):
                         log_query(message)


               case BusinessOptions.GENERAL_QUERY.value:
                    get_information_from_all_users()


               # case BusinessOptions.REPORT.value:
               #      print("report")


               # case BusinessOptions.GENERAL_REPORT.value:
               #      print("general report")


               case ResponseShouldBeANumberNotLetter():
                    raise ResponseShouldBeANumberNotLetter("La respuesta no puede ser una letra!!")


               case ResponseOutOfRange():
                    raise ResponseOutOfRange("La respuesta esta fuera del rango!!")


               case ClearScreen():
                    os.system("cls")


               case StopExecution():
                    UsersInformation().close()
                    show_goodbye_message()
                    exit()


     except Exception as e:
          show_error_message(e)
          input("🛑 Pulsa enter para continuar! 🛑\n")

