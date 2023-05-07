from errors.users.delete import *


def get_user_data_for_delete_it() -> tuple[str, str] | tuple[Exception, str]:
    prefix_emoji : str = "⚪"


    user_id : str = input(f"{prefix_emoji} ID: ")
    if user_id == "":
        return (UserIDEmpty,"ID vacio")

    if not user_id.isdigit():
        return (UserIDShouldBeANumber, "ID no valido contiene letras")

    return (user_id, "ID valido")
