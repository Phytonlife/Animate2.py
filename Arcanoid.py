import arcade



 # задаем ширину, высоту и заголовок окна

SCREEN_WIDTH = 600

SCREEN_HEIGHT = 600

SCREEN_TITLE = "Пинг-понг"

class Brick(arcade.Sprite):
    def update(self):
        if arcade.check_for_collision(self,game.ball):
            game.ball.change_y=-game.ball.change_y
            game.Point=game.Point+1
            self.remove_from_sprite_lists()
            if game.Point==28:
                game.ball.stop()

class Ball(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x

        self.center_y += self.change_y

        if self.left < 0 or self.right>SCREEN_WIDTH:

         self.change_x = -self.change_x

        if self.top>SCREEN_HEIGHT:

         self.change_y = -self.change_y





class Bar(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x




class OurGame(arcade.Window):


    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.ball = Ball("player.png", 0.2)

        self.bar = Bar("bar.png", 0.3)

        self.bricks=arcade.SpriteList()

        self.Score=3
        self.Point=0
        self.level=1
    level=1
    if level == 2:

        for j in range(1, 5):

            for i in range(7):
                brick1 = Brick("bar.png", 0.2)
                brick1.center_x = 75 + i * 75
                brick1.center_y = 350 + j * 50
                bricks.append(brick1)


    def setup(self):
        if self.level==1:

            for j in range(1,5):

                for i in range(7):

                    brick1=Brick("bar.png",0.2)
                    brick1.center_x=75+i*75
                    brick1.center_y=350+j*50
                    self.bricks.append(brick1)




        self.ball.center_x = 300

        self.ball.center_y = 300

        self.ball.change_x = 3

        self.ball.change_y = 5



        self.bar.center_x = 300

        self.bar.center_y = 20

        self.bar.change_x = 0



# отрисовка объектов

    def on_draw(self):

        arcade.start_render()

        arcade.set_background_color(arcade.color.WHITE)

        self.ball.draw()
        self.bricks.draw()

        self.bar.draw()
        arcade.draw_text(f"Попытки {self.Score} \n   Счет {self.Point}",500,200,arcade.color.BLACK,14)



# логика

    def update(self, delta_time):
        self.bricks.update()
        if self.ball.bottom<0:

            self.ball.center_y=450

            self.Score=self.Score-1
            if self.Score==0:
                self.ball.stop()
        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.bottom = self.bar.top
            self.ball.change_y = -self.ball.change_y


        self.ball.update()

        self.bar.update()



    def on_key_press(self, key, modifiers):# бинт клавиш

        if key == arcade.key.RIGHT:

            self.bar.change_x = 5

        if key == arcade.key.LEFT:


            self.bar.change_x = -5

    def on_key_release(self, key, modifiers):# когда клавишу отпустили

        if key == arcade.key.RIGHT or key == arcade.key.LEFT:

            self.bar.change_x = 0



game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

game.setup()

arcade.run()