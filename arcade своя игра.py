import random

import arcade
import random
x=300
y=7

class igra(arcade.Window):
    def __init__(self,hight,width,title):
        super(igra, self).__init__(hight,width,title)

    raketka = arcade.draw_rectangle_filled(x, y, 70, 15, arcade.color.BLUE, 0)











    def on_draw(self):

        arcade.start_render()
        arcade.set_background_color(arcade.color.TIFFANY_BLUE)



    # def update(self, delta_time: float):











igra1=igra(600,600,"Tennis")

arcade.run()
