import pyfiglet
from log import NivelesLog


def mostrar_titulo(nombre : str) -> None:
    """muestra un texto en pantalla con formato

    encapsularlo en una funcion permite posteriormente
    poder modificar el disenio y aplicarlo a todas las funciones
    que lo utilicen

    Args:
        nombre (str): el nombre del que se mostrara conformato
    """
    pyfiglet.print_figlet(nombre.upper())


def mostrar_error_obtenido(error : str) -> None:
    """imprime el mensaje de error con emojis ❌

    Args:
        error (str): el mensaje de error
    """
    emoji_error = "🚫"
    print('\n')
    print(emoji_error, error, emoji_error, end='\n' * 2)


def mostrar_mensaje_de_despedida() -> None:
    """mensaje de despedida
    """
    emoji_despedida : str = "🏆"
    print("\n")
    print(f"{emoji_despedida} Gracias por su tiempo. Hasta pronto! {emoji_despedida}")


def mostrar_log(mensaje : str, nivel : NivelesLog = NivelesLog.INFO) -> None:
    """imprime un mensaje con emojis que representan el nivel de log

    Args:
        mensaje (str): el mensaje que se imprimira
        nivel (NivelesLog, optional): objeto que hace referencia al nivel del log. Defaults to NivelesLog.INFO.
    """
    emoji = nivel.emoji()

    print('\n')
    print(f"{emoji} {mensaje} {emoji}", end='\n' * 2)
