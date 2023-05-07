from prettytable import PrettyTable
from views.util import show_title
from inputs.query import get_information_from_user_query
from connection import UsersInformation


def get_user_information() -> tuple[str, str] | tuple[Exception, str]:
    show_title("User Query")

    user_identifier, query_type = get_information_from_user_query()
    if not isinstance(user_identifier, str):
        return (user_identifier, query_type)

    db = UsersInformation()
    user_values = db.get(user_identifier)
    del db

    if len(user_values) < 1:
        warning_emoji = "⚠"
        print(f"{warning_emoji} Sin coincidencias {warning_emoji}")
        return  (str, str)

    table_user = PrettyTable()
    table_user.field_names = ["ID", "NAME", "PHONE", "EMAIL", "ADDRESS"]
    table_user.add_rows(user_values)

    print("\n")
    print(table_user, end="\n\n")
    input("🟢 Presiona cualquier tecla para continuar🟢\n")

    return (user_identifier, "Usuario creado con exito!")


def get_information_from_all_users() -> None:
    show_title("Users Query")

    db = UsersInformation()
    users_values = db.get()
    del db

    if len(users_values) < 1:
        warning_emoji = "⚠"
        print(f"{warning_emoji} Sin coincidencias {warning_emoji}")
        return  (str, str)

    table_user = PrettyTable()
    table_user.field_names = ["ID", "NAME", "PHONE", "EMAIL", "ADDRESS"]
    table_user.add_rows(users_values)

    print(table_user, end="\n\n")
    input("🟢 Presiona cualquier tecla para continuar🟢\n")
