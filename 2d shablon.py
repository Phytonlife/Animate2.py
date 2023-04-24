# здесь пишите программу
class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append({gd.name: gd.price})

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return self.goods


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

gd=Table("Table",200)
gd1=Table("вазы",200)
gd2=Table("вазы",200)
gd3=Table("вазы",200)
gd4=Table("вазы",200)