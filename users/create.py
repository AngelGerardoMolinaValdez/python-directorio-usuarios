from views.util import show_title
from inputs.create import get_information_from_new_user
from connection import UsersInformation

def create_user() -> None:
    show_title("Create User")

    data_from_user, message = get_information_from_new_user()

    if not isinstance(data_from_user, dict):
        return (data_from_user, message)

    db = UsersInformation()
    db.create(**data_from_user)
    del db
    return (data_from_user, "Usuario creado con exito!")


