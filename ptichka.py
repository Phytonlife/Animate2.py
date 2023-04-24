

import arcade


class person(arcade.AnimatedTimeSprite):
    def update(self):
        pass
class person2(arcade.Sprite):
    def update(self):
        pass

class person3(arcade.Sprite):
    def update(self):
        pass

class game(arcade.Window):
    def __init__(self,x,y,title):
        super(game, self).__init__(x,y,title)
        pass





    def setup(self):
        pass


    def on_draw(self):
        pass

    def update(self, delta_time: float):
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.SPACE:
            pass






    def on_key_release(self, symbol: int, modifiers: int):
        pass






window=game(1000,500,"drokonchik")
window.setup()
arcade.run()


