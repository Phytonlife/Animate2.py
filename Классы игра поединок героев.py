import random

random_magic=random.randint(1,5)

class Hero():
    regen = False
    critical = False

    def __init__(self,atack,hp,magic=random_magic):
        self.Atack=atack
        self.Health=hp
        self.Magic=random_magic
    def Hero_magic(self):
        global regen
        global critical
        if self.Magic==0:
            print("У тебя появилось регенерация")
            self.regen=True
        elif self.Magic==1:
            print("Ты получил способность двойную атаку")
            self.Atack=self.Atack*2
        elif self.Magic==2:
            self.Health = self.Health * 2
            print("Ты получил способность 2ую жизнь")
        elif self.Magic==3:

            self.critical=True


    def uron(self,damage=0):
        self.Health=self.Health-damage
#роверяем жизнь и атаку
angel=Hero(15,200)
demon=Hero(14,150,1)
#Наноси урон
demon.uron(20)
print(demon.Health)
raund=0
Hero1="Angel"
Hero2="Demon"
#Магия

#Magic=["Regen","Double Damage","Monster Health","20% critical damage x5"]
#print(Magic)
#p=input("choose your magic 0-3")
angel.Hero_magic()
demon.Hero_magic()
while True:
    raund=raund+1
    print(f"Начался {raund} раунд  ")
    print("Ходит первый игрок ")
    deistvie1=input("Какое действия выбираете 1 - Атаковать, 2 - Встать в броню , 3 - Сделать магию")
    if deistvie1=="1":
        demon.uron(angel.Atack)
    elif deistvie1=="2":
        angel.Health+=random.randint(1,50)
    elif deistvie1=="3":
        angel.Hero_magic()


    if angel.Health<=0 and demon.Health<=0:
        print("Ничья")
    elif angel.Health<0:
        print(f"Победил {Hero2}")
        break
    elif demon.Health < 0:
        print(f"Победил {Hero1}")
        break


    angel.uron(demon.Atack)
    print(f"У {Hero1}, осталось здоровья {angel.Health}")
    print(f"У {Hero2}, осталось здоровья {demon.Health}")


