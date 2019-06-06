import arcade
from app import settings, session
from app.board import mono as board, convert, test, get, mapping
from app.checker import spawn
from tools import stamp


class Shell(arcade.Window):

    def __init__(self):

        self.board = board.Board()

        self.board.update()
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

        self.active_player = 1              # 1 = White, 2 = Black
        self.checker_selected = None
        self.tile_hovered = None


    def setup(self):
        arcade.set_background_color(color=settings.GAME_WINDOW_BACKGROUND_COLOR)
        arcade.run()

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

            # Removing duplicate positions from move list:
            if len(attack_list) > 0:
                for attack_position in attack_list:
                    if attack_position in move_list:
                        move_list.remove(attack_position)

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

            def clicked():
                result = False
                if test.coordinates_are_valid(coordinates):
                    if test.coordinates_in_board_boundaries(coordinates):
                        result = True
                return result

            def clicked_same_color(checker_object):
                result = True if self.active_player == 1 and checker_object.color.lower() == 'white' or \
                                 self.active_player == 2 and checker_object.color.lower() == 'black' else False
                return result

            def clicked_same_checker(checker_object):
                result = False
                if checker_object == self.checker_selected:
                    result = True
                return result

            def select(checker_object):
                self.checker_selected = checker_object

            def deselect():
                self.checker_selected = None

            if clicked():
                checker_clicked = get.checker_by_coordinates(coordinates)
                if checker_clicked is None:
                    deselect()
                else:
                    if not clicked_same_color(checker_clicked):
                        deselect()
                    else:
                        if clicked_same_checker(checker_clicked):
                            deselect()
                        else:
                            select(checker_clicked)
                            print(checker_clicked,
                                  '\nmoves:', checker_clicked.move_list,
                                  '\nkill:', checker_clicked.kill_list)

        def handle_board_click_dev(coordinates):

            def clicked():
                result = False
                if test.coordinates_are_valid(coordinates):
                    if test.coordinates_in_board_boundaries(coordinates):
                        result = True
                return result

            def rotate_color(checker):
                checker.color = 'White' if checker.color == 'Black' else 'Black'

            def promote_checker(checker):
                checker.promote()

            def remove_checker(checker):
                row, column = checker.position[0], checker.position[1]
                mapping.SURFACE_GRID[row][column] = None

            if clicked():
                checker_clicked = get.checker_by_coordinates(coordinates)
                clicked_position = convert.coordinates_to_board_position(coordinates)
                clicked_row, clicked_column = clicked_position[0], clicked_position[1]
                if checker_clicked is None:
                    new_checker = spawn.checker(spawn_position=clicked_position,
                                                spawn_color='White',
                                                spawn_queen=False)
                    mapping.SURFACE_GRID[clicked_row][clicked_column] = new_checker
                else:
                    if checker_clicked.queen:
                        if checker_clicked.color == 'White':
                            rotate_color(checker_clicked)
                        else:
                            remove_checker(checker_clicked)
                    else:
                        if checker_clicked.color == 'White':
                            rotate_color(checker_clicked)
                        else:
                            rotate_color(checker_clicked)
                            promote_checker(checker_clicked)
                self.board.update()


        click_coordinates = [x, y]
        if test.coordinates_in_board_boundaries(click_coordinates):
            if button == arcade.MOUSE_BUTTON_LEFT:
                handle_board_click(click_coordinates)
            else:
                handle_board_click_dev(click_coordinates)
        else:
            pass

    def update(self, delta_time: float):
        pass

shell = Shell()
shell.setup()