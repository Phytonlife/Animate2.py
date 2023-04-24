import random

day=0
class Jivotnoe():
    def __init__(self,name,zapas,golod=100):
        self.Name=name
        self.Zapas=zapas
        self.Golod=golod
    def dobivat_edu(self,poisk):
        self.Zapas=self.Zapas+poisk
    def kuwat_edu(self,kolichestvo_edi):
        self.Golod=self.Golod+kolichestvo_edi
        self.Zapas=self.Zapas-kolichestvo_edi

class Pcheli (Jivotnoe):
    def __init__(self,name,zapas,golod,med=100):
        super().__init__(name,zapas,golod)
        self.Med=med
    def sobirat_med(self,kolichestvo):
        self.Med=self.Med+kolichestvo
        self.Golod=self.Golod-kolichestvo

    def day1(self):
        global day
        day+=1
        randompchel=random.randint(1,15)
        k=self.sobirat_med(randompchel)
        print(f"День - {day}")
        print(f"Собрал мед{k}")
        print(f"Собрал еду {self.dobivat_edu(randompchel)}")
        print(f"Покушал {self.kuwat_edu(randompchel)}")




def life(self):
    print(f"Запас меда - {self.Med}")
    print(f"Запас сытности - {self.Golod}")
    print(f"Имя - {self.Name}")
    print(f"Запас еды {self.Zapas}")



Phela1=Pcheli("Pchela1",100,golod=100)

life(Phela1)
Pcheli.day1(Phela1)
