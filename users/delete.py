from views.util import show_title
from inputs.delete import get_user_data_for_delete_it
from connection import UsersInformation

def delete_user() -> None:
    show_title("Delete User")

    user_id = get_user_data_for_delete_it()

    if not isinstance(user_id, str):
        return (user_id, "El usuario esta vacio!!")

    confirmation = input("\n⚪ Deseas continuar? Y[Si] N[No] ")
    if confirmation.strip().upper() == "N":
        return (user_id, "Se cancela por confirmacion negativa")

    db = UsersInformation()
    db.delete(user_id)
    del db

    input("\n✅ Eliminado con exito! Pulsa cualquier tecla para continuar. ✅\n")
    return (user_id, "Usuario creado con exito!")


