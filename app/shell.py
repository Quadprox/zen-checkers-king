import arcade
from app import settings, session
from app.board import mono as board, convert, test, get, mapping
from app.checker import spawn
from app.ui import mono as ui
from tools.pencil import stamp


class Shell(arcade.Window):

    def __init__(self):

        self.board = board.Board()
        self.player = None
        self.ui = ui.UI()

        super().__init__(
            width=settings.GAME_WINDOW_WIDTH,
            height=settings.GAME_WINDOW_HEIGHT,
            title=settings.GAME_WINDOW_TITLE,
            fullscreen=settings.GAME_WINDOW_FULLSCREEN,
            resizable=settings.GAME_WINDOW_RESIZABLE,
            update_rate=settings.GAME_WINDOW_UPDATE_RATE,
            antialiasing=settings.GAME_WINDOW_ANTIALIASING
        )

        self.__dev_mode = session.DEV_MODE
        self.__test_mode = session.TEST_MODE
        self.__debug_mode = session.DEBUG_MODE

        self.active_player = 1                          # 1 = White, 2 = Black;
        self.active_checker = None                      # None, if deselected;

        self.highlight_checkers_move = False
        self.highlight_checkers_attack = False

        self.game_running = False
        self.game_paused = False


    def setup(self):
        self.__board_reset()
        self.ui.set_mode(mode=0)

        # Arcade preload functions:
        arcade.set_background_color(color=settings.GAME_WINDOW_BACKGROUND_COLOR)
        arcade.run()

    def __remove_all_highlights(self):
        self.highlight_checkers_attack = False
        self.highlight_checkers_move = False

    def __player_color(self):
        player_color = 'White' if self.active_player == 1 else 'Black'
        return player_color

    def __player_must_attack(self):
        must_attack = False
        attack_checkers = get.checkers_that_can_attack()
        for checker in attack_checkers:
            if checker.color == self.__player_color():
                must_attack = True
                break
        return must_attack

    def __player_cannot_move(self):
        cannot_move = True
        move_checkers = get.checkers_that_can_move()
        for checker in move_checkers:
            if checker.color == self.__player_color():
                if checker.can_move:
                    cannot_move = False
                    break
        return cannot_move

    def __next_player_turn(self):
        self.active_player = 2 if self.active_player == 1 else 1
        if self.__player_cannot_move():
            self.__board_reset()

    def __board_clear(self):
        self.board.clear()

    def __board_fill(self):
        self.board.fill()
        self.board.update()

    def __board_reset(self):
        self.__board_clear()
        self.__board_fill()
        self.__board_update()

    def __board_update(self):
        self.board.update()

    def __ui_switch_mode(self, mode: int):

        def end_current_game():
            self.__board_reset()
            self.__board_update()
            self.active_player = 1
            self.ui.clockface.stopwatch.reset()
            if self.game_running:
                self.game_running = False

        def restart_game():
            end_current_game()
            self.ui.clockface.stopwatch.start()
            if not self.game_running:
                self.game_running = True
            if self.game_paused:
                self.game_paused = False

        # Main menu
        if self.ui.active_mode == 0:

            # --> Active game (start new):
            if mode == 2:
                end_current_game()
                self.ui.clockface.stopwatch.start()
                if not self.game_running:
                    self.game_running = True

            # --> Game won:
            elif mode == 6:
                end_current_game()

            # --> Game lost:
            elif mode == 7:
                end_current_game()

            # --> Quit:
            elif mode == -1:
                quit()

        # Settings menu:
        elif self.ui.active_mode == 1:
            pass

        # Active game:
        elif self.ui.active_mode == 2:

            # --> Pause menu:
            if mode == 3:
                if not self.game_paused:
                    self.game_paused = True
                self.ui.clockface.stopwatch.pause()

        # Pause menu:
        elif self.ui.active_mode == 3:

            # --> Active game (unpause):
            if mode == 2:
                if self.game_paused:
                    self.game_paused = False
                self.ui.clockface.stopwatch.unpause()

        # Start new game menu confirmation:
        elif self.ui.active_mode == 4:

            # --> Active game (start new):
            if mode == 2:
                restart_game()

        # End current game menu confirmation:
        elif self.ui.active_mode == 5:

            # --> Game lost (end current):
            if mode == 7:
                end_current_game()

        # Game won:
        elif self.ui.active_mode == 6:
            pass

        # Game won
        elif self.ui.active_mode == 7:
            pass

        self.ui.set_mode(mode)



    def on_draw(self):

        def display_highlighted_checkers():

            def remove_duplicates():
                nonlocal checkers_move_list
                for checker in checkers_attack_list:
                    if checker in checkers_move_list:
                        checkers_move_list.remove(checker)

            def highlight_attack():
                for checker in checkers_attack_list:
                    if checker.color == self.__player_color():
                        coordinates = checker.coordinates
                        stamp.board_tile_highlight_attack(tile_coord_x=coordinates[0],
                                                          tile_coord_y=coordinates[1])

            def highlight_moves():
                for checker in checkers_move_list:
                    if checker.color == self.__player_color():
                        coordinates = checker.coordinates
                        stamp.board_tile_highlight_move(tile_coord_x=coordinates[0],
                                                        tile_coord_y=coordinates[1])

            checkers_move_list = get.checkers_that_can_move()
            checkers_attack_list = get.checkers_that_can_attack()
            if self.highlight_checkers_move and self.highlight_checkers_attack:
                remove_duplicates()
                highlight_attack()
                highlight_moves()
            else:
                if self.highlight_checkers_move:
                    highlight_moves()
                if self.highlight_checkers_attack:
                    highlight_attack()

        def display_highlighted_tiles():

            def highlight_move_tiles():
                if self.active_checker.can_move and not self.active_checker.can_kill:
                    checker_coordinates = self.active_checker.coordinates
                    stamp.board_tile_highlight_move(tile_coord_x=checker_coordinates[0],
                                                    tile_coord_y=checker_coordinates[1])
                for move_position in move_list:
                    coordinates = convert.board_position_to_coordinates(conv_position=move_position)
                    move_position_coord_x, move_position_coord_y = coordinates
                    stamp.board_tile_highlight_move(tile_coord_x=move_position_coord_x,
                                                    tile_coord_y=move_position_coord_y)

            def highlight_attack_tiles():
                if self.active_checker.can_kill:
                    checker_coordinates = self.active_checker.coordinates
                    stamp.board_tile_highlight_attack(tile_coord_x=checker_coordinates[0],
                                                      tile_coord_y=checker_coordinates[1])
                for attack_position in attack_list:
                    coordinates = convert.board_position_to_coordinates(conv_position=attack_position)
                    move_position_coord_x, move_position_coord_y = coordinates
                    stamp.board_tile_highlight_attack(tile_coord_x=move_position_coord_x,
                                                      tile_coord_y=move_position_coord_y)

            # Collecting move list and attack list:
            move_list = self.active_checker.move_list
            attack_list = self.active_checker.kill_list

            # Removing positions from move list, if checker can attack:
            if len(attack_list) > 0:
                move_list = []

            # Highlighting move positions and attack positions:
            highlight_move_tiles()
            highlight_attack_tiles()

        arcade.start_render()

        # Board rendering:
        self.board.display()
        if self.highlight_checkers_attack or self.highlight_checkers_move:
            display_highlighted_checkers()
        else:
            if self.active_checker is not None:
                if not self.highlight_checkers_attack or self.highlight_checkers_move:
                    display_highlighted_tiles()
        self.board.display_checkers()

        # UI rendering:
        self.ui.display()

    def on_key_press(self, symbol: int, modifiers: int):

        def enable_hint():
            self.highlight_checkers_move = True
            self.highlight_checkers_attack = True

        if symbol == arcade.key.KEY_0:
            self.__ui_switch_mode(mode=0)
        elif symbol == arcade.key.KEY_1:
            self.__ui_switch_mode(mode=1)
        elif symbol == arcade.key.KEY_2:
            self.__ui_switch_mode(mode=2)
        elif symbol == arcade.key.KEY_3:
            self.__ui_switch_mode(mode=3)
        elif symbol == arcade.key.KEY_4:
            self.__ui_switch_mode(mode=4)
        elif symbol == arcade.key.KEY_5:
            self.__ui_switch_mode(mode=5)
        elif symbol == arcade.key.KEY_6:
            self.__ui_switch_mode(mode=6)
        elif symbol == arcade.key.KEY_7:
            self.__ui_switch_mode(mode=7)

        elif symbol == arcade.key.H:
            enable_hint()


    def on_key_release(self, symbol: int, modifiers: int):

        def disable_hint():
            self.highlight_checkers_move = False
            self.highlight_checkers_attack = False

        if symbol == arcade.key.H:
            disable_hint()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        def handle_board_click(coordinates):

            def force_hint():
                if self.highlight_checkers_move:
                    self.highlight_checkers_move = False
                self.highlight_checkers_attack = True

            def select_checker(checker_object):
                self.active_checker = checker_object

            def deselect_checker():
                self.active_checker = None

            def assert_player_owns_checker(checker_object):
                result = False
                if self.__player_color() == checker_object.color:
                    result = True
                return result

            def try_moving():
                if self.active_checker.can_kill:
                    try_attacking()
                else:
                    if self.__player_must_attack():
                        deselect_checker()
                        force_hint()
                    else:
                        if clicked_position in self.active_checker.move_list:
                            self.active_checker.move(clicked_position)
                            self.__board_update()
                            self.__next_player_turn()
                            deselect_checker()

            def try_attacking():
                if clicked_position in self.active_checker.kill_list:
                    self.active_checker.move(clicked_position)
                    self.__board_update()
                    if not self.active_checker.can_kill:
                        self.__next_player_turn()
                        deselect_checker()

            if test.coordinates_are_valid(coordinates):
                if test.coordinates_in_board_boundaries(coordinates):
                    self.__remove_all_highlights()
                    checker_clicked = get.checker_by_coordinates(coordinates)
                    if checker_clicked is None:
                        if self.active_checker is not None:
                            clicked_position = convert.coordinates_to_board_position(coordinates)
                            if self.active_checker.can_move or self.active_checker.can_kill:
                                try_moving()
                    else:
                        if not assert_player_owns_checker(checker_clicked):
                            deselect_checker()
                        else:
                            if checker_clicked == self.active_checker:
                                deselect_checker()
                            else:
                                select_checker(checker_clicked)

        def handle_board_click_dev(coordinates):

            def spawn_checker():
                new_checker = spawn.checker(spawn_position=clicked_position,
                                            spawn_color='White',
                                            spawn_queen=False)
                new_checker.dev = True
                mapping.SURFACE_GRID[clicked_row][clicked_column] = new_checker

            def switch_color(checker_object):
                checker_object.color = 'White' if checker_object.color == 'Black' else 'Black'

            def promote_checker(checker_object):
                checker_object.promote()

            def remove_checker():
                mapping.SURFACE_GRID[clicked_row][clicked_column] = None

            if test.coordinates_are_valid(coordinates):
                if test.coordinates_in_board_boundaries(coordinates):
                    checker_clicked = get.checker_by_coordinates(coordinates)
                    clicked_position = convert.coordinates_to_board_position(coordinates)

                    if test.position_can_be_used(clicked_position):
                        clicked_row, clicked_column = clicked_position
                        if checker_clicked is None:
                            spawn_checker()
                        else:
                            if checker_clicked.queen:
                                if checker_clicked.color == 'White':
                                    switch_color(checker_clicked)
                                else:
                                    remove_checker()
                            else:
                                if checker_clicked.color == 'White':
                                    switch_color(checker_clicked)
                                else:
                                    switch_color(checker_clicked)
                                    promote_checker(checker_clicked)
                        self.board.update()

        click_coordinates = [x, y]

        # Board surface clicked:
        if test.coordinates_in_board_boundaries(click_coordinates):
            if button == arcade.MOUSE_BUTTON_LEFT:

                # Checking if game is running and not paused to process the click command:
                if self.game_running and not self.game_paused:
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