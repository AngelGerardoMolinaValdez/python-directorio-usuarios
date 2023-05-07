class ResponseShouldBeANumberNotLetter(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class ResponseOutOfRange(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class StopExecution(Exception):
    pass


class ClearScreen(Exception):
    pass