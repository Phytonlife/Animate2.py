import arcade
import random
class ship(arcade.Sprite):
    def update(self):
        pass
class pulya(arcade.Sprite):
    def __init__(self):
        super(pulya, self).__init__("laser.png",0.7)
        self.sound = arcade.load_sound("laser.wav")


    def update(self):
        self.change_y=5
        self.center_y=self.center_y+self.change_y
        #if arcade.check_for_collision(self)
        if self.center_y>=600:
            self.kill()

class enemies(arcade.AnimatedTimeSprite):
    def __init__(self):
        super(enemies, self).__init__()
        self.textures.append(arcade.load_texture("tie fighter.png"))
        self.textures.append(arcade.load_texture("tie fighter2.png"))

    def update(self):
        self.center_y-=1

class game3d(arcade.Window):
    def __init__(self,x,y,name):
        super(game3d, self).__init__(x,y,name)
        self.bg=arcade.load_texture("space_background.png")
        self.Ship=ship("x-wing.png",0.5)
        self.set_mouse_visible(False)
        self.pulyi=arcade.SpriteList()
        self.Enemy=arcade.SpriteList()



    def setup(self):
        self.Ship.center_x=400
        self.Ship.center_y=25
        for i in range(1,20):
            enemyone=enemies()
            enemyone.center_y=random.randint(700,1500)
            enemyone.center_x=random.randint(0,800)
            self.Enemy.append(enemyone)


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.Ship.center_x=x
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        Pulya=pulya()
        Pulya.top=self.Ship.top
        Pulya.center_x=self.Ship.center_x
        arcade.play_sound(Pulya.sound)
        self.pulyi.append(Pulya)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(400,300,800,600,self.bg)
        self.Ship.draw()
        self.pulyi.draw()
        self.Enemy.draw()

    def update(self, delta_time: float):
        self.pulyi.update()
        self.Enemy.update_animation()
        self.Enemy.update()

starwars2d=game3d(800,600,"Star Wars")
starwars2d.setup()
arcade.run()