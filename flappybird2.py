import arcade
class Bird(arcade.AnimatedTimeSprite):
    pass

class game2d(arcade.Window):
    def __init__(self,x,y,title):
        super(game2d, self).__init__(x,y,title)
        self.ball=Bird(0.5)
    def setup(self):


