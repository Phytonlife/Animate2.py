import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game")
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # создаем спрайт игрока
        self.player_sprite = arcade.Sprite("player.png")
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2

        # создаем спрайт фона
        self.background_sprite = arcade.Sprite("background.png")
        self.background_sprite.center_x = SCREEN_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2

        # создаем список спрайтов
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.background_sprite)
        self.sprite_list.append(self.player_sprite)

        # начальная позиция области просмотра
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()

    def on_update(self, delta_time):
        # перемещаем игрока
        self.player_sprite.center_x += 1

        # устанавливаем новую позицию области просмотра
        self.view_left = self.player_sprite.center_x -100
        self.view_bottom = self.player_sprite.center_y - SCREEN_HEIGHT // 2

        # обновляем область просмотра
        arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left, self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

if __name__ == '__main__':
    game = MyGame()
    arcade.run()