import arcade

class Peizazh(arcade.Window):
    def __init__(self,width,height,title):
        super(Peizazh, self).__init__(width,height,title)
    def ptichka(self,x,y):
        arcade.draw_arc_outline(x,y,30,10,arcade.color.BLACK,0,160,5)
    def zdanie(self,x,y):
        arcade.draw_rectangle_filled(x,y,140,100,arcade.color.BROWN)
        arcade.draw_rectangle_filled(x, y, 40, 40, arcade.color.CYAN)
        arcade.draw_line(x-20,y,x+20,y,arcade.color.BLACK,5)
        arcade.draw_line(x , y+20, x , y-20, arcade.color.BLACK, 5)
        arcade.draw_triangle_filled(x-70,y+50,x,y+100,x+70,y+50,arcade.color.CORAL)

    def derevo(self,x,y):
        arcade.draw_rectangle_filled(x,y,15,100,arcade.color.BROWN)
        arcade.draw_arc_outline(x+30,y+50,50,15,arcade.color.GREEN,0,170,15)
        arcade.draw_arc_outline(x - 30, y + 50, 50, 15, arcade.color.GREEN, 0, 170, 15)
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        arcade.draw_rectangle_filled(300,100,600,200,arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(100,400,40,arcade.color.YELLOW)
        self.derevo(100,70)
        self.derevo(400,140)
        self.ptichka(50,300)
        self.zdanie(230,200)
        self.ptichka(75, 300)
        self.ptichka(150, 400)
        self.ptichka(175, 400)
        self.ptichka(300, 370)
        self.ptichka(325, 370)
        self.ptichka(450, 400)
        self.ptichka(475, 400)



land=Peizazh(500,500,"Peizazh")
arcade.run()