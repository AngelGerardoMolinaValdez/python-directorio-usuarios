import os
from vistas import *
from menus import *
from entradas import *
from data import *
from errores import *


while True:
    try:
        mostrar_menu()
        codigo_funcionalidad : int = obtener_respuesta_de_movimiento()

        nombre_flujo_de_ejecucion : callable = OpcionesDisponibles(
               codigo_funcionalidad).funcionalidad()

        nombre_flujo_de_ejecucion()

    except LimpiezaDePantalla:
         os.system("cls")

    except EjecucionDetenida:
         mostrar_mensaje_de_despedida()
         exit()

    except Exception as error_execution:
         mostrar_error_obtenido(str(error_execution))
         input("🛑 Pulsa enter para continuar! 🛑\n")
