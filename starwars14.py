import random

import arcade



# устанавливаем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Динозаврик"


class Enemy(arcade.AnimatedTimeSprite):
    def __init__(self):
        super(Enemy, self).__init__(1)
        self.textures.append(arcade.load_texture("tie fighter.png"))
        self.textures.append(arcade.load_texture("tie fighter2.png"))
        self.change_y=-1
    # def update(self):
    #     self.center_y-=self.change_y

class Boat(arcade.Sprite):
    pass
class Pulya(arcade.Sprite):
    def __init__(self):
        super(Pulya, self).__init__("laser.png",0.7)
        self.change_y=5
        self.pylya_sound=arcade.load_sound("laser.wav")
    def update(self):
        self.center_y+=self.change_y
        if self.center_y>600:
            self.kill()

# класс с игрой
class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg=arcade.load_texture("space_background.png")
        self.boat=Boat("x-wing.png",0.7)
        self.set_mouse_visible(False)
        self.pyli=arcade.SpriteList()
        self.Enemies=arcade.SpriteList()
        



    # начальные значения
    def setup(self):

        self.boat.center_x=400
        self.boat.center_y=35
        for i in range(70):
            enemy=Enemy()
            enemy.center_x = random.randint(20,780)
            enemy.center_y = random.randint(600,1400)


    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(400,300,800,600,self.bg)
        self.boat.draw()
        self.pyli.draw()
        self.enemy.draw()


    # игровая логика
    def update(self, delta_time):
        self.pyli.update()
        self.enemy.update_animation()
        self.enemy.update()

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        pass

    # отпустить клавишу
    def on_key_release(self, key, modifiers):
        pass
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.boat.center_x=x
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pulya=Pulya()
        pulya.center_x=self.boat.center_x
        pulya.top=self.boat.top
        self.pyli.append(pulya)
        arcade.play_sound(pulya.pylya_sound)




game  = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game .setup()
arcade.run()
