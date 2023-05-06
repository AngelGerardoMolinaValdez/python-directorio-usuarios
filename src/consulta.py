from prettytable import PrettyTable
from vistas import mostrar_titulo
from log import NivelesLog
from database import repository
from errores import UsuarioNoExiste, NombreDeUsuarioVacio



def consulta() -> None:
    nombre_usuario : str = input("💬 Cual es el nombre del usuario? ")

    datos_de_usuario = repository.get(nombre_usuario)

    if datos_de_usuario == "":
        raise NombreDeUsuarioVacio("No fue especificado ningun nombre")

    if datos_de_usuario is None:
        raise UsuarioNoExiste(f"El usuario '{nombre_usuario}' no existe.")

    tabla_resultados : PrettyTable = PrettyTable()
    tabla_resultados.field_names = ["NOMBRE", "TELEFONO"]

    resultados = map(
        lambda datos: [nombre_usuario, datos[1]],
        datos_de_usuario.items())

    tabla_resultados.add_rows(resultados)
    print(tabla_resultados, end="\n" * 2)

    emoji_ok = NivelesLog.INFO.emoji()
    input(f"{emoji_ok} Pulsa enter para continuar! {emoji_ok}")


def consulta_general() -> None:
    mostrar_titulo("Consulta General")

    tabla_resultados : PrettyTable = PrettyTable()
    tabla_resultados.field_names = ["NOMBRE", "TELEFONO"]

    resultados = map(
        lambda datos: [datos[0], datos[1]["telefono"]],
        repository.items())

    tabla_resultados.add_rows(resultados)
    print(tabla_resultados, end="\n" * 2)

    emoji_ok = NivelesLog.INFO.emoji()
    input(f"{emoji_ok} Pulsa enter para continuar! {emoji_ok}")

