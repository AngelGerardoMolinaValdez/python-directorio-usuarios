from errors.users.query import *


def get_information_from_user_query() -> tuple[str, str] | tuple[Exception, str]:
    prefix_emoji : str = "⚪"


    user_identifier : str = input(f"{prefix_emoji} Nombre o ID: ")
    if user_identifier == "":
        return (UserIdentifierEmpty, "No se especifico el tipo de busqueda")


    query_type = "name"
    if user_identifier.isdigit():
        query_type = "id"
    
    return (user_identifier, query_type)
