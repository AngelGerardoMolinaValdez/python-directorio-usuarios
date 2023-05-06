from vistas import mostrar_titulo, mostrar_log
from log import NivelesLog
from database import repository
from errores import UsuarioNoExiste, NombreDeUsuarioVacio


def modificacion() -> None:
    mostrar_titulo("Modificacion")

    nombre = input("💬 Cual es el nombre? ")
    print()
 
    datos_de_usuario = repository.get(nombre)

    if datos_de_usuario == "":
        raise NombreDeUsuarioVacio("No fue especificado ningun nombre")

    if datos_de_usuario is None:
        raise UsuarioNoExiste(f"El usuario '{nombre}' no existe.")

    for nombre_opcion, _ in datos_de_usuario.items():
        nuevo_valor = input(f"💬 Nuevo valor para {nombre_opcion}? ")

        if nuevo_valor == "":
            continue
        
        repository[nombre][nombre_opcion] = nuevo_valor

    mostrar_log(f"Usuario {nombre} modificado!", NivelesLog.OK)
