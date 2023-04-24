import random

import arcade
import Animate


# задаем ширину, высоту и заголовок окна

SCREEN_WIDTH = 660

SCREEN_HEIGHT = 660

SCREEN_TITLE = "Bomberman"

PLAYER1_SPEED = 10

PLAYER2_SPEED = 10

class TverdiBlock(arcade.Sprite):
    def __init__(self):
        super(TverdiBlock, self).__init__("Blocks/SolidBlock.png",1)
    pass




class Bomberman(Animate.Animate):
    def __init__(self,speed):
        super(Bomberman, self).__init__("Bomberman/Front/Bman_F_f00.png",0.5)
        self.direction = 4
        self.walk_down_frames = []
        self.motion = 0
        self.speed = speed


        for i in range(8):

            self.walk_down_frames.append(arcade.load_texture(f"Bomberman/Front/Bman_F_f0{i}.png"))

        # Back

        self.walk_up_frames = []

        for i in range(8):

            self.walk_up_frames.append(arcade.load_texture(f"Bomberman/Back/Bman_B_f0{i}.png"))

        # Right

        self.walk_right_frames = []

        for i in range(8):

            self.walk_right_frames.append(arcade.load_texture(f"Bomberman/Side/Bman_F_f0{i}.png"))

        self.walk_left_frames = []

        for i in range(8):
            self.walk_left_frames.append(arcade.load_texture(f"Bomberman/Side/Bman_F_f0{i}.png",flipped_horizontally = True))

    def costume_change(self):
        if self.direction == 1:
            self.textures = self.walk_left_frames
        elif self.direction == 2:
            self.textures = self.walk_right_frames
        elif self.direction == 3:
            self.textures = self.walk_up_frames
        elif self.direction == 4:
            self.textures = self.walk_down_frames
    def update(self):
        self.center_x += self.change_x

        self.center_y += self.change_y

class RazrushaemiBlock(arcade.Sprite):
    def __init__(self):
        super(RazrushaemiBlock, self).__init__("Blocks/ExplodableBlock.png",1)
    pass

class Game(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.bg=arcade.load_texture("Blocks/BackgroundTile.png")

        self.tverdiBlocks=arcade.SpriteList()
        self.razrushamiBlocks=arcade.SpriteList()
        self.bomberman = Bomberman(PLAYER1_SPEED)
        self.bomberman2 = Bomberman(PLAYER2_SPEED)


        self.setup()




    def setup(self):
        self.bomberman.set_position(30,30)
        self.bomberman2.set_position(630, 630)
        self.bomberman2.color=(255,0,0)

        for stroki in range(11):
            for stolbec in range(11):
                if stroki%2==1 and stolbec%2==1:
                    tverdiblock=TverdiBlock()
                    tverdiblock.center_x=60*stolbec+30
                    tverdiblock.center_y=60*stroki+30
                    self.tverdiBlocks.append(tverdiblock)
                else:
                    if random.randint(1,2)==1:
                        if stolbec==0 and stroki<3 or stolbec<3 and stroki==0 or stolbec==10 and stroki>7 or stolbec>7 and stroki==10 :
                            continue
                        razrushamiblock=RazrushaemiBlock()
                        razrushamiblock.center_x = 60 * stolbec + 30
                        razrushamiblock.center_y = 60 * stroki + 30
                        self.razrushamiBlocks.append(razrushamiblock)




    def on_draw(self):


        self.clear()


        for stroka in range(11):
            for stolbec in range(11):
                centrx=stolbec*60+30
                centry=stroka*60+30
                arcade.draw_texture_rectangle(centrx,centry,60,60,self.bg)
        self.tverdiBlocks.draw()
        self.razrushamiBlocks.draw()
        self.bomberman.draw()
        self.bomberman2.draw()



    def update(self, delta_time):
        self.bomberman.update_animation(delta_time)
        self.bomberman2.update_animation(delta_time)
        self.bomberman.update()

        pass



    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            if self.bomberman.motion==0:
                self.bomberman.motion=1
                self.bomberman.direction = 1
                self.bomberman.change_x = -self.bomberman.speed
        elif key == arcade.key.RIGHT:
            if self.bomberman.motion==0:
                self.bomberman.motion=1
                self.bomberman.direction = 2
                self.bomberman.change_x = self.bomberman.speed
        elif key == arcade.key.UP:
            if self.bomberman.motion==0:
                self.bomberman.motion=1
                self.bomberman.direction = 3
                self.bomberman.change_y = self.bomberman.speed
        elif key == arcade.key.DOWN:
            if self.bomberman.motion==0:
                self.bomberman.motion=1
                self.bomberman.direction = 4
                self.bomberman.change_y = -self.bomberman.speed
        self.bomberman.costume_change()
        self.bomberman2.costume_change()



    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.UP or key == arcade.key.DOWN:

            self.bomberman.change_x = 0

            self.bomberman.change_y = 0

            self.bomberman.direction = 0
            self.bomberman.motion=0





window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run()