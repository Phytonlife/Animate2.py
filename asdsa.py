class Digit:
    def __init__(self):

        super(Digit, self).__init__()
        if not isinstance(self.value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')

class Integer:
    def __init__(self):
        super(Integer, self).__init__()
        if not isinstance(self.value, int):
            raise TypeError('значение не соответствует типу объекта')


class Float:
    def __init__(self):
        super(Positive, self).__init__()
        if not isinstance(self.value, float):
            raise TypeError('значение не соответствует типу объекта')


class Positive:
    def __init__(self):
        super(Positive, self).__init__()
        if self.value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative:
    def __init__(self):
        super(Positive, self).__init__()
        if self.value >= 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        self.value = value
        super(PrimeNumber, self).__init__()


class FloatPositive(Float, Positive):
    def __init__(self, value):
        self.value = value
        super(FloatPositive, self).__init__()


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))





