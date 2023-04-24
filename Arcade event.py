import random

import arcade
class figureEvent(arcade.Window):
    def __init__(self,width,height,title):
        super(figureEvent, self).__init__(width,height,title)
        self.X1=300
        self.Y1=300
        self.change_numberX=5
        self.change_numberY=5
        self.random=random.randint(1,15)
        self.randomy=random.randint(1,15)
        self.kvadratx=400
        self.kvadraty=200
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_circle_filled(self.X1,self.Y1,24,arcade.color.GUPPIE_GREEN)
        arcade.draw_rectangle_filled(self.kvadratx,self.kvadraty,72,72,arcade.color.DARK_GREEN)
        arcade.draw_rectangle_outline(self.kvadratx-100,self.kvadraty+100,77,77,arcade.color.BROWN,5)
    def update(self, delta_time: float):
        # if self.Y1 <600:
        self.Y1 = self.Y1 + self.random
        if self.Y1>576:
            self.random=-self.random
        if self.Y1 < 24:
            self.random = -self.random
        self.X1 = self.X1 + self.randomy
        if self.X1>576:
            self.randomy=-self.randomy
        if self.X1 < 24:
            self.randomy = -self.randomy


event=figureEvent(600,600,"title")
arcade.run()

