from model import BusinessOptions, UtilityOptions
from errors.inputs import *


def get_user_response() -> int | Exception:
    """Solicita la respuesta para realizar el movimiento

    Valida el range de opciones directamente del objeto enum
    que se encuentra en el modulo `data`

    Returns:
        int: el digito numerico de la respuesta
    """
    valid_business_responses : list[str] = map(
        lambda option: option.value,
                             BusinessOptions.__members__.values()
    )
    user_response : str = input("💬 Cual es tu respuesta(solo numeros)? ")

    if not user_response.isdigit():
        return ResponseShouldBeANumberNotLetter()

    if int(user_response) == UtilityOptions.CLOSE.value:
        return StopExecution()

    if int(user_response) == UtilityOptions.CLEAR.value:
        return ClearScreen()

    if int(user_response) not in valid_business_responses:
        return ResponseOutOfRange()

    return int(user_response)
