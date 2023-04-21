from prettytable import PrettyTable
from data import OpcionesDisponibles, Utilidades
from vistas import *


def mostrar_menu() -> None:
    """muestra las opciones disponibles en funcionamiento

    toma las opciones del objeto enum que se encuentra en
    el modulo `data`
    """
    opciones_validas : list[int, str] = list(
        map(lambda opcion: [opcion.value, opcion.name], OpcionesDisponibles))

    opciones_de_utilidad : list[int, str] = list(
        map(lambda opcion: [opcion.value, opcion.name], Utilidades))

    todas_las_opciones : list[list[int, str]] = opciones_de_utilidad + opciones_validas

    mostrar_titulo("Directorio")

    tabla_de_opciones : PrettyTable = PrettyTable()
    tabla_de_opciones.field_names = ["OPCION", "VALOR"]
    tabla_de_opciones.add_rows(todas_las_opciones)

    print(tabla_de_opciones, end="\n" * 2)