import arcade
from app import settings, session
from app.board import mono as board, convert, test, get
from tools import stamp


class Shell(arcade.Window):

    def __init__(self):

        self.board = board.Board()
        self.board.fill()
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
                        del move_list[attack_position]

            # Highlighting move positions and attack positions:
            highlight_move()
            highlight_attack()

        arcade.start_render()

        self.board.display(render_checkers=True)
        if self.checker_selected is not None:
            if self.checker_selected.can_move:
                display_highlighted_tiles()

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        def listen_if_checker_was_clicked(coordinates):

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

        click_coordinates = [x, y]
        if test.coordinates_in_board_boundaries(click_coordinates):
            listen_if_checker_was_clicked(click_coordinates)
        else:
            pass

    def update(self, delta_time: float):
        pass

shell = Shell()
shell.setup()