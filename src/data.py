from typing import Final
from enum import Enum
from alta import alta
from baja import baja
from modificacion import modificacion
from consulta import consulta, consulta_general


FUNCIONES_DISPONIBLES : Final[dict[int, callable]] = {
    2 : alta,
    3 : baja,
    4 : modificacion,
    5 : consulta,
    6 : consulta_general
}


class OpcionesDisponibles(Enum):
    """enumera las opciones disponibles de acciones validas
    del proyecto

    Los valores que se definen en las constantes son:
    key = el valor de la opcion que se mostrara en el menu de opciones
    value = el objeto de la funcion que ejecutara al ser invocada

    Args:
        Enum (enum): hereda la clase Enum para crear la estructura de datos
    """
    ALTA = 2
    BAJA = 3
    MODIFICACION = 4
    CONSULTA = 5
    CONSULTA_GENERAL = 6


    def __init__(self, id_funcionalidad : int) -> None:
        self.id_funcionalidad = id_funcionalidad


    def funcionalidad(self) -> callable:
        """obtiene la funcion a ejecutar
        
        En base al valor del componente de enum seleccionado retornara la funcion del movimiento que ejecutara

        Returns:
            callable: funcion que sera ejecutada
        """
        return FUNCIONES_DISPONIBLES[self.id_funcionalidad]


class Utilidades(Enum):
    """Enumera las funciones de utilidad del sistema

    Al invocar alguna de estas funcionalidades se provocara una excepcion
    que permitira realizar x accion en la ejecucion

    Args:
        Enum (enum): la clase que heredara para volverse objeto enum
    """
    CERRAR = 0
    LIMPIAR = 1
