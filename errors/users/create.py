class UserNameEmpty(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class PhoneEmpty(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class EmailEmpty(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class AddressEmpty(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class UserNameIsOnlyNumbers(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class PhoneNumberDoesNotContainOnlyNumbers(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])


class EmailNotValid(Exception):
    def __str__(self):
        return self.__class__.__name__ + " => " + str(self.args[0])
