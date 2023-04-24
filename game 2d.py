import random

import arcade


class person(arcade.AnimatedTimeSprite):
    def update(self):
        self.center_y=self.center_y+self.change_y

        if self.center_y <= 35:
            self.change_y = 0
            self.center_y = 35
            window.prizhok=True
        if self.center_y >= 170:
            self.change_y=-5
class person2(arcade.Sprite):
    def update(self):
        self.center_x=self.center_x-self.change_x

        if self.center_x<=-20:
            self.center_x=self.center_x+1000+random.randint(0,200)
            window.Point=window.Point+1

class person3(arcade.Sprite):
    def update(self):
        self.center_x=self.center_x-self.change_x

        if self.center_x<=-20:
            self.center_x=self.center_x+1200+random.randint(0,200)
            window.Point = window.Point + 1

class game(arcade.Window):
    def __init__(self,x,y,title):
        super(game, self).__init__(x,y,title)
        self.Bg=arcade.load_texture("desert.png")
        self.Bg2=arcade.load_texture("desertGO.png")
        self.Playstatus=True

        self.Person1=person(0.5)
        self.Person1.textures=[]
        self.Person1.textures.append(arcade.load_texture("dino1.png"))
        self.Person1.textures.append(arcade.load_texture("dino2.png"))
        self.Person1.textures.append(arcade.load_texture("dino3.png"))
        self.Kaktus=person2("cactus2.png",0.5)
        self.Kaktus2=person3("cactus3.png",0.5)
        self.Point=0


    prizhok=True


    def setup(self):
        self.Kaktus.change_x = 5
        self.Person1.center_x=50
        self.Person1.center_y=35
        self.Person1.change_y=0
        self.Kaktus.center_x=1200
        self.Kaktus.center_y=30
        self.Kaktus2.center_x = 1600
        self.Kaktus2.center_y = 30
        self.Kaktus2.change_x=5


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        if self.Playstatus==True:

            arcade.draw_texture_rectangle(500,250,1000,500,self.Bg)
        if self.Playstatus == False:
            arcade.draw_texture_rectangle(500, 250, 1000, 500, self.Bg2)
        arcade.draw_text(f"Score {self.Point}",900,450,arcade.color.BLACK,14)
        self.Person1.draw()
        self.Kaktus.draw()
        self.Kaktus2.draw()

    def update(self, delta_time: float):
        if arcade.check_for_collision(self.Person1,self.Kaktus) or arcade.check_for_collision(self.Person1,self.Kaktus2):
            self.Person1.stop()
            self.Kaktus.stop()
            self.Kaktus2.stop()
            self.Playstatus=False

        self.Person1.update_animation()
        self.Person1.update()
        self.Kaktus.update()
        self.Kaktus2.update()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.SPACE:
            if self.prizhok==True:
                self.prizhok = False
                self.Person1.change_y=5






    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.Person1.change_y = -5






window=game(1000,500,"drokonchik")
window.setup()
arcade.run()


