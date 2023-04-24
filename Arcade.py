import arcade

class our_picture(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.CORAL)
        arcade.draw_circle_filled(300,300,200,arcade.color.LIGHT_BLUE)
        arcade.draw_circle_filled(200,400,25,arcade.color.BLACK)
        arcade.draw_circle_filled(400, 400, 25, arcade.color.BLACK)
        arcade.draw_arc_outline(300,200,50,80,arcade.color.BLACK,180,360,50)#x,y,ширина,высота,цвет,начальный градус,конец градуса,ширина линий
okno= our_picture(600,600,"Smilik")
arcade.run()