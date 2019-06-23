import arcade
from app import settings, session
from app.board import mono as board, convert, test, get, mapping
from app.checker import spawn
from app.ui import mono as ui, click
from app.ui.elements.button import Button
from tools.pencil import stamp
from tools import console


class Shell(arcade.Window):

    def __init__(self):

        super().__init__(
            width=settings.GAME_WINDOW_WIDTH,
            height=settings.GAME_WINDOW_HEIGHT,
            title=settings.GAME_WINDOW_TITLE,
            fullscreen=settings.GAME_WINDOW_FULLSCREEN,
            resizable=settings.GAME_WINDOW_RESIZABLE,
            update_rate=settings.GAME_WINDOW_UPDATE_RATE,
            antialiasing=settings.GAME_WINDOW_ANTIALIASING
        )

        console.echo(
            message='Initializing application game window ({width}x{height}px)...'.format(
                width=self.width,
                height=self.height))

        self.__dev_mode = session.DEV_MODE
        self.__test_mode = session.TEST_MODE
        self.__debug_mode = session.DEBUG_MODE

        self.board = board.Board()
        self.player = None
        self.ui = ui.UI()

        self.active_player = 1                          # 1 = White, 2 = Black;
        self.active_checker = None                      # None, if deselected;

        self.highlight_checkers_move = False
        self.highlight_checkers_attack = False

        self.display_checkers = False

        self.game_running = False
        self.game_paused = False



    @staticmethod
    def setup():
        # Shell specific setup:
        pass

        # Arcade preload functions:
        arcade.set_background_color(color=settings.GAME_WINDOW_BACKGROUND_COLOR)
        arcade.run()

    def start_game(self):
        self.game_running = True
        self.game_paused = False
        self.__board_reset()
        self.active_player = 1
        self.ui.show_clockface()
        self.ui.clockface.stopwatch.start()

    def restart_game(self):
        self.ui.clockface.stopwatch.stop()
        self.ui.clockface.stopwatch.reset()
        self.start_game()

    def stop_game(self):
        self.ui.clockface.stopwatch.stop()
        self.game_running = False
        self.game_paused = False
        self.active_player = 1

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
        if cannot_move:
            console.echo(
                message='Player {index} is unable to move'.format(
                    index=self.active_player),
                level=2)
        return cannot_move

    def __player_has_no_checkers(self):
        no_checkers = True
        for row in mapping.SURFACE_GRID:
            for column in mapping.SURFACE_GRID[row]:
                position = [row, column]
                checker = get.checker_by_position(position)
                if checker is not None:
                    if checker.color == self.__player_color():
                        no_checkers = False
        if no_checkers:
            console.echo(
                message='Player {index} has no checkers remaining on the board!'.format(
                    index=self.active_player),
                level=3)
        return no_checkers

    def __next_player_turn(self):
        self.active_player = 2 if self.active_player == 1 else 1
        console.echo(
            message='Switched to player {index} turn'.format(
                index=self.active_player),
            level=1)
        if self.__player_cannot_move():
            if self.__player_has_no_checkers():
                if self.active_player == 1:
                    self.ui.set_mode(mode=7)
                else:
                    self.ui.set_mode(mode=6)
            else:
                self.ui.set_mode(mode=9)
            self.stop_game()

    def __board_clear(self):
        self.board.clear()

    def __board_fill(self):
        self.board.fill()
        self.board.update()

    def __board_reset(self):
        console.echo(
            message='Resetting board surface...',
            level=2)
        self.board.update()
        self.__board_clear()
        self.__board_fill()
        self.__board_update()

    def __board_update(self):
        console.echo(
            message='Updating board checkers...',
            level=2)
        self.board.update()

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
                        stamp.checker_higlight_attack(ch_coord_x=coordinates[0],
                                                      ch_coord_y=coordinates[1])

            def highlight_moves():
                for checker in checkers_move_list:
                    if checker.color == self.__player_color():
                        coordinates = checker.coordinates
                        stamp.checker_higlight_move(ch_coord_x=coordinates[0],
                                                    ch_coord_y=coordinates[1])

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
                    stamp.checker_higlight_move(ch_coord_x=checker_coordinates[0],
                                                ch_coord_y=checker_coordinates[1])
                for move_position in move_list:
                    coordinates = convert.board_position_to_coordinates(conv_position=move_position)
                    move_position_coord_x, move_position_coord_y = coordinates
                    stamp.board_tile_highlight_move(tile_coord_x=move_position_coord_x,
                                                    tile_coord_y=move_position_coord_y)

            def highlight_attack_tiles():
                if self.active_checker.can_kill:
                    checker_coordinates = self.active_checker.coordinates
                    stamp.checker_higlight_attack(ch_coord_x=checker_coordinates[0],
                                                  ch_coord_y=checker_coordinates[1])
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
        if self.display_checkers:
            self.board.display_checkers()

        # UI rendering:
        self.ui.display()

    def on_key_press(self, symbol: int, modifiers: int):

        def enable_hint():
            self.highlight_checkers_move = True
            self.highlight_checkers_attack = True


        # Main menu:
        if self.ui.active_mode == 0:
            if symbol == arcade.key.SPACE:
                self.ui.set_mode(mode=2)
                self.display_checkers = True
                self.start_game()
            elif symbol == arcade.key.ESCAPE:
                self.ui.set_mode(mode=8)

        # Settings menu:
        elif self.ui.active_mode == 1:
            if symbol == arcade.key.ESCAPE:
                if not self.game_running:
                    self.ui.set_mode(mode=0)
                else:
                    self.ui.set_mode(mode=3)

        # Active game mode:
        elif self.ui.active_mode == 2:
            if symbol == arcade.key.H:
                enable_hint()
            elif symbol == arcade.key.ESCAPE:
                self.game_paused = True
                self.ui.clockface.stopwatch.pause()
                self.ui.set_mode(mode=3)

        # Paused game mode:
        elif self.ui.active_mode == 3:
            if symbol == arcade.key.ESCAPE:
                if self.game_paused:
                    self.game_paused = False
                self.ui.clockface.stopwatch.unpause()
                self.ui.set_mode(mode=2)

        # Start new game confirmation menu:
        elif self.ui.active_mode == 4:
            if symbol == arcade.key.SPACE:
                self.restart_game()
                self.ui.set_mode(mode=2)
            elif symbol == arcade.key.ESCAPE:
                self.ui.set_mode(mode=3)

        # End current game confirmation menu:
        elif self.ui.active_mode == 5:
            if symbol == arcade.key.SPACE:
                self.stop_game()
                self.ui.set_mode(mode=7)
            elif symbol == arcade.key.ESCAPE:
                self.ui.set_mode(mode=3)

        # Game results (Game won):
        elif self.ui.active_mode == 6:
            if symbol == arcade.key.SPACE:
                self.ui.clockface.stopwatch.stop()
                self.ui.clockface.stopwatch.reset()
                self.ui.hide_clockface()
                self.display_checkers = False
                self.ui.set_mode(mode=0)
            elif symbol == arcade.key.ESCAPE:
                self.ui.set_mode(mode=8)

        # Game results (Game lost/force end):
        elif self.ui.active_mode == 7:
            if symbol == arcade.key.SPACE:
                self.ui.clockface.stopwatch.stop()
                self.ui.clockface.stopwatch.reset()
                self.ui.hide_clockface()
                self.display_checkers = False
                self.ui.set_mode(mode=0)
            elif symbol == arcade.key.ESCAPE:
                self.ui.set_mode(mode=8)

        # Quit confirmation menu:
        elif self.ui.active_mode == 8:
            if symbol == arcade.key.SPACE:
                quit()
            elif symbol == arcade.key.ESCAPE:
                prev_mode = self.ui.previous_mode
                self.ui.set_mode(mode=prev_mode)

        # Game results (Game draw):
        elif self.ui.active_mode == 9:
            if symbol == arcade.key.SPACE:
                self.ui.clockface.stopwatch.stop()
                self.ui.clockface.stopwatch.reset()
                self.ui.hide_clockface()
                self.display_checkers = False
                self.ui.set_mode(mode=0)
            elif symbol == arcade.key.ESCAPE:
                self.ui.set_mode(mode=8)

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
                console.echo(
                    message='Highlighting possible moves...',
                    level=2)

            def select_checker(checker_object):
                self.active_checker = checker_object
                console.echo(
                    message='Selected new checker',
                    level=3)

            def deselect_checker():
                if self.active_checker is not None:
                    self.active_checker = None
                    console.echo(
                        message='Deselected current checker',
                        level=2)

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
                        console.echo(
                            message='Unable to move current checker. There is a checker that can attack!',
                            level=3)
                        deselect_checker()
                        force_hint()
                    else:
                        if clicked_position in self.active_checker.move_list:
                            self.active_checker.move(clicked_position)
                            self.__board_update()
                            self.__next_player_turn()
                            deselect_checker()
                        else:
                            console.echo(
                                message='Unable to move to {position}. Position {position} is out of reach'.format(
                                    position=convert.board_position_to_alphanumeric_index(clicked_position)),
                                level=3)
                            deselect_checker()

            def try_attacking():
                if clicked_position in self.active_checker.kill_list:
                    self.active_checker.move(clicked_position)
                    self.__board_update()
                    console.echo(
                        message='Checking if player can attack...',
                        level=1)
                    if not self.active_checker.can_kill:
                        console.echo(
                            message='Player {index} is unable to continue attacking!'.format(
                                index=self.active_player),
                            level=2 )
                        self.__next_player_turn()
                        deselect_checker()
                else:
                    position_index = convert.board_position_to_alphanumeric_index(clicked_position)
                    error_reason = 'Checker must attack first!'
                    if clicked_position not in self.active_checker.move_list:
                        error_reason = f'Position {position_index} is out of reach!'
                    console.echo(
                        message='Unable to move to {position}. {reason}'.format(
                            position=position_index,
                            reason=error_reason),
                        level=3)

            if test.coordinates_are_valid(coordinates):
                if test.coordinates_in_board_boundaries(coordinates):
                    self.__remove_all_highlights()
                    checker_clicked = get.checker_by_coordinates(coordinates)
                    if checker_clicked is None:
                        console.echo(
                            message='Empty tile clicked',
                            level=2)
                        if self.active_checker is not None:
                            clicked_position = convert.coordinates_to_board_position(coordinates)
                            if self.active_checker.can_move or self.active_checker.can_kill:
                                try_moving()
                    else:
                        console.echo(
                            message='{checker} clicked at {position}'.format(
                                checker=checker_clicked,
                                position=checker_clicked.index),
                            level=2)
                        if not assert_player_owns_checker(checker_clicked):
                            console.echo(
                                message='Unable to select opponent\'s checker!',
                                level=3
                            )
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

        def handle_panel_click(coordinates):

            def show_hint():
                console.echo(
                    message='Hint enabled. Highlighting possible moves...',
                    level=3)
                if not self.highlight_checkers_move:
                    self.highlight_checkers_move = True
                if not self.highlight_checkers_attack:
                    self.highlight_checkers_attack = True

            def hide_hint():
                console.echo(
                    message='Hint disabled. Removing highlights...',
                    level=3)
                if self.highlight_checkers_move:
                    self.highlight_checkers_move = False
                if self.highlight_checkers_attack:
                    self.highlight_checkers_attack = False

            def hint_enabled():
                hint_status = False
                if self.highlight_checkers_move and self.highlight_checkers_attack:
                    hint_status = True
                return hint_status

            def console_echo_button_click(button_caption: str):
                console.echo(
                    message='Button {caption} clicked'.format(
                        caption=button_caption),
                    level=2)

            for ui_element in self.ui.collection[self.ui.active_mode]:
                if isinstance(ui_element, Button):
                    if click.coordinates_in_button_boundaries(coordinates, ui_element):
                        # Main menu:
                        if self.ui.active_mode == 0:
                            if ui_element.ID == settings.BUTTON_ID_START_GAME:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=2)
                                self.start_game()
                                self.display_checkers = True
                            elif ui_element.ID == settings.BUTTON_ID_SETTINGS:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=1)
                            elif ui_element.ID == settings.BUTTON_ID_QUIT:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=8)

                        # Settings menu:
                        elif self.ui.active_mode == 1:
                            if ui_element.ID == settings.BUTTON_ID_BACK:
                                console_echo_button_click(ui_element.caption)
                                if not self.game_running:
                                    self.ui.set_mode(mode=0)
                                else:
                                    self.ui.set_mode(mode=3)

                        # Active game mode:
                        elif self.ui.active_mode == 2:
                            if ui_element.ID == settings.BUTTON_ID_PAUSE:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=3)
                                self.game_paused = True
                                self.ui.clockface.stopwatch.pause()
                            elif ui_element.ID == settings.BUTTON_ID_HINT:
                                console_echo_button_click(ui_element.caption)
                                if hint_enabled():
                                    hide_hint()
                                else:
                                    show_hint()
                            elif ui_element.ID == settings.BUTTON_ID_UNDO:
                                console_echo_button_click(ui_element.caption)
                                pass # TODO: Add undo function:

                        # Paused game mode:
                        elif self.ui.active_mode == 3:
                            if ui_element.ID == settings.BUTTON_ID_RESUME:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=2)
                                if self.game_paused:
                                    self.game_paused = False
                                self.ui.clockface.stopwatch.unpause()
                            elif ui_element.ID == settings.BUTTON_ID_RESTART_GAME:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=4)
                            elif ui_element.ID == settings.BUTTON_ID_SETTINGS:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=1)
                            elif ui_element.ID == settings.BUTTON_ID_MAIN_MENU:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=5)
                            elif ui_element.ID == settings.BUTTON_ID_QUIT:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=8)

                        # Start new game confirmation menu:
                        elif self.ui.active_mode == 4:
                            if ui_element.ID == settings.BUTTON_ID_YES:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=2)
                                self.restart_game()
                            elif ui_element.ID == settings.BUTTON_ID_NO:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=3)

                        # End current game confirmation menu:
                        elif self.ui.active_mode == 5:
                            if ui_element.ID == settings.BUTTON_ID_YES:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=7)
                                self.stop_game()
                            elif ui_element.ID == settings.BUTTON_ID_NO:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=3)

                        # Game results (Game won):
                        elif self.ui.active_mode == 6:
                            if ui_element.ID == settings.BUTTON_ID_CONTINUE:
                                console_echo_button_click(ui_element.caption)
                                self.ui.clockface.stopwatch.stop()
                                self.ui.clockface.stopwatch.reset()
                                self.ui.hide_clockface()
                                self.display_checkers = False
                                self.ui.set_mode(mode=0)
                            elif ui_element.ID == settings.BUTTON_ID_QUIT:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=8)

                        # Game results (Game lost/force end):
                        elif self.ui.active_mode == 7:
                            if ui_element.ID == settings.BUTTON_ID_CONTINUE:
                                console_echo_button_click(ui_element.caption)
                                self.ui.clockface.stopwatch.stop()
                                self.ui.clockface.stopwatch.reset()
                                self.ui.hide_clockface()
                                self.display_checkers = False
                                self.ui.set_mode(mode=0)
                            elif ui_element.ID == settings.BUTTON_ID_QUIT:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=8)

                        # Quit confirmation menu:
                        elif self.ui.active_mode == 8:
                            if ui_element.ID == settings.BUTTON_ID_YES:
                                console_echo_button_click(ui_element.caption)
                                quit()
                            elif ui_element.ID == settings.BUTTON_ID_NO:
                                console_echo_button_click(ui_element.caption)
                                prev_mode = self.ui.previous_mode
                                self.ui.set_mode(mode=prev_mode)

                        # Game results (Game draw):
                        elif self.ui.active_mode == 9:
                            if ui_element.ID == settings.BUTTON_ID_CONTINUE:
                                console_echo_button_click(ui_element.caption)
                                self.ui.clockface.stopwatch.stop()
                                self.ui.clockface.stopwatch.reset()
                                self.ui.hide_clockface()
                                self.display_checkers = False
                                self.ui.set_mode(mode=0)
                            elif ui_element.ID == settings.BUTTON_ID_QUIT:
                                console_echo_button_click(ui_element.caption)
                                self.ui.set_mode(mode=8)


        click_coordinates = [x, y]
        console.echo(
            message='Registered {button} click at {coordinates}'.format(
                button='LMB' if button == arcade.MOUSE_BUTTON_LEFT else \
                       'RMB' if button == arcade.MOUSE_BUTTON_RIGHT else \
                       'MMB' if button == arcade.MOUSE_BUTTON_MIDDLE else \
                       'unregistered mouse button',
                coordinates=f'{x}:{y}'),
            level=1)

        if button == arcade.MOUSE_BUTTON_LEFT:
            if test.coordinates_in_board_boundaries(click_coordinates):
                if self.game_running and not self.game_paused:
                    handle_board_click(click_coordinates)
            else:
                handle_panel_click(click_coordinates)
        else:
            if session.DEV_MODE:
                handle_board_click_dev(click_coordinates)


    def update(self, delta_time: float):
        pass

shell = Shell()
shell.setup()