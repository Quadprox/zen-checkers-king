import arcade
import app.settings as settings
import tools.pencil.stamp as stamp
import random
import app.board.mono as board
import app.ui.mono as ui


CHECKER_SHOWCASE_POS_X = 64
CHECKER_SHOWCASE_POS_Y = 64


def __initialize(showcase_object: str):
    arcade.open_window(
        width=settings.BOARD_SIDE_LEN if showcase_object == 'board' else
              settings.GAME_WINDOW_WIDTH if showcase_object in ('project', 'panel') else
              CHECKER_SHOWCASE_POS_X * 2 if showcase_object == 'checker' else 0,
        height=settings.BOARD_SIDE_LEN if showcase_object == 'board' else
               settings.GAME_WINDOW_HEIGHT if showcase_object in ('project', 'panel') else
               CHECKER_SHOWCASE_POS_Y * 2 if showcase_object == 'checker' else 0,
        window_title=f'{settings.PROJECT_NAME} ({showcase_object} showcase demo)',
        resizable=False,
        antialiasing=False,
    )


def __start_render():
    arcade.set_background_color(settings.ERROR_COLOR_MAIN)
    arcade.start_render()


def __finish_render():
    arcade.finish_render()
    arcade.run()


def board_surface(filled: bool = False):
    __initialize(showcase_object='board')
    __start_render()
    if filled:
        board.Board().fill()
    board.Board().display()
    __finish_render()


def checker_surface():
    __initialize(showcase_object='checker')
    __start_render()
    stamp.checker(
        ch_coord_x=CHECKER_SHOWCASE_POS_X,
        ch_coord_y=CHECKER_SHOWCASE_POS_Y,
        ch_color=random.choice(('White', 'Black')),
        ch_queen=random.choice((True, False))
    )
    __finish_render()


def panel_surface():
    __initialize(showcase_object='panel')
    __start_render()
    panel = ui.UI()
    panel.set_mode(mode=1)
    panel.initialize()
    panel.display()
    __finish_render()


def project_surface():
    __initialize(showcase_object='project')
    __start_render()

    # Setting up board (filled with checkers at game start)
    board.Board().fill()
    board.Board().display()

    # Setting up UI panel (active game mode)
    panel = ui.UI()
    panel.set_mode(mode=1)
    panel.initialize()
    panel.display()


panel_surface()