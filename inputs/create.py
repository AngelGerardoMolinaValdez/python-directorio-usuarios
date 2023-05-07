from errors.users.create import *
from re import match


def get_information_from_new_user() -> dict[str, str]:
    prefix_emoji : str = "⚪"
    pattern_valid_email : str = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


    name : str = input(f"{prefix_emoji} Nombre completo: ")
    if name == "":
        return (UserNameEmpty, "Nombre de usuario vacio")

    if name.isdigit():
        return (UserNameIsOnlyNumbers, "Nombre de usuario contiene numeros")


    phone : str = input(f"{prefix_emoji} Numero telefonico: ")
    if phone == "":
        return (PhoneEmpty, "numero de telefono vacio")

    if not phone.isdigit():
        return (PhoneNumberDoesNotContainOnlyNumbers, "Numero de telefono contiene letras")


    email : str = input(f"{prefix_emoji} Correo Electronico: ")
    if email == "":
        return (EmailEmpty, "Correo vacio")

    if not match(pattern_valid_email, email):
        return (EmailNotValid, "Correo no valido")


    address : str = input(f"{prefix_emoji} Direccion: ")
    if address == "":
        return (AddressEmpty, "Direccion vacia")


    new_user_information : dict[str, str] = {
        "name" : name,
        "phone" : phone,
        "email" : email,
        "address" : address
    }

    return (new_user_information, "Informacion obtenida correctamente!")
