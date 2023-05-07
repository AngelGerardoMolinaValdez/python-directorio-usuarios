from pyfiglet import print_figlet
# from log import NivelesLog


def show_title(text : str) -> None:
    """muestra un texto en pantalla con formato

    encapsularlo en una funcion permite posteriormente
    poder modificar el disenio y aplicarlo a todas las funciones
    que lo utilicen

    Args:
        text (str): el nombre del que se mostrara con formato
    """
    print_figlet(text.upper())


def show_goodbye_message() -> None:
    """mensaje de despedida
    """
    emoji_despedida : str = "🏆"
    print("\n")
    print(f"{emoji_despedida} Gracias por su tiempo. Hasta pronto! {emoji_despedida}")
