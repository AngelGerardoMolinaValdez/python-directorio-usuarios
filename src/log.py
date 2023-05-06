from enum import Enum


class NivelesLog(Enum):
    """Enumera los niveles para el log del sistema

    Al validar el nivel del log mostrar el prefijo que es un emoji de
    referencia al estatus del moviento indicado

    Args:
        Enum (enum): la clase que heredara para volverse objeto enum
    """
    INFO = 0
    OK = 1
    ERROR = 2

    def __init__(self, nivel) -> None:
        self.emojis = {
            0 : "🔔",
            1 : "✅",
            2 : "❌"
        }
        self.nivel = nivel
    
    def emoji(self) -> str:
        """obtiene el emoji segun el nivel del log

        Returns:
            str: el emoji
        """
        return self.emojis[self.nivel]