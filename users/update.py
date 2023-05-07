from views.util import show_title
from inputs.update import get_information_from_update_user_data
from errors.users.update import *
from connection import UsersInformation

def update_user_information() -> None:
    show_title("Update User Information")

    user_data, message = get_information_from_update_user_data()

    if not isinstance(user_data, dict):
        return (user_data, "El usuario esta vacio!!")

    user_id = message

    confirmation = input("\n⚪ Deseas continuar? Y[Si] N[No] ")
    if confirmation.strip().upper() == "N":
        return (user_data, "Se cancela por confirmacion negativa")

    db = UsersInformation()
    values = db.get(user_id)

    if len(values) < 1:
        return (
            UserDoesNotExist,
            "No existe el usuario especificado con el id")

    values = db.update(user_id, **user_data)
    del db

    input("\n✅ Modificado con exito! Pulsa cualquier tecla para continuar. ✅\n")
    return (user_data, "Usuario modificado con exito!")
