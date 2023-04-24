class Checksuper:
    @classmethod
    def check(cls,obj):
        print([issubclass(cls,i) for i in [Digit,Integer,Float,Positive,Negative]])
        if [issubclass(cls,i) for i in [Digit,Integer,Float,Positive,Negative]]:
            print("ok")
        else:
            print("no")
class Integer(Checksuper):
    def __init__(self, value):
        self.check(value)
        #super(Integer, self).__init__(value)
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')

class Digit(Checksuper):
    def __init__(self, value):

        super(Digit, self).__init__(value)
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')




class Float(Checksuper):
    def __init__(self, value):
        super(Float, self).__init__(value)
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')


class Positive(Checksuper):
    def __init__(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Checksuper):
    def __init__(self, value):
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super(PrimeNumber, self).__init__(value)
        self.value = value


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super(FloatPositive, self).__init__(value)
        self.value = value


# digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
#           FloatPositive(3.5), FloatPositive(8.9)]
#
# lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
# lst_float = list(filter(lambda x: isinstance(x, Float), digits))

number=Integer(23)


