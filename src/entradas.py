from data import OpcionesDisponibles, Utilidades
from errores import RespuestaEsLetraNoNumero,EjecucionDetenida,LimpiezaDePantalla,RespuestaFueraDeRango


def obtener_respuesta_de_movimiento() -> int:
    """Solicita la respuesta para realizar el movimiento

    Valida el range de opciones directamente del objeto enum
    que se encuentra en el modulo `data`

    Returns:
        int: el digito numerico de la respuesta
    """
    respuestas_validas = map(lambda opcion: opcion.value,
                             OpcionesDisponibles.__members__.values())

    respuesta = input("💬 Ingresa tu respuesta(solo numeros) ")

    if not respuesta.isdigit():
        raise RespuestaEsLetraNoNumero("Fue ingresada una letra y no un numero.")

    if int(respuesta) == Utilidades.CERRAR.value:
        raise EjecucionDetenida()

    if int(respuesta) == Utilidades.LIMPIAR.value:
        raise LimpiezaDePantalla()

    if int(respuesta) not in respuestas_validas:
        raise RespuestaFueraDeRango("La respuesta esta fuera de rango")

    return int(respuesta)
