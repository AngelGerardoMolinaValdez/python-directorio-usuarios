from enum import Enum


class BusinessOptions(Enum):
    """enumera las opciones disponibles de acciones validas
    del proyecto

    Los valores que se definen en las constantes son:
    key = el valor de la opcion que se mostrara en el menu de opciones
    value = el objeto de la funcion que ejecutara al ser invocada

    Args:
        Enum (enum): hereda la clase Enum para crear la estructura de datos
    """
    CREATE = 2
    DELETE = 3
    UPDATE = 4
    QUERY = 5
    GENERAL_QUERY = 6
    # REPORT = 7
    # GENERAL_REPORT = 8



class UtilityOptions(Enum):
    """Enumera las funciones de utilidad del sistema

    Al invocar alguna de estas funcionalidades se provocara una excepcion
    que permitira realizar x accion en la ejecucion

    Args:
        Enum (enum): la clase que heredara para volverse objeto enum
    """
    CLOSE = 0
    CLEAR = 1
