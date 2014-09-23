# -*- coding: utf-8 -*-


class RomanNumeral(object):
    """ Represents an a Roman Numeral

    """

    def __init__(self, value):
        if isinstance(value, str) or isinstance(value, unicode):
            self.value = self.__parse_roman_numeral_from_string(value)
        if isinstance(value, int):
            self.value = value

    def __repr__(self):
        return 'RomanNumeral({})'.format(self.value)


    def __cmp__(a, b):
        cmpnum = cmp(a.value, b.value)
        return cmpnum

    def __add__(self, other):
        return self.__class__(self.value + int(other))

    def __sub__(self, other):
        return self.__class__(self.value - int(other))

    def __mul__(self, other):
        return self.__class__(self.value * int(other))

    def __floordiv__(self, other):
        return self.__class__(self.value / int(other))

    def __mod__(self, other):
        return self.__class__(self.value % int(other))

    def __divmod__(self, other):
        return self.__floordiv__(other), self.__mod__(other)

    def __div__(self, other):
        return self.__floordiv__(other)

    def __pow__(self, other, modulo=None):
        return self.__class__(self.value ** int(other))




    @classmethod
    def from_int(cls, roman_as_int):
        """ Create a RomanNumeral object from an int

        """

        cls(roman_as_int)

    @classmethod
    def from_string(cls, roman_as_string):
        """ Create a RomanNumeral object from an string

        """

        cls(roman_as_string)


    def __parse_roman_numeral_from_string(value):

        return 10