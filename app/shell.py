import arcade
from app import settings, session
from app.board import mono as board, convert, test, get, mapping
from app.checker import spawn
from tools import stamp
import random


class Shell(arcade.Window):

    def __init__(self):

        self.board = board.Board()
        self.player = None

        super().__init__(
            width=settings.GAME_WINDOW_WIDTH,
            height=settings.GAME_WINDOW_HEIGHT,
            title=settings.GAME_WINDOW_TITLE,
            fullscreen=settings.GAME_WINDOW_FULLSCREEN,
            resizable=settings.GAME_WINDOW_RESIZABLE,
            update_rate=settings.GAME_WINDOW_UPDATE_RATE,
            antialiasing=settings.GAME_WINDOW_ANTIALIASING
        )

        self.active_player = 1              # 1 = White, 2 = Black;
        self.checker_selected = None        # None, if deselected;
        self.tile_hovered = None


    def setup(self):

        self.__board_reset()

        # Arcade preload functions:
        arcade.set_background_color(color=settings.GAME_WINDOW_BACKGROUND_COLOR)
        arcade.run()

    def __player_must_attack(self):
        player_color = 'White' if self.active_player == 1 else 'Black'
        must_attack = False
        for row in mapping.SURFACE_GRID:
            for column in mapping.SURFACE_GRID[row]:
                checker = mapping.SURFACE_GRID[row][column]
                if checker is not None:
                    if checker.color == player_color:
                        if checker.can_kill:
                            must_attack = True
        return must_attack

    def __next_player_turn(self):
        self.active_player = 2 if self.active_player == 1 else 1

    def __board_clear(self):
        self.board.clear()

    def __board_fill(self):
        self.board.fill()
        self.board.update()

    def __board_reset(self):
        self.__board_clear()
        self.__board_fill()

    def __board_update(self):
        self.board.update()

    def on_draw(self):

        def display_highlighted_tiles():

            def highlight_move():
                for move_position in move_list:
                    coordinates = convert.board_position_to_coordinates(conv_position=move_position)
                    move_position_coord_x, move_position_coord_y = coordinates[0], coordinates[1]
                    stamp.board_tile_highlight_move(tile_coord_x=move_position_coord_x,
                                                    tile_coord_y=move_position_coord_y)

            def highlight_attack():
                for attack_position in attack_list:
                    coordinates = convert.board_position_to_coordinates(conv_position=attack_position)
                    move_position_coord_x, move_position_coord_y = coordinates[0], coordinates[1]
                    stamp.board_tile_highlight_attack(tile_coord_x=move_position_coord_x,
                                                      tile_coord_y=move_position_coord_y)

            # Collecting move list and attack list:
            move_list = self.checker_selected.move_list
            attack_list = self.checker_selected.kill_list

            # Removing positions from move list, if checker can attack:
            if len(attack_list) > 0:
                move_list = []

            # Highlighting move positions and attack positions:
            highlight_move()
            highlight_attack()

        arcade.start_render()

        self.board.display(render_checkers=True)
        if self.checker_selected is not None:
            display_highlighted_tiles()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.KEY_1:
            self.active_player = 1
        elif symbol == arcade.key.KEY_2:
            self.active_player = 2

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        def handle_board_click(coordinates):

            def try_moving():
                if self.checker_selected.can_kill:
                    try_attacking()
                else:
                    if self.__player_must_attack():
                        print('Unable to move. You have a checker, that should perform an attack!')
                        self.checker_selected = None
                        checkers_to_attack = []
                        for row in mapping.SURFACE_GRID:
                            for column in mapping.SURFACE_GRID[row]:
                                checker = mapping.SURFACE_GRID[row][column]
                                if checker is not None:
                                    if (checker.color == 'White' and self.active_player == 1 or
                                        checker.color == 'Black' and self.active_player == 2):
                                        if checker.can_kill:
                                            checkers_to_attack.append(checker)
                        self.checker_selected = random.choice(checkers_to_attack)
                    else:
                        if clicked_position in self.checker_selected.move_list:
                            self.checker_selected.move(clicked_position)
                            self.__board_update()
                            self.__next_player_turn()
                            self.checker_selected = None

            def try_attacking():
                if clicked_position in self.checker_selected.kill_list:
                    self.checker_selected.move(clicked_position)
                    self.__board_update()
                    if not self.checker_selected.can_kill:
                        self.__next_player_turn()
                        self.checker_selected = None

            if test.coordinates_are_valid(coordinates):
                if test.coordinates_in_board_boundaries(coordinates):
                    checker_clicked = get.checker_by_coordinates(coordinates)
                    if checker_clicked is None:
                        if self.checker_selected is not None:
                            clicked_position = convert.coordinates_to_board_position(coordinates)
                            if self.checker_selected.can_move or self.checker_selected.can_kill:
                                try_moving()
                    else:
                        if not (self.active_player == 1 and checker_clicked.color.lower() == 'white' or
                                self.active_player == 2 and checker_clicked.color.lower() == 'black'):
                            self.checker_selected = None
                        else:
                            if checker_clicked == self.checker_selected:
                                self.checker_selected = None
                            else:
                                self.checker_selected = checker_clicked

        def handle_board_click_dev(coordinates):
            if test.coordinates_are_valid(coordinates):
                if test.coordinates_in_board_boundaries(coordinates):
                    checker_clicked = get.checker_by_coordinates(coordinates)
                    clicked_position = convert.coordinates_to_board_position(coordinates)
                    if test.position_can_be_used(clicked_position):
                        clicked_row, clicked_column = clicked_position[0], clicked_position[1]
                        if checker_clicked is None:
                            new_checker = spawn.checker(spawn_position=clicked_position,
                                                        spawn_color='White',
                                                        spawn_queen=False)
                            mapping.SURFACE_GRID[clicked_row][clicked_column] = new_checker
                        else:
                            if checker_clicked.queen:
                                if checker_clicked.color == 'White':
                                    checker_clicked.color = 'White' if checker_clicked.color == 'Black' else 'Black'
                                else:
                                    mapping.SURFACE_GRID[clicked_row][clicked_column] = None
                            else:
                                if checker_clicked.color == 'White':
                                    checker_clicked.color = 'White' if checker_clicked.color == 'Black' else 'Black'
                                else:
                                    checker_clicked.color = 'White' if checker_clicked.color == 'Black' else 'Black'
                                    checker_clicked.promote()
                        self.board.update()

        click_coordinates = [x, y]

        # Board surface clicked:
        if test.coordinates_in_board_boundaries(click_coordinates):
            if button == arcade.MOUSE_BUTTON_LEFT:
                handle_board_click(click_coordinates)
            else:
                handle_board_click_dev(click_coordinates)

        # UI panel clicked:
        else:
            pass

    def update(self, delta_time: float):
        pass

shell = Shell()
shell.setup()