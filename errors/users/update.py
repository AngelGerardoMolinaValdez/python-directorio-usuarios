class UserDoesNotExist(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class UserIDShouldBeANumber(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class UserIDEmpty(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])