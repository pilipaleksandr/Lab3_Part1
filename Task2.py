class Notebook:
    def __init__(self):
        self.__notebook = []

    def add(self, obj):
        self.__notebook.append(obj)


class Person:
    def __init__(self, name="", surname="", phone_number="", birthday=""):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.birthday = birthday

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        self.__birthday = value

    def __add__(self, value):
        if self.__name == "":
            self.__name = value
        elif self.__surname == "":
            self.__surname = value
        elif self.__phone_number == "":
            self.__phone_number = value
        elif self.__birthday == "":
            self.__birthday = value

    def __sub__(self):
        if self.__birthday != "":
            self.__birthday = ""
            print("Birthday was deleted")
        elif self.__phone_number != "":
            self.__phone_number = ""
            print("Phone number was deleted")
        elif self.__surname != "":
            self.__surname = ""
            print("Surname was deleted")
        elif self.__name != "":
            self.__name = ""
            print("Name was deleted")

    def __mul__(self, value):
        if self.__birthday == value:
            print("It's objects birthday")
        elif self.__phone_number == value:
            print("It's objects phone number")
        elif self.__surname == value:
            print("It's objects surname")
        elif self.__name == value:
            print("It's objects name")
