import arcade

import random

 # константы #

SCREEN_TITLE = "Minesweeper" # название окна

ROW_COUNT = 7 # количество строк на игровом поле

COLUMN_COUNT = 7 # количество столбцов на игровом поле

CELL_WIDTH = 100 # ширина одной ячейки

CELL_HEIGHT = 100 # высота одной ячейки

MARGIN = 2 # толщина границы (то есть линий между ячейками)

# ширина и высота окна

SCREEN_WIDTH = (CELL_WIDTH + MARGIN) * COLUMN_COUNT + MARGIN

SCREEN_HEIGHT = (CELL_HEIGHT + MARGIN) * ROW_COUNT + MARGIN

MINES_COUNT = 10 # количество мин на игровом поле

class Minesweeper(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        self.grid = []

    def setup_grid(self):

        for row in range(ROW_COUNT):

            self.grid.append([])

            for column in range(COLUMN_COUNT):

                self.grid[row].append(0)

    def setup(self):

        """Расположение мин и трофея на игровой сетке"""

        pass

    def on_draw(self):

        """Отрисовка объектов"""

        arcade.start_render()

        arcade.set_background_color(arcade.color.BLACK)
        for row in range(ROW_COUNT):

            for column in range(COLUMN_COUNT):

                color = arcade.color.LIGHT_BLUE

                x = (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2

                y = (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2


                arcade.draw_rectangle_filled(x, y, CELL_WIDTH, CELL_HEIGHT, color)
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print(x,y)
        column = x // (CELL_WIDTH + MARGIN)

        row = y // (CELL_HEIGHT + MARGIN)

        if [row, column] in self.mines_coordinates:

            self.grid[row][column] = 1

            self.mines_coordinates.remove([row, column])

        if [row, column] == self.trophy:

            self.grid[row][column] = 4



game = Minesweeper(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

game.setup()
game.setup_grid()

arcade.run()