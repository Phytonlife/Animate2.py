import random


class Geroi():
    def __init__(self,Name,Health,Damage,Agility,Armor,Magic=random.randint(0,3)):
        self.name=Name
        self.health=Health
        self.damage=Damage
        self.agility=Agility
        self.armor=Armor
        self.magic=Magic

    def magic_on(self):
        if self.magic==0:
            self.health=self.health*2
        elif self.magic==1:
            self.damage=self.damage*3
        elif self.magic==2:
            self.agility=self.agility*3
        else:
            pass

DragonKnight=Geroi("Dragon Knight",100,25,15,5)
Drakon=Geroi("Dragon",500,50,10,0,4)

magics=["Двойное здороье","Тройная атака","Тройная ловкость","Не получил магию"]
def arena1x1(a,b):
    a.magic_on()
    print(f" {a.name} получил магию {magics[a.magic]}")
    a.armor = a.armor * a.agility / 10
    a.health = a.health + a.armor * random.randint(1, 3)
    while True:

        a.health=a.health+a.armor*random.randint(1,3)-b.damage
        print(f"воин {b.name} наносит урон {a.name} воину {b.damage}, у воина {a.name} осталось здоровья {a.health}  ")
        b.health = b.health + b.armor * random.randint(1, 3) - a.damage
        print(f"воин {a.name} наносит урон {b.name} воину {a.damage}, у воина {b.name} осталось здоровья {b.health}  ")
        if a.health<=0:
            print(f"выйграл {b.name}")
            break
        elif b.health<=0:
            print(f"выйграл {a.name}")
            break



arena1x1(DragonKnight,Drakon)