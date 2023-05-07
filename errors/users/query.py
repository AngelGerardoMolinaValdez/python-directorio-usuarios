class UserIdentifierEmpty(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])