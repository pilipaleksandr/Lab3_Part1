class Rational:

    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError("Denominator can't be '0'")
        self.__denominator = value

    def show_rational_form(self):
        print("Rational form of given number: ", self.__numerator, "/", self.__denominator)

    def show_float_form(self):
        print("Floating-point format of given number: ", self.__numerator / self.__denominator)


if __name__ == '__main__':
    try:
        obj1 = Rational()
        obj1.show_rational_form()
        obj1.show_float_form()

        obj2 = Rational(2,5)
        obj2.show_rational_form()
        obj2.show_float_form()
    except Exception as e:
        print(e)