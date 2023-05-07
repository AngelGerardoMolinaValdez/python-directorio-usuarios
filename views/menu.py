from prettytable import PrettyTable
from model import BusinessOptions, UtilityOptions
from views.util import show_title


def show_menu() -> None:
    """muestra las opciones disponibles en funcionamiento

    toma las opciones del objeto enum que se encuentra en
    el modulo `data`
    """
    valid_options : list[int, str] = list(
        map(
        lambda option: [option.value, option.name], BusinessOptions)
    )

    utility_options : list[int, str] = list(
        map(
        lambda option: [option.value, option.name], UtilityOptions)
    )

    options : list[list[int, str]] = utility_options + valid_options

    show_title("DIRECTORY")
    tabla_de_opciones : PrettyTable = PrettyTable()
    tabla_de_opciones.field_names = ["OPTION", "SUMMARY"]
    tabla_de_opciones.add_rows(options)
    print(tabla_de_opciones, end="\n" * 2)
