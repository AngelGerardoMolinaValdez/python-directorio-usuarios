from database import repository
from errores import NombreDeUsuarioNoPuedeSerNumero, UsuarioRegistrado, NumeroTelefonicoNoTieneSoloNumeros, NumeroTelefonicoNoTiene10Digitos
from log import NivelesLog
from vistas import mostrar_titulo, mostrar_log


def alta() -> None:
    mostrar_titulo("Alta")

    nombre = input("💬 Cual es el nombre? ")
    print()

    if nombre.isdigit():
        raise NombreDeUsuarioNoPuedeSerNumero(f"El nombre {nombre} no es valido " +
                                             "ya que el nombre no puede ser solo numeros")

    if nombre in repository:
        raise UsuarioRegistrado(f"El usuario {nombre} ya esta registrado")

    telefono = input("💬 Cual es el numero telefonico(10 digitos)? ")
    

    if not telefono.isdigit():
        raise NumeroTelefonicoNoTieneSoloNumeros(
            f"El numero telefonico '{telefono}' tiene letras, verifique el contenido")

    if 0 <= len(telefono) < 10:
        raise NumeroTelefonicoNoTiene10Digitos(
            f"El numero '{telefono}' tiene {len(telefono)} y no 10 digitos como deberia ser.")

    repository[nombre] = {"telefono" : telefono}
    mostrar_log(f"Usuario {nombre} agregado!", NivelesLog.OK)
