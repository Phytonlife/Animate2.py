import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Играем в пинг понг"

MOVEMENT_SPEED = 5


class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x = -self.change_x

        # логика соударения с нижним краем перенесена в .update самой игры
        if self.top > SCREEN_HEIGHT:
            self.change_y = -self.change_y


class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x

        # чтобы не уезжала ракетка за края экрана
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.sprites = None
        self.player_sprite = None
        self.ball_sprite = None

        # свойства для жизней и очков
        self.score = 0
        self.lives = 3

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.sprites = arcade.SpriteList()

        self.player_sprite = Player("bar.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.sprites.append(self.player_sprite)

        self.ball_sprite = Ball("player.png", SPRITE_SCALING)
        self.ball_sprite.center_x = SCREEN_WIDTH / 2
        self.ball_sprite.center_y = 500
        self.ball_sprite.change_x = 2
        self.ball_sprite.change_y = 2
        self.sprites.append(self.ball_sprite)

    def on_draw(self):
        arcade.start_render()

        self.sprites.draw()

        # выводим сколько очков
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 560, arcade.color.WHITE, 20)

        # выводим количество жизней
        output = "Lives: " + str(self.lives)
        arcade.draw_text(output, 700, 560, arcade.color.WHITE, 20)

    def update(self, delta_time):
        # следующая строчка для тех, кто сам хочет написать проверку соударения шарика и ракетки
        # if self.ball_sprite.left > self.player_sprite.left and self.ball_sprite.right < self.player_sprite.right and self.ball_sprite.bottom < self.player_sprite.top:
        # или же можно использовать специальный метод для проверки соударения
        if arcade.check_for_collision(self.ball_sprite, self.player_sprite):
            # подняли нижнюю границу шарика до верха ракетки
            self.ball_sprite.bottom = self.player_sprite.top
            # изменили направление движения
            self.ball_sprite.change_y = -self.ball_sprite.change_y
            # увеличили очки
            self.score += 1

        if self.ball_sprite.bottom <= 0:
            # уменьшили жизни на 1
            self.lives -= 1
            # подняли шарик наверх
            self.ball_sprite.center_y = 500

        self.sprites.update()

    # код, срабатывающий при нажатии клавиши
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5

    # код, срабатывающий при поднятии клавиши
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()

