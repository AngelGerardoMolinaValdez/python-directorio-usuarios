class RespuestaEsLetraNoNumero(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class RespuestaFueraDeRango(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class EjecucionDetenida(Exception):
    pass


class LimpiezaDePantalla(Exception):
    pass


class UsuarioRegistrado(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class NombreDeUsuarioNoPuedeSerNumero(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class NumeroTelefonicoNoTiene10Digitos(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class NumeroTelefonicoNoTieneSoloNumeros(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class UsuarioNoExiste(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class NombreDeUsuarioVacio(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])
