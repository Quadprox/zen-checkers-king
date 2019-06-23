import os
import arcade
from datetime import datetime


# General project information and directories:
PROJECT_NAME = 'Zen Checkers King'
PROJECT_APP_VERSION = '0.7.2'
PROJECT_DIR = os.path.dirname(__file__)
PROJECT_APP_DIR = os.path.dirname(__file__)
PROJECT_TOOLS_DIR = os.path.join(PROJECT_DIR, 'tools')
PROJECT_RESOURCES_DIR = os.path.join(PROJECT_DIR, 'resources')
PROJECT_IMAGES_DIR = os.path.join(PROJECT_RESOURCES_DIR, 'images')

# Special error color palettes:
ERROR_COLOR_MAIN = [235, 35, 35]
ERROR_COLOR_ALT = [235, 35, 145]

# Board tile settings:
TILE_SIDE_LEN = 64
TILE_COLOR_WHITE = [255, 210, 155]
TILE_COLOR_BLACK = [25, 20, 20]
TILE_HIGHLIGHT_COLOR_MOVE = [85, 165, 85]
TILE_HIGHLIGHT_COLOR_ATTACK = [210, 45, 30]
TILE_HIGHLIGHT_SIDE_MODIFIER = 0.85
TILE_HIGHLIGHT_SIDE_LEN = int(TILE_SIDE_LEN * TILE_HIGHLIGHT_SIDE_MODIFIER)
TILE_HIGHLIGHT_BORDER_SIDE_LEN = 2
TILE_COUNT_PER_ROW = 8
TILE_COUNT_PER_COLUMN = 8

# Checker object settings:
CHECKER_RADIUS_OUTER = int(TILE_SIDE_LEN * 0.90 / 2)
CHECKER_RADIUS_INNER = int(CHECKER_RADIUS_OUTER * 0.75)
CHECKER_COLOR_WHITE_MAIN = [230, 230, 225]
CHECKER_COLOR_WHITE_ALT = [200, 200, 200]
CHECKER_COLOR_BLACK_MAIN = [135, 75, 60]
CHECKER_COLOR_BLACK_ALT = [80, 20, 15]
CHECKER_SIMPLE_BORDER_LEN = 4
CHECKER_QUEEN_INDEX_FONT_SIZE = 12
CHECKER_QUEEN_INDEX_FONT_NAME = 'Monospaced'.lower()
CHECKER_QUEEN_INDEX_STYLE_BOLD = False
CHECKER_QUEEN_INDEX_STYLE_ITALIC = True
CHECKER_QUEEN_LINE_WIDTH = CHECKER_SIMPLE_BORDER_LEN
CHECKER_SHADOW_SHIFT_X = 2
CHECKER_SHADOW_SHIFT_Y = 1
CHECKER_SEGMENTS = 64

# Board surface settings:
BOARD_MARGIN_OUTER_LEN = 16
BOARD_MARGIN_INNER_LEN = 2
BOARD_MARGIN_LEN = int(BOARD_MARGIN_OUTER_LEN + BOARD_MARGIN_INNER_LEN)
BOARD_MARGIN_COLOR_OUTER = TILE_COLOR_BLACK
BOARD_MARGIN_COLOR_INNER = TILE_COLOR_WHITE
BOARD_SIDE_LEN = int(BOARD_MARGIN_LEN * 2 + TILE_SIDE_LEN * TILE_COUNT_PER_ROW)
BOARD_POSITION_X = int(BOARD_SIDE_LEN / 2)
BOARD_POSITION_Y = int(BOARD_SIDE_LEN / 2)
BOARD_LETTER_INDEX = 'ABCDEFGH'
BOARD_NUMBER_INDEX = '12345678'
BOARD_INDEX_FONT_SIZE = 10
BOARD_INDEX_FONT_NAME = 'Monospaced'.lower()
BOARD_INDEX_STYLE_BOLD = False
BOARD_INDEX_STYLE_ITALIC = False
BOARD_BOUNDARY_BOTTOM = BOARD_MARGIN_LEN
BOARD_BOUNDARY_TOP = BOARD_SIDE_LEN - BOARD_MARGIN_LEN
BOARD_BOUNDARY_LEFT = BOARD_MARGIN_LEN
BOARD_BOUNDARY_RIGHT = BOARD_SIDE_LEN - BOARD_MARGIN_LEN
BOARD_ROW_COUNT = 8
BOARD_COLUMN_COUNT = 8

# UI panel surface settings:
UI_PANEL_WIDTH = int(TILE_SIDE_LEN * 3.5)
UI_PANEL_HEIGHT = BOARD_SIDE_LEN
UI_PANEL_BACKGROUND_COLOR = CHECKER_COLOR_WHITE_MAIN
UI_PANEL_POSITION_X = int(BOARD_SIDE_LEN + UI_PANEL_WIDTH / 2)
UI_PANEL_POSITION_Y = int(BOARD_SIDE_LEN / 2)

# Game window settings:
GAME_WINDOW_BACKGROUND_COLOR = ERROR_COLOR_MAIN
GAME_WINDOW_WIDTH = BOARD_SIDE_LEN + UI_PANEL_WIDTH
GAME_WINDOW_HEIGHT = BOARD_SIDE_LEN
GAME_WINDOW_TITLE = f'{PROJECT_NAME} v{PROJECT_APP_VERSION}'
GAME_WINDOW_RESIZABLE = False
GAME_WINDOW_FULLSCREEN = False
GAME_WINDOW_UPDATE_RATE = 1/60
GAME_WINDOW_ANTIALIASING = True

# Button surface settings:
BUTTON_MARGIN_X = 8
BUTTON_MARGIN_Y = 12
BUTTON_LARGE_WIDTH = int(UI_PANEL_WIDTH - BUTTON_MARGIN_X * 2)
BUTTON_LARGE_HEIGHT = 42
BUTTON_SMALL_WIDTH = int(UI_PANEL_WIDTH / 2 - (BUTTON_MARGIN_X + BUTTON_MARGIN_X / 2))
BUTTON_SMALL_HEIGHT = BUTTON_LARGE_HEIGHT
BUTTON_BORDER_LEN = 2
BUTTON_BORDER_COLOR = TILE_COLOR_BLACK
BUTTON_FILLED_COLOR = TILE_HIGHLIGHT_COLOR_ATTACK
BUTTON_CAPTION_FONT_SIZE = 24
BUTTON_CAPTION_FONT_NAME = 'georgia'
BUTTON_CAPTION_STYLE_BOLD = False
BUTTON_CAPTION_STYLE_ITALIC = False
BUTTON_CAPTION_COLOR = BUTTON_BORDER_COLOR
BUTTON_SMALL_POSITION_X_LEFT = int(BOARD_SIDE_LEN + BUTTON_MARGIN_X + BUTTON_SMALL_WIDTH / 2)
BUTTON_SMALL_POSITION_X_RIGHT = int(GAME_WINDOW_WIDTH - BUTTON_MARGIN_X - BUTTON_SMALL_WIDTH / 2)
BUTTON_LARGE_POSITION_X_MIDDLE = int(BOARD_SIDE_LEN + UI_PANEL_WIDTH / 2)
BUTTON_ID_START_GAME = 'StartGameButton'
BUTTON_ID_RESTART_GAME = 'RestartGameButton'
BUTTON_ID_SETTINGS = 'SettingsButton'
BUTTON_ID_MAIN_MENU = 'MainMenuButton'
BUTTON_ID_QUIT = 'QuitButton'
BUTTON_ID_HINT = 'HintButton'
BUTTON_ID_UNDO = 'UndoButton'
BUTTON_ID_YES = 'YesButton'
BUTTON_ID_NO = 'NoButton'
BUTTON_ID_PAUSE = 'PauseButton'
BUTTON_ID_RESUME = 'ResumeButton'
BUTTON_ID_BACK = 'BackButton'
BUTTON_ID_CONTINUE = 'ContinueButton'

# Clockface surface settings:
CLOCKFACE_CAPTION_COLOR = TILE_COLOR_BLACK
CLOCKFACE_CAPTION_FONT_SIZE = 42
CLOCKFACE_CAPTION_FONT_NAME = 'Monospaced'.lower()
CLOCKFACE_CAPTION_STYLE_BOLD = False
CLOCKFACE_CAPTION_STYLE_ITALIC = False
CLOCKFACE_POSITION_X = int(BOARD_SIDE_LEN + UI_PANEL_WIDTH / 2)
CLOCKFACE_POSITION_Y = int(UI_PANEL_HEIGHT - 42)

# Menu name caption surface settings:
MENU_CAPTION_POSITION_X = BUTTON_LARGE_POSITION_X_MIDDLE
MENU_CAPTION_COLOR = TILE_COLOR_BLACK
MENU_CAPTION_FONT_SIZE = 22
MENU_CAPTION_FONT_NAME = 'georgia'
MENU_CAPTION_STYLE_BOLD = False
MENU_CAPTION_STYLE_ITALIC = False

# Logo caption surface settings:
LOGO_CAPTION_COLOR = TILE_COLOR_BLACK
LOGO_CAPTION_FONT_NAME = 'georgia'
LOGO_CAPTION_STYLE_BOLD = False
LOGO_CAPTION_STYLE_ITALIC = False

# Divider surface settings:
DIVIDER_LENGTH = int(UI_PANEL_WIDTH - BUTTON_MARGIN_X * 2)
DIVIDER_WIDTH = 2
DIVIDER_COLOR = TILE_COLOR_BLACK
DIVIDER_POSITION_X = int(BOARD_SIDE_LEN + UI_PANEL_WIDTH / 2)

SURFACE_GRID = {}
SURFACE_EMPTY = False



def draw_rectangle_solid(rect_coord_x: int, rect_coord_y: int, rect_width: int, rect_height: int,
                         rect_color: list, rect_tilt: bool = False):
    arcade.draw_rectangle_filled(
        center_x=rect_coord_x,
        center_y=rect_coord_y,
        width=rect_width,
        height=rect_height,
        color=rect_color,
        tilt_angle=12 if rect_tilt else 0
    )


def draw_rectangle_outline(rect_coord_x: int, rect_coord_y: int, rect_width: int, rect_height: int,
                           rect_border_color: list, rect_border_width: int, rect_tilt: bool = False):
    arcade.draw_rectangle_outline(
        center_x=rect_coord_x,
        center_y=rect_coord_y,
        width=rect_width,
        height=rect_height,
        color=rect_border_color,
        border_width=rect_border_width,
        tilt_angle=12 if rect_tilt else 0
    )


def draw_square_solid(sq_coord_x: int, sq_coord_y: int, sq_side_len: int,
                      sq_color: list, sq_tilt: bool = False):
    draw_rectangle_solid(
        rect_coord_x=sq_coord_x,
        rect_coord_y=sq_coord_y,
        rect_width=sq_side_len,
        rect_height=sq_side_len,
        rect_color=sq_color,
        rect_tilt=sq_tilt
    )


def draw_square_outline(sq_coord_x: int, sq_coord_y: int, sq_side_len: int,
                        sq_border_color: list, sq_border_width: int, sq_tilt: bool = False):
    draw_rectangle_outline(
        rect_coord_x=sq_coord_x,
        rect_coord_y=sq_coord_y,
        rect_width=sq_side_len,
        rect_height=sq_side_len,
        rect_border_color=sq_border_color,
        rect_border_width=sq_border_width,
        rect_tilt=sq_tilt
    )


def draw_circle_solid(circle_coord_x: int, circle_coord_y: int, circle_radius: int,
                      circle_color: list, circle_segments: int):
    arcade.draw_circle_filled(
        center_x=circle_coord_x,
        center_y=circle_coord_y,
        radius=circle_radius,
        color=circle_color,
        num_segments=circle_segments
    )


def draw_circle_outline(circle_coord_x: int, circle_coord_y: int, circle_radius: int,
                        circle_border_color: list, circle_border_width: int, circle_segments: int):
    arcade.draw_circle_outline(
        center_x=circle_coord_x,
        center_y=circle_coord_y,
        radius=circle_radius,
        color=circle_border_color,
        border_width=circle_border_width,
        num_segments=circle_segments
    )


def draw_character(char_string: str, char_coord_x: int, char_coord_y: int, char_color: list,
                   char_font_size: int, char_font_name: str, char_rotation_angle: int,
                   char_font_bold: bool = False, char_font_italic: bool = False,
                   char_anchor: bool = True):
    arcade.draw_text(
        text=char_string,
        start_x=char_coord_x,
        start_y=char_coord_y,
        color=char_color,
        font_size=char_font_size,
        font_name=char_font_name,
        bold=char_font_bold,
        italic=char_font_italic,
        anchor_x='center' if char_anchor else 'left',
        anchor_y='center' if char_anchor else 'left',
        rotation=char_rotation_angle
    )


def draw_line(line_start_x: int, line_start_y: int, line_end_x: int, line_end_y: int,
              line_color: list, line_width: int):
    arcade.draw_line(
        start_x=line_start_x,
        start_y=line_start_y,
        end_x=line_end_x,
        end_y=line_end_y,
        color=line_color,
        line_width=line_width
    )


def stamp_board_tile(tile_coord_x: int, tile_coord_y: int, tile_color: str):
    draw_square_solid(
        sq_coord_x=tile_coord_x,
        sq_coord_y=tile_coord_y,
        sq_side_len=TILE_SIDE_LEN,
        sq_color=TILE_COLOR_WHITE if tile_color.lower() == 'white' else
                 TILE_COLOR_BLACK if tile_color.lower() == 'black' else
                 ERROR_COLOR_MAIN,
        sq_tilt=False
    )


def stamp_board_highlighted_tile(tile_coord_x: int, tile_coord_y: int, tile_highlight_type: str):
    draw_square_outline(
        sq_coord_x=tile_coord_x,
        sq_coord_y=tile_coord_y,
        sq_side_len=TILE_HIGHLIGHT_SIDE_LEN,
        sq_border_width=TILE_HIGHLIGHT_BORDER_SIDE_LEN,
        sq_border_color=TILE_HIGHLIGHT_COLOR_MOVE if tile_highlight_type.lower() == 'move' else
                        TILE_HIGHLIGHT_COLOR_ATTACK if tile_highlight_type.lower() == 'kill' else
                        ERROR_COLOR_ALT,
        sq_tilt=False
    )


def stamp_board_tile_highlight_move(tile_coord_x: int, tile_coord_y: int):
    draw_square_outline(
        sq_coord_x=tile_coord_x,
        sq_coord_y=tile_coord_y,
        sq_side_len=TILE_HIGHLIGHT_SIDE_LEN,
        sq_border_width=TILE_HIGHLIGHT_BORDER_SIDE_LEN,
        sq_border_color=TILE_HIGHLIGHT_COLOR_MOVE,
        sq_tilt=False
    )


def stamp_board_tile_highlight_attack(tile_coord_x: int, tile_coord_y: int):
    draw_square_outline(
        sq_coord_x=tile_coord_x,
        sq_coord_y=tile_coord_y,
        sq_side_len=TILE_HIGHLIGHT_SIDE_LEN,
        sq_border_width=TILE_HIGHLIGHT_BORDER_SIDE_LEN,
        sq_border_color=TILE_HIGHLIGHT_COLOR_ATTACK,
        sq_tilt=False
    )


def stamp_checker_highlight_move(ch_coord_x: int, ch_coord_y: int):
    draw_square_solid(
        sq_coord_x=ch_coord_x,
        sq_coord_y=ch_coord_y,
        sq_side_len=TILE_HIGHLIGHT_SIDE_LEN,
        sq_color=TILE_HIGHLIGHT_COLOR_MOVE,
        sq_tilt=False
    )


def stamp_checker_highlight_attack(ch_coord_x: int, ch_coord_y: int):
    draw_square_solid(
        sq_coord_x=ch_coord_x,
        sq_coord_y=ch_coord_y,
        sq_side_len=TILE_HIGHLIGHT_SIDE_LEN,
        sq_color=TILE_HIGHLIGHT_COLOR_ATTACK,
        sq_tilt=False
    )


def __checker_complex_queen_index(ch_coord_x: int, ch_coord_y: int, ch_color: str):
    draw_character(
        char_string='Q',
        char_coord_x=ch_coord_x,
        char_coord_y=ch_coord_y + 2,
        char_color=CHECKER_COLOR_WHITE_ALT if ch_color.lower() == 'white' else
                   CHECKER_COLOR_BLACK_ALT if ch_color.lower() == 'black' else
                   ERROR_COLOR_ALT,
        char_font_size=int(round(CHECKER_QUEEN_INDEX_FONT_SIZE * 2.2, 0)),
        char_font_name=CHECKER_QUEEN_INDEX_FONT_NAME,
        char_font_bold=False,
        char_font_italic=False,
        char_anchor=True,
        char_rotation_angle=0
    )


def __checker_simple_queen_index(ch_coord_x: int, ch_coord_y: int, ch_color: str):
    draw_line(
        line_start_x=int(ch_coord_x - CHECKER_RADIUS_OUTER) + 5,
        line_start_y=ch_coord_y - 15,
        line_end_x=int(ch_coord_x + CHECKER_RADIUS_OUTER) - 5,
        line_end_y=ch_coord_y + 15,
        line_color=CHECKER_COLOR_WHITE_MAIN if ch_color.lower() == 'white' else
                   CHECKER_COLOR_BLACK_MAIN if ch_color.lower() == 'black' else
                   ERROR_COLOR_MAIN,
        line_width=CHECKER_QUEEN_LINE_WIDTH
    )


def __checker_simple(ch_coord_x: int, ch_coord_y: int, ch_color: str, ch_queen: bool = False):

    def render_outline():
        draw_circle_outline(
            circle_coord_x=ch_coord_x,
            circle_coord_y=ch_coord_y,
            circle_radius=CHECKER_RADIUS_OUTER,
            circle_border_color=CHECKER_COLOR_WHITE_MAIN if ch_color.lower() == 'white' else
                                CHECKER_COLOR_BLACK_MAIN if ch_color.lower() == 'black' else
                                ERROR_COLOR_MAIN,
            circle_border_width=CHECKER_SIMPLE_BORDER_LEN,
            circle_segments=CHECKER_SEGMENTS
        )

    def render_queen_index():
        __checker_simple_queen_index(ch_coord_x, ch_coord_y, ch_color)

    render_outline()
    if ch_queen:
        render_queen_index()


def __checker_complex(ch_coord_x: int, ch_coord_y: int, ch_color: str, ch_queen: bool = False):

    def render_outer_radius():
        draw_circle_solid(
            circle_coord_x=ch_coord_x + CHECKER_SHADOW_SHIFT_X,
            circle_coord_y=ch_coord_y + CHECKER_SHADOW_SHIFT_Y,
            circle_radius=CHECKER_RADIUS_OUTER,
            circle_color=CHECKER_COLOR_WHITE_ALT if ch_color.lower() == 'white' else
                         CHECKER_COLOR_BLACK_ALT if ch_color.lower() == 'black' else
                         ERROR_COLOR_ALT,
            circle_segments=CHECKER_SEGMENTS
        )
        draw_circle_solid(
            circle_coord_x=ch_coord_x - CHECKER_SHADOW_SHIFT_X,
            circle_coord_y=ch_coord_y - CHECKER_SHADOW_SHIFT_Y,
            circle_radius=CHECKER_RADIUS_OUTER,
            circle_color=CHECKER_COLOR_WHITE_MAIN if ch_color.lower() == 'white' else
                         CHECKER_COLOR_BLACK_MAIN if ch_color.lower() == 'black' else
                         ERROR_COLOR_MAIN,
            circle_segments=CHECKER_SEGMENTS
        )

    def render_outer_inner():
        draw_circle_solid(
            circle_coord_x=ch_coord_x - CHECKER_SHADOW_SHIFT_X,
            circle_coord_y=ch_coord_y - CHECKER_SHADOW_SHIFT_Y,
            circle_radius=CHECKER_RADIUS_INNER,
            circle_color=CHECKER_COLOR_WHITE_ALT if ch_color.lower() == 'white' else
                         CHECKER_COLOR_BLACK_ALT if ch_color.lower() == 'black' else
                         ERROR_COLOR_ALT,
            circle_segments=CHECKER_SEGMENTS
        )
        draw_circle_solid(
            circle_coord_x=ch_coord_x + CHECKER_SHADOW_SHIFT_X,
            circle_coord_y=ch_coord_y + CHECKER_SHADOW_SHIFT_Y,
            circle_radius=CHECKER_RADIUS_INNER,
            circle_color=CHECKER_COLOR_WHITE_MAIN if ch_color.lower() == 'white' else
                         CHECKER_COLOR_BLACK_MAIN if ch_color.lower() == 'black' else
                         ERROR_COLOR_MAIN,
            circle_segments=CHECKER_SEGMENTS
        )

    def render_queen_index():
        __checker_complex_queen_index(ch_coord_x, ch_coord_y, ch_color)

    render_outer_radius()
    render_outer_inner()
    if ch_queen:
        render_queen_index()


def stamp_checker(ch_coord_x: int, ch_coord_y: int, ch_color: str, ch_queen: bool = False):
    style = 1
    render_checker = {
        0: lambda: __checker_simple(ch_coord_x, ch_coord_y, ch_color, ch_queen),
        1: lambda: __checker_complex(ch_coord_x, ch_coord_y, ch_color, ch_queen)
    }
    render_checker[style]()


def __button_large(b_coord_x: int, b_coord_y: int, b_caption: str, b_filled: bool = False):
    if b_filled:
        draw_rectangle_solid(
            rect_coord_x=b_coord_x,
            rect_coord_y=b_coord_y,
            rect_width=BUTTON_LARGE_WIDTH,
            rect_height=BUTTON_LARGE_HEIGHT,
            rect_color=BUTTON_FILLED_COLOR,
            rect_tilt=False
        )
    draw_rectangle_outline(
        rect_coord_x=b_coord_x,
        rect_coord_y=b_coord_y,
        rect_width=BUTTON_LARGE_WIDTH,
        rect_height=BUTTON_LARGE_HEIGHT,
        rect_border_color=BUTTON_BORDER_COLOR,
        rect_border_width=BUTTON_BORDER_LEN,
        rect_tilt=False
    )
    draw_character(
        char_string=b_caption,
        char_coord_x=b_coord_x,
        char_coord_y=b_coord_y,
        char_color=BUTTON_CAPTION_COLOR,
        char_font_size=BUTTON_CAPTION_FONT_SIZE,
        char_font_name=BUTTON_CAPTION_FONT_NAME,
        char_rotation_angle=6 if b_filled else 0,
        char_font_bold=BUTTON_CAPTION_STYLE_BOLD,
        char_font_italic=BUTTON_CAPTION_STYLE_ITALIC,
        char_anchor=True
    )


def __button_small(b_coord_x: int, b_coord_y: int, b_caption: str, b_filled: bool = False):
    if b_filled:
        draw_rectangle_solid(
            rect_coord_x=b_coord_x,
            rect_coord_y=b_coord_y,
            rect_width=BUTTON_SMALL_WIDTH,
            rect_height=BUTTON_SMALL_HEIGHT,
            rect_color=BUTTON_FILLED_COLOR,
            rect_tilt=False
        )
    draw_rectangle_outline(
        rect_coord_x=b_coord_x,
        rect_coord_y=b_coord_y,
        rect_width=BUTTON_SMALL_WIDTH,
        rect_height=BUTTON_SMALL_HEIGHT,
        rect_border_color=BUTTON_BORDER_COLOR,
        rect_border_width=BUTTON_BORDER_LEN,
        rect_tilt=False
    )
    draw_character(
        char_string=b_caption,
        char_coord_x=b_coord_x,
        char_coord_y=b_coord_y,
        char_color=BUTTON_CAPTION_COLOR,
        char_font_size=BUTTON_CAPTION_FONT_SIZE,
        char_font_name=BUTTON_CAPTION_FONT_NAME,
        char_rotation_angle=6 if b_filled else 0,
        char_font_bold=BUTTON_CAPTION_STYLE_BOLD,
        char_font_italic=BUTTON_CAPTION_STYLE_ITALIC,
        char_anchor=True
    )


def stamp_button(b_coord_x: int, b_coord_y: int, b_size: str, b_caption: str, b_filled: bool = False):
    size = b_size.lower()
    render_button = {
        'large': lambda: __button_large(b_coord_x, b_coord_y, b_caption, b_filled),
        'small': lambda: __button_small(b_coord_x, b_coord_y, b_caption, b_filled),
    }
    render_button[size]()


def stamp_clockface(cf_coord_x: int, cf_coord_y: int, cf_value: list):
    value_list = cf_value
    if not isinstance(cf_value, list):
        value_list = [23, 59, 59]
    hours, minutes, seconds = value_list
    hours = f'{hours}' if hours >= 10 else f'0{hours}'
    minutes = f'{minutes}' if minutes >= 10 else f'0{minutes}'
    seconds = f'{seconds}' if seconds >= 10 else f'0{seconds}'
    cf_time_string = f'{hours}:{minutes}:{seconds}'
    draw_character(
        char_string=cf_time_string,
        char_coord_x=cf_coord_x,
        char_coord_y=cf_coord_y,
        char_color=CLOCKFACE_CAPTION_COLOR,
        char_font_size=CLOCKFACE_CAPTION_FONT_SIZE,
        char_font_name=CLOCKFACE_CAPTION_FONT_NAME,
        char_font_bold=CLOCKFACE_CAPTION_STYLE_BOLD,
        char_font_italic=CLOCKFACE_CAPTION_STYLE_ITALIC,
        char_rotation_angle=0,
        char_anchor=True
    )


def stamp_div(div_coord_x: int, div_coord_y: int):
    div_start_x = int(div_coord_x - DIVIDER_LENGTH / 2)
    div_end_x = int(div_coord_x + DIVIDER_LENGTH / 2)
    div_start_y, div_end_y = div_coord_y, div_coord_y
    draw_line(
        line_start_x=div_start_x,
        line_start_y=div_start_y,
        line_end_x=div_end_x,
        line_end_y=div_end_y,
        line_color=DIVIDER_COLOR,
        line_width=DIVIDER_WIDTH
    )


def grid_clear():
    global SURFACE_GRID, SURFACE_EMPTY

    for row in SURFACE_GRID.keys():
        for column in SURFACE_GRID[row].keys():
            if SURFACE_GRID[row][column] is not None:
                SURFACE_GRID[row][column] = None
    SURFACE_EMPTY = True


def grid_fill():
    global SURFACE_GRID, SURFACE_EMPTY

    for row in SURFACE_GRID.keys():
        for column in SURFACE_GRID[row].keys():
            board_position = [row, column]
            if test_position_can_spawn_checker(check_position=board_position):
                if SURFACE_GRID[row][column] is None:
                    f_checker = spawn_checker(spawn_position=board_position,
                                            spawn_color='',
                                            spawn_queen=False)
                    SURFACE_GRID[row][column] = f_checker
    SURFACE_EMPTY = False


def empty():
    status = SURFACE_EMPTY
    return status


def __load_texture(texture_filename: str, texture_mirrored: bool = False):
    texture_path = os.path.join(PROJECT_IMAGES_DIR, texture_filename)
    texture = arcade.load_texture(file_name=texture_path,
                                  mirrored=texture_mirrored,
                                  scale=1)
    return texture


def render_texture(texture_filename: str, texture_coord_x: int, texture_coord_y: int, texture_mirrored: bool = False):
    texture_object = __load_texture(texture_filename=texture_filename, texture_mirrored=texture_mirrored)
    arcade.draw_texture_rectangle(
        center_x=texture_coord_x,
        center_y=texture_coord_y,
        texture=texture_object,
        width=texture_object.width,
        height=texture_object.height,
    )


def __is_type_list(value):
    return True if isinstance(value, list) else False


def __is_type_integer(value):
    return True if isinstance(value, int) else False


def __is_even(number: int):
    return True if number % 2 == 0 else False


def __is_positive(number: int):
    return True if number > 0 else False


def test_position_is_valid(check_position: list):
    test_result = False
    if __is_type_list(check_position):
        row, column = check_position
        if __is_type_integer(row) and __is_type_integer(column):
            row_range = range(1, BOARD_ROW_COUNT + 1)
            column_range = range(1, BOARD_COLUMN_COUNT + 1)
            if row in row_range and column in column_range:
                test_result = True
    return test_result


def test_position_can_be_used(check_position: list):
    test_result = False
    if test_position_is_valid(check_position):
        row, column = check_position
        if __is_even(row) and not __is_even(column) or \
           __is_even(column) and not __is_even(row):
            test_result = True
    return test_result


def test_position_can_spawn_checker(check_position: list):
    test_result = False
    if test_position_can_be_used(check_position):
        row = check_position[0]
        if row not in (4, 5):
            test_result = True
    return test_result


def test_coordinates_are_valid(check_coordinates: list):
    test_result = False
    if __is_type_list(check_coordinates):
        coord_x, coord_y = check_coordinates
        if __is_type_integer(coord_x) and __is_type_integer(coord_y):
            if __is_positive(coord_x) and __is_positive(coord_y):
                test_result = True
    return test_result


def test_coordinates_in_board_boundaries(check_coordinates: list):
    test_result = False
    if test_coordinates_are_valid(check_coordinates):
        boundaries_range_x = range(BOARD_BOUNDARY_LEFT, BOARD_BOUNDARY_RIGHT)
        boundaries_range_y = range(BOARD_BOUNDARY_BOTTOM, BOARD_BOUNDARY_TOP)
        coord_x, coord_y = check_coordinates
        coord_x_in_range = True if coord_x in boundaries_range_x else False
        coord_y_in_range = True if coord_y in boundaries_range_y else False
        if coord_x_in_range and coord_y_in_range:
            test_result = True
    return test_result


def convert_board_position_to_coordinates(conv_position: list):
    if test_position_is_valid(conv_position):
        row, column = conv_position
        coord_x = int(BOARD_MARGIN_LEN + TILE_SIDE_LEN / 2 + TILE_SIDE_LEN * (column - 1))
        coord_y = int(BOARD_MARGIN_LEN + TILE_SIDE_LEN / 2 + TILE_SIDE_LEN * (row - 1))
        coordinates = [coord_x, coord_y]
        return coordinates


def convert_board_position_to_alphanumeric_index(conv_position: list):
    if test_position_is_valid(conv_position):
        row, column = conv_position
        letter = BOARD_LETTER_INDEX[column - 1]
        number = row
        alphanumeric_index = f'{letter}{number}'
        return alphanumeric_index


def convert_coordinates_to_board_position(conv_coordinates: list):
    if test_coordinates_are_valid(conv_coordinates):
        coord_x, coord_y = conv_coordinates
        row = 1 + ((coord_y - BOARD_MARGIN_LEN) // TILE_SIDE_LEN)
        column = 1 + ((coord_x - BOARD_MARGIN_LEN) // TILE_SIDE_LEN)
        position = [row, column]
        return position


def get_checker_by_position(check_position: list):
    if test_position_can_be_used(check_position):
        row, column = check_position
        if SURFACE_GRID[row][column] is not None:
            g_checker = SURFACE_GRID[row][column]
            return g_checker


def get_checker_by_coordinates(check_coordinates: list):
    if test_coordinates_in_board_boundaries(check_coordinates):
        board_position = convert_coordinates_to_board_position(check_coordinates)
        return get_checker_by_position(board_position)


def get_checkers_that_can_move():
    checkers_can_attack_list = []
    for row in SURFACE_GRID:
        for column in SURFACE_GRID[row]:
            if SURFACE_GRID[row][column] is not None:
                g_checker = SURFACE_GRID[row][column]
                if g_checker.can_move:
                    checkers_can_attack_list.append(g_checker)
    return checkers_can_attack_list


def get_checkers_that_can_attack():
    checkers_can_attack_list = []
    for row in SURFACE_GRID:
        for column in SURFACE_GRID[row]:
            if SURFACE_GRID[row][column] is not None:
                g_checker = SURFACE_GRID[row][column]
                if g_checker.can_kill:
                    checkers_can_attack_list.append(g_checker)
    return checkers_can_attack_list


def __checker_predefined(spawn_position: list, spawn_color: str, spawn_queen: bool = False):
    new_checker = Checker(init_position=spawn_position,
                               init_color=spawn_color,
                               init_type_queen=spawn_queen)
    return new_checker


def __checker_undefined(spawn_position: list):
    spawn_color = 'White' if spawn_position[0] in (1, 2, 3) else 'Black'
    new_checker = Checker(init_position=spawn_position,
                               init_color=spawn_color,
                               init_type_queen=False)
    return new_checker


def spawn_checker(spawn_position: list, spawn_color: str, spawn_queen: bool = False):
    if spawn_color in ('White', 'Black'):
        spawned_checker = __checker_predefined(spawn_position, spawn_color, spawn_queen)
    else:
        spawned_checker = __checker_undefined(spawn_position)
    return spawned_checker


POINTER_POS_CHECKER = None
POINTER_POS_EMPTY = False
POINTER_POS_INVALID = False
POINTER_FORWARD = False


def __pointer(check_position: list):
    global POINTER_POS_CHECKER, POINTER_POS_EMPTY, POINTER_POS_INVALID

    POINTER_POS_CHECKER = None
    POINTER_POS_EMPTY = False
    POINTER_POS_INVALID = False

    if test_position_is_valid(check_position):
        POINTER_POS_INVALID = False
        POINTER_POS_CHECKER = get_checker_by_position(check_position)
        if POINTER_POS_CHECKER is None:
            POINTER_POS_EMPTY = True
    else:
        POINTER_POS_INVALID = True


def __forward(checker_color: str, movement_axis: int):
    global POINTER_FORWARD

    result = True if checker_color.lower() == 'white' and movement_axis == 1 else \
             True if checker_color.lower() == 'black' and movement_axis == -1 else False
    POINTER_FORWARD = result


def __between(old_position, new_position):
    tiles_between = []
    between_count = abs(old_position[0] - new_position[0])
    if between_count > 1:
        row_offset = 1 if old_position[0] < new_position[0] else -1
        column_offset = 1 if old_position[1] < new_position[1] else -1
        position_between = old_position
        while True:
            position_between = [position_between[0] + row_offset, position_between[1] + column_offset]
            if not test_position_is_valid(position_between):
                break
            else:
                if position_between in (old_position, new_position):
                    break
                else:
                    tiles_between.append(position_between)
    return tiles_between


def get_move_list(checker_object):
    checker_move_list = [[], []]
    checker_position = checker_object.position
    checker_color = checker_object.color
    checker_queen = checker_object.queen
    for axis_x in (-1, 1):
        for axis_y in (-1, 1):
            checker_attacking = False
            peek_position = checker_position
            while True:
                peek_position = [peek_position[0] + axis_y,         # row position shift
                                 peek_position[1] + axis_x]         # column position shift
                __pointer(peek_position)
                __forward(checker_color, movement_axis=axis_y)
                if POINTER_POS_INVALID:
                    break
                else:
                    if POINTER_POS_EMPTY:
                        if not checker_attacking:
                            if POINTER_FORWARD:
                                checker_move_list[0].append(peek_position)
                                if not checker_queen:
                                    break
                            else:
                                if not checker_queen:
                                    break
                                else:
                                    checker_move_list[0].append(peek_position)
                        else:
                            checker_move_list[0].append(peek_position)
                            checker_move_list[1].append(peek_position)
                            if not checker_queen:
                                break
                    else:
                        if POINTER_POS_CHECKER.color.lower() == checker_color.lower():
                            break
                        else:
                            if not checker_attacking:
                                checker_attacking = True
                            else:
                                break
    return checker_move_list


def move(checker_object, new_position):
    tiles_between = __between(old_position=checker_object.position,
                              new_position=new_position)
    if len(tiles_between) > 0:
        for position in tiles_between:
            row, column = position[0], position[1]
            SURFACE_GRID[row][column] = None

    # Moving the checker from old to new positions:
    SURFACE_GRID[checker_object.position[0]][checker_object.position[1]] = None     # Delete old instance
    SURFACE_GRID[new_position[0]][new_position[1]] = checker_object                 # Move instance to position
    checker_object.set_position(new_position)


class Checker:

    ID = 0

    @classmethod
    def __update_id(cls):
        cls.ID += 1

    def __init__(self, init_position: list, init_color: str, init_type_queen: bool = False):

        # Public attributes:
        self.position = init_position       # List type collection, eg. [1, 2]
        self.color = init_color             # White / Black
        self.queen = init_type_queen        # True / False (default)
        self.dev = False                    # True, if force-spawn / False (default)

        # Protected private attributes:
        self.__move_list = []               # Contains board positions current checker can move to
        self.__kill_list = []               # Contains board positions current checker must move to

        # Initialisation methods and setups:
        self.__update_id()                  # Updates checker class object's ID value (unique)

    def __str__(self):
        checker_information = '{color} {checker}'.format(
            color=self.color,
            checker="checker (queen)" if self.queen else "checker",)
        return checker_information

    @property
    def coordinates(self):
        coordinates = convert_board_position_to_coordinates(conv_position=self.position)
        return coordinates

    @property
    def index(self):
        alphanumeric_index = convert_board_position_to_alphanumeric_index(conv_position=self.position)
        return alphanumeric_index

    @property
    def can_promote(self):
        status = False
        color = self.color.lower()
        row = self.position[0]
        if color == 'white' and row == 8 or color == 'black' and row == 1:
            status = True
        return status

    @property
    def can_move(self):
        status = False
        if len(self.__move_list) > 0:
            status = True
        return status

    @property
    def can_kill(self):
        status = False
        if len(self.__kill_list) > 0:
            status = True
        return status

    @property
    def move_list(self):
        return self.__move_list

    @property
    def kill_list(self):
        return self.__kill_list

    def set_color(self, new_color: str):
        self.color = new_color

    def set_position(self, new_position: str):
        self.position = new_position

    def promote(self):
        if not self.queen:
            self.queen = True

    def move(self, position):
        move(checker_object=self, new_position=position)

    def update(self):
        if self.can_promote and not self.dev:
            self.promote()

        updated_move_list = get_move_list(checker_object=self)
        if updated_move_list is not None:
            self.__move_list = updated_move_list[0]         # Move list
            self.__kill_list = updated_move_list[1]         # Attack list

    def display(self):
        coordinates = self.coordinates
        coordinate_x, coordinate_y = coordinates
        render_texture(
            texture_filename='checker_{color}{type}.png'.format(
                color=self.color.lower(),
                type='_queen' if self.queen else ''),
            texture_coord_x=coordinate_x,
            texture_coord_y=coordinate_y,
        )


class Board:


    def __init__(self):
        global SURFACE_GRID, SURFACE_EMPTY

        row_count_range = range(1, BOARD_ROW_COUNT + 1)
        column_count_range = range(1, BOARD_COLUMN_COUNT + 1)
        for row in row_count_range:
            if row not in SURFACE_GRID.keys():
                SURFACE_GRID[row] = {}
            for column in column_count_range:
                if column not in SURFACE_GRID[row].keys():
                    SURFACE_GRID[row][column] = None
        SURFACE_EMPTY = True

    @staticmethod
    def clear():
        grid_clear()

    @staticmethod
    def fill():
        grid_fill()

    @staticmethod
    def update():
        for row in SURFACE_GRID:
            for column in SURFACE_GRID[row]:
                if SURFACE_GRID[row][column] is not None:
                    u_checker = SURFACE_GRID[row][column]
                    u_checker.update()

    @property
    def map_is_cleared(self):
        status = SURFACE_EMPTY
        return status

    @staticmethod
    def display():
        render_texture(
            texture_filename='board_surface.png',
            texture_coord_x=BOARD_POSITION_X,
            texture_coord_y=BOARD_POSITION_Y,
            texture_mirrored=False
        )

    @staticmethod
    def display_checkers():
        for row in SURFACE_GRID:
            for column in SURFACE_GRID[row]:
                if SURFACE_GRID[row][column] is not None:
                    SURFACE_GRID[row][column].display()


PRESET_NAMES = {
    0: 'Main menu',
    1: 'Settings menu',
    2: 'Active game GUI',
    3: 'Paused menu',
    4: 'Start new game menu',
    5: 'End current game menu',
    6: 'Game results (game won)',
    7: 'Game results (game lost/force restarted)',
    8: 'Quit app confirmation menu',
    9: 'Game results (game draw)',
}
CLOCKFACE_POSITIONS = {
    1: [CLOCKFACE_POSITION_X, CLOCKFACE_POSITION_Y],      # Default position
    2: [0, 0]                                             # Alternative position
}
MENU_NAME_POSITION = {
    1: [660, 452]
}
APP_INFORMATION = {
    1: [660, 20]
}
TURN_HISTORY_POSITIONS = {
    0: [DIVIDER_POSITION_X, 182],
    1: [],
    2: []
}
DIVIDER_POSITIONS = {
    1: [DIVIDER_POSITION_X, 472],
    2: [DIVIDER_POSITION_X, 192],
    3: []
}
BUTTON_GRID_POSITIONS = {

    # 1 to 5 are positions from top to bottom displayed on the panel surface. The lower the number, the higher the
    # button is situated on the grid. Inner position 0 sets the button object to the center point, 1 and 2 set the
    # object alignment to left or right side accordingly:

    1: {0: [BUTTON_LARGE_POSITION_X_MIDDLE,
            BUTTON_LARGE_HEIGHT * 5 + BUTTON_MARGIN_Y * 5],
        1: [BUTTON_SMALL_POSITION_X_LEFT,
            BUTTON_LARGE_HEIGHT * 5 + BUTTON_MARGIN_Y * 5],
        2: [BUTTON_SMALL_POSITION_X_RIGHT,
            BUTTON_LARGE_HEIGHT * 5 + BUTTON_MARGIN_Y * 5]},

    2: {0: [BUTTON_LARGE_POSITION_X_MIDDLE,
            BUTTON_LARGE_HEIGHT * 4 + BUTTON_MARGIN_Y * 4],
        1: [BUTTON_SMALL_POSITION_X_LEFT,
            BUTTON_LARGE_HEIGHT * 4 + BUTTON_MARGIN_Y * 4],
        2: [BUTTON_SMALL_POSITION_X_RIGHT,
            BUTTON_LARGE_HEIGHT * 4 + BUTTON_MARGIN_Y * 4]},

    3: {0: [BUTTON_LARGE_POSITION_X_MIDDLE,
            BUTTON_LARGE_HEIGHT * 3 + BUTTON_MARGIN_Y * 3],
        1: [BUTTON_SMALL_POSITION_X_LEFT,
            BUTTON_LARGE_HEIGHT * 3 + BUTTON_MARGIN_Y * 3],
        2: [BUTTON_SMALL_POSITION_X_RIGHT,
            BUTTON_LARGE_HEIGHT * 3 + BUTTON_MARGIN_Y * 3]},

    4: {0: [BUTTON_LARGE_POSITION_X_MIDDLE,
            BUTTON_LARGE_HEIGHT * 2 + BUTTON_MARGIN_Y * 2],
        1: [BUTTON_SMALL_POSITION_X_LEFT,
            BUTTON_LARGE_HEIGHT * 2 + BUTTON_MARGIN_Y * 2],
        2: [BUTTON_SMALL_POSITION_X_RIGHT,
            BUTTON_LARGE_HEIGHT * 2 + BUTTON_MARGIN_Y * 2]},

    5: {0: [BUTTON_LARGE_POSITION_X_MIDDLE,
            BUTTON_LARGE_HEIGHT + BUTTON_MARGIN_Y],
        1: [BUTTON_SMALL_POSITION_X_LEFT,
            BUTTON_LARGE_HEIGHT + BUTTON_MARGIN_Y],
        2: [BUTTON_SMALL_POSITION_X_RIGHT,
            BUTTON_LARGE_HEIGHT + BUTTON_MARGIN_Y]},
}


def click_get_button_boundary_range(button_object):
    coordinate_x, coordinate_y = button_object.coordinates
    boundary_top = int(coordinate_y + BUTTON_SMALL_HEIGHT / 2)
    boundary_bottom = int(coordinate_y - BUTTON_SMALL_HEIGHT / 2)
    boundary_right = int(coordinate_x + BUTTON_SMALL_WIDTH / 2 if button_object.size == 'small' else \
                         coordinate_x + BUTTON_LARGE_WIDTH / 2 if button_object.size == 'large' else 0)
    boundary_left = int(coordinate_x - BUTTON_SMALL_WIDTH / 2 if button_object.size == 'small' else \
                        coordinate_x - BUTTON_LARGE_WIDTH / 2 if button_object.size == 'large' else 0)
    boundaries = [range(boundary_left, boundary_right),
                  range(boundary_bottom, boundary_top)]
    return boundaries


def click_coordinates_in_button_boundaries(coordinates, button_object):
    coordinate_x, coordinate_y = coordinates
    boundary_x_range, boundary_y_range = click_get_button_boundary_range(button_object)
    in_boundaries = False
    if coordinate_x in boundary_x_range and coordinate_y in boundary_y_range:
        in_boundaries = True
    return in_boundaries


def get_seconds_from_dt(datetime_value):
    converted = datetime.strftime(datetime_value, '%S')
    return converted


def get_minutes_from_dt(datetime_value):
    converted = datetime.strftime(datetime_value, '%M')
    return converted


def get_hours_from_dt(datetime_value):
    converted = datetime.strftime(datetime_value, '%H')
    return converted


def dt_to_list(datetime_value):
    seconds = get_seconds_from_dt(datetime_value)
    minutes = get_minutes_from_dt(datetime_value)
    hours = get_hours_from_dt(datetime_value)
    converted = [hours, minutes, seconds]
    return converted


def dt_to_seconds(datetime_value):
    converted_list = dt_to_list(datetime_value)
    converted_seconds = list_to_seconds(converted_list)
    return converted_seconds


def list_to_seconds(conv_list: list):
    hours, minutes, seconds = conv_list
    seconds_in_minute = 60
    minutes_in_hour = 60
    converted_seconds = int(int(seconds) +
                            int(minutes) * seconds_in_minute +
                            int(hours) * minutes_in_hour * seconds_in_minute)
    return converted_seconds


def seconds_to_list(conv_seconds: int):
    seconds_in_minute = 60
    minutes_in_hour = 60
    hours = conv_seconds // seconds_in_minute // minutes_in_hour
    minutes = conv_seconds // seconds_in_minute
    seconds = conv_seconds - minutes * minutes_in_hour
    converted_list = [hours, minutes, seconds]
    return converted_list


def __now_dt():
    time = datetime.now()
    return time


def __now_formatted():
    time = datetime.strftime(__now_dt(), '%H:%M:%S')
    return time


def now(formatted: bool = True):
    generate = {
        True: lambda: __now_formatted(),
        False: lambda: __now_dt()
    }
    time = generate[formatted]()
    return time


def list_adjust(adj_list: list, mod: int, number: int):
    conv_seconds = list_to_seconds(adj_list)
    adj_seconds = conv_seconds + int(mod) * int(number)
    adjusted_list = seconds_to_list(adj_seconds)
    return adjusted_list


def dt(dt_start, dt_end):
    list_start = dt_to_list(dt_start)
    list_end = dt_to_list(dt_end)
    difference = lists(list_start, list_end)
    return difference


def lists(list_start: list, list_end: list):
    start = list_to_seconds(list_start)
    end = list_to_seconds(list_end)
    difference = end - start
    return difference


class Stopwatch:

    def __init__(self):
        self.running = False
        self.paused = False

        # Protected attributes to store and reset session / game values
        self.__started = None
        self.__paused = None
        self.__resumed = None
        self.__skip = 0
        self.__stopped = None

    def start(self):
        self.running = True
        self.__started = now(formatted=False)

    def pause(self):
        self.paused = True
        self.__paused = now(formatted=False)

    def unpause(self):
        self.paused = False
        self.__resumed = now(formatted=False)
        seconds_paused = dt(dt_start=self.__paused,
                                       dt_end=self.__resumed)
        self.__skip += seconds_paused
        self.__paused = None
        self.__resumed = None

    def stop(self):
        self.__stopped = now(formatted=False)
        self.running = False
        self.paused = False

    def reset(self):
        if self.running:
            self.stop()
        self.__started = None
        self.__paused = None
        self.__resumed = None
        self.__skip = 0
        self.__stopped = None

    def elapsed(self):
        if self.__started is not None:
            start_time = self.__started
            pause_time = self.__paused
            end_time = self.__stopped

            if self.running:
                end_time = now(formatted=False)

            if not self.paused:
                unskipped_time = dt(dt_start=start_time, dt_end=end_time)
                final_time = unskipped_time - self.__skip
                final_time_formatted = seconds_to_list(final_time)
            else:
                final_time = dt(dt_start=start_time, dt_end=pause_time) - self.__skip
                final_time_formatted = seconds_to_list(final_time)

            return final_time_formatted


class Timer:

    ID = 0

    @classmethod
    def update_timer_id(cls):
        cls.ID += 1

    def __init__(self):
        self.running = False
        self.update_timer_id()

        # Protected attributes to store and reset session / game values
        self.__started = None
        self.__paused = None
        self.__resumed = None
        self.__skip = 0
        self.__set = None

    @property
    def ring(self):
        time_up = False
        if self.running:
            rem_seconds = list_to_seconds(self.remaining)
            if rem_seconds <= 0:
                time_up = True
        return time_up

    def set(self, seconds: int):
        self.__set = seconds

    def start(self):
        if self.__set is not None:
            self.running = True
            self.__started = now(formatted=False)

    def pause(self):
        self.__paused = now(formatted=False)

    def unpause(self):
        self.__resumed = now(formatted=False)
        seconds_paused = dt(dt_start=self.__paused, dt_end=self.__resumed)
        self.__skip += seconds_paused
        self.__paused = None
        self.__resumed = None

    def stop(self):
        if self.running:
            self.running = False
            self.__started = None
            self.__paused = None
            self.__resumed = None
            self.__skip = 0
            self.__set = None

    @property
    def elapsed(self):
        if self.running:
            start_time = self.__started
            end_time = now(formatted=False)
            unskipped_time = dt(dt_start=start_time, dt_end=end_time)
            final_time = unskipped_time - self.__skip
            final_time_formatted = seconds_to_list(final_time)
            return final_time_formatted

    @property
    def remaining(self):
        start_seconds = dt_to_seconds(self.__started)
        end_seconds = start_seconds + self.__set + self.__skip
        now_seconds = dt_to_seconds(now(formatted=False))
        diff_seconds = end_seconds - now_seconds
        diff_formatted = seconds_to_list(diff_seconds)
        return diff_formatted


class Button:
    ID = None

    def __init__(self, init_position: list, init_filled: bool = False):
        self.__caption = None
        self.__position = init_position
        self.__size = 'large' if init_position[1] == 0 else 'small'

        self.filled = init_filled

    def __str__(self):
        return f'UI element ({self.size} button \"{self.caption}\")'

    @property
    def size(self):
        return self.__size

    @property
    def caption(self):
        return self.__caption

    @property
    def position(self):
        return self.__position

    @property
    def coordinates(self):
        position, align = self.__position
        conv_coordinates = BUTTON_GRID_POSITIONS[position][align]
        return conv_coordinates

    @property
    def is_valid(self):
        result = True
        if self.caption is None or self.size is None:
            result = False
        return result

    def set_caption(self, caption: str):
        self.__caption = str(caption).capitalize()

    def display(self):
        if self.is_valid:
            coordinate_x, coordinate_y = self.coordinates
            stamp_button(
                b_coord_x=coordinate_x,
                b_coord_y=coordinate_y,
                b_size=self.size,
                b_caption=self.caption,
                b_filled=self.filled
            )


class StartButton(Button):
    ID = BUTTON_ID_START_GAME
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Start')


class SettingsButton(Button):
    ID = BUTTON_ID_SETTINGS
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Settings')


class QuitButton(Button):
    ID = BUTTON_ID_QUIT
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Quit')


class PauseButton(Button):
    ID = BUTTON_ID_PAUSE
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Pause')


class ResumeButton(Button):
    ID = BUTTON_ID_RESUME
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Resume')


class RestartButton(Button):
    ID = BUTTON_ID_RESTART_GAME
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Restart')


class YesButton(Button):
    ID = BUTTON_ID_YES
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Yes')


class NoButton(Button):
    ID = BUTTON_ID_NO
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('No')


class HintButton(Button):
    ID = BUTTON_ID_HINT
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Hint')


class UndoButton(Button):
    ID = BUTTON_ID_UNDO
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Undo')


class BackButton(Button):
    ID = BUTTON_ID_BACK
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Back')


class MainMenuButton(Button):
    ID = BUTTON_ID_MAIN_MENU
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Main Menu')


class ContinueButton(Button):
    ID = BUTTON_ID_CONTINUE
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Continue')


class Clockface:
    def __init__(self):
        self.__position = 1
        self.stopwatch = Stopwatch()

    @property
    def time(self):
        return self.stopwatch.elapsed()

    def display(self):
        coordinate_x, coordinate_y = CLOCKFACE_POSITIONS[1]
        stamp_clockface(
            cf_coord_x=coordinate_x,
            cf_coord_y=coordinate_y,
            cf_value=self.time
        )


class Divider:
    def __init__(self):
        self.__position = 1

    def __str__(self):
        return f'UI element (block line divider)'

    @property
    def position(self):
        return self.__position

    def set_position(self, new_position: int):
        self.__position = new_position

    @property
    def coordinates(self):
        coordinates = DIVIDER_POSITIONS[self.position]
        return coordinates

    def display(self):
        coordinate_x, coordinate_y = self.coordinates
        stamp_div(
            div_coord_x=coordinate_x,
            div_coord_y=coordinate_y
        )


class ClockfaceDivider(Divider):
    def __init__(self):
        super().__init__()
        self.set_position(new_position=1)


class LowerDivider(Divider):
    def __init__(self):
        super().__init__()
        self.set_position(new_position=2)


class Logo:
    def __init__(self):
        self._upper_caption = 'zen'
        self._lower_caption = 'Checkers'

    def __str__(self):
        return f'UI element (app logo \"{self.caption}\")'

    @property
    def caption(self):
        caption = f'{self._upper_caption} {self._lower_caption}'
        return caption

    @property
    def coordinates(self):
        coordinates = [[660, 524],      # Upper caption
                       [660, 496]]      # Lower caption
        return coordinates

    def display(self):
        upper_coordinates, lower_coordinates = self.coordinates
        upper_coord_x, upper_coord_y = upper_coordinates
        lower_coord_x, lower_coord_y = lower_coordinates
        draw_character(
            char_string=self._upper_caption,
            char_coord_x=upper_coord_x,
            char_coord_y=upper_coord_y,
            char_color=LOGO_CAPTION_COLOR,
            char_font_name=LOGO_CAPTION_FONT_NAME,
            char_font_size=22,
            char_font_bold=LOGO_CAPTION_STYLE_BOLD,
            char_font_italic=LOGO_CAPTION_STYLE_ITALIC,
            char_rotation_angle=0,
            char_anchor=True
        )
        draw_character(
            char_string=self._lower_caption.upper(),
            char_coord_x=lower_coord_x,
            char_coord_y=lower_coord_y,
            char_color=LOGO_CAPTION_COLOR,
            char_font_name=LOGO_CAPTION_FONT_NAME,
            char_font_size=28,
            char_font_bold=LOGO_CAPTION_STYLE_BOLD,
            char_font_italic=LOGO_CAPTION_STYLE_ITALIC,
            char_rotation_angle=0,
            char_anchor=True
        )


class AppInformation:
    def __init__(self):
        self.__caption = GAME_WINDOW_TITLE
        self.__position = 1

    @property
    def caption(self):
        return self.__caption

    @property
    def position(self):
        return self.__position

    @property
    def coordinates(self):
        coordinates = APP_INFORMATION[self.position]
        return coordinates

    def display(self):
        coordinate_x, coordinate_y = self.coordinates
        draw_character(
            char_string=self.caption,
            char_coord_x=coordinate_x,
            char_coord_y=coordinate_y,
            char_color=CLOCKFACE_CAPTION_COLOR,
            char_rotation_angle=0,
            char_font_name='tahoma',
            char_font_size=12,
            char_font_bold=False,
            char_font_italic=False,
            char_anchor=True
        )


class TurnHistoryCaption:
    def __init__(self):
        self.__position = 0
        self.__caption = 'Turn history'

    def __str__(self):
        return f'UI element (turn history caption \"{self.caption}\")'

    @property
    def caption(self):
        return self.__caption

    @property
    def position(self):
        return self.__position

    @property
    def coordinates(self):
        coordinates = TURN_HISTORY_POSITIONS[self.position]
        return coordinates

    def set_caption(self, menu_caption: str):
        self.__caption = menu_caption

    def display(self):
        coordinate_x, coordinate_y = self.coordinates
        draw_character(
            char_string=self.caption,
            char_coord_x=coordinate_x,
            char_coord_y=coordinate_y,
            char_color=CLOCKFACE_CAPTION_COLOR,
            char_font_name='georgia',
            char_font_size=12,
            char_font_bold=False,
            char_font_italic=False,
            char_rotation_angle=0,
            char_anchor=True
        )


class MenuName:
    def __init__(self):
        self.__position = 1
        self.__caption = 'NAME'

    def __str__(self):
        return f'UI element (menu name caption \"{self.caption}\")'

    @property
    def caption(self):
        return self.__caption

    @property
    def position(self):
        return self.__position

    @property
    def coordinates(self):
        coordinates = MENU_NAME_POSITION[self.position]
        return coordinates

    def set_caption(self, menu_caption: str):
        self.__caption = menu_caption

    def display(self):
        if self.caption != 'NAME':
            coordinate_x, coordinate_y = self.coordinates
            draw_character(
                char_string=self.caption,
                char_coord_x=coordinate_x,
                char_coord_y=coordinate_y,
                char_color=MENU_CAPTION_COLOR,
                char_font_name=MENU_CAPTION_FONT_NAME,
                char_font_size=MENU_CAPTION_FONT_SIZE,
                char_font_bold=MENU_CAPTION_STYLE_BOLD,
                char_font_italic=MENU_CAPTION_STYLE_ITALIC,
                char_rotation_angle=0,
                char_anchor=True
            )


class MainMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Main Menu')


class SettingsMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Game settings')


class PauseMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Game paused')


class StartNewMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Start new game?')


class EndCurrentMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='End game?')


class GameWonMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Victory!')


class GameLostMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Defeat!')


class GameDrawMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Draw!')


class QuitMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Quit?')


def build_main_menu():
    collection = [
        Logo(),
        ClockfaceDivider(),
        MainMenu(),
        StartButton(init_position=[1, 0]),
        SettingsButton(init_position=[2, 0]),
        QuitButton(init_position=[5, 0]),
        AppInformation(),
    ]
    return collection


def build_settings_menu():
    collection = [
        Logo(),
        ClockfaceDivider(),
        SettingsMenu(),
        BackButton(init_position=[5, 0]),
        AppInformation(),
    ]
    return collection


def build_active_game():
    collection = [
        ClockfaceDivider(),
        LowerDivider(),
        TurnHistoryCaption(),
        PauseButton(init_position=[4, 0]),
        HintButton(init_position=[5, 1]),
        UndoButton(init_position=[5, 2]),
        AppInformation(),
    ]
    return collection


def build_paused_game():
    collection = [
        Logo(),
        ClockfaceDivider(),
        PauseMenu(),
        ResumeButton(init_position=[1, 0]),
        RestartButton(init_position=[2, 0]),
        SettingsButton(init_position=[3, 0]),
        MainMenuButton(init_position=[4, 0]),
        QuitButton(init_position=[5, 0]),
        AppInformation(),
    ]
    return collection


def build_start_new_confirmation():
    collection = [
        Logo(),
        ClockfaceDivider(),
        StartNewMenu(),
        YesButton(init_position=[1, 1]),
        NoButton(init_position=[1, 2]),
        AppInformation(),
    ]
    return collection


def build_end_current_confirmation():
    collection = [
        Logo(),
        ClockfaceDivider(),
        EndCurrentMenu(),
        YesButton(init_position=[1, 1]),
        NoButton(init_position=[1, 2]),
        AppInformation(),
    ]
    return collection


def build_game_won():
    collection = [
        Logo(),
        ClockfaceDivider(),
        GameWonMenu(),
        ContinueButton(init_position=[4, 0]),
        QuitButton(init_position=[5, 0]),
        AppInformation(),
    ]
    return collection


def build_game_lost():
    collection = [
        Logo(),
        ClockfaceDivider(),
        GameLostMenu(),
        ContinueButton(init_position=[4, 0]),
        QuitButton(init_position=[5, 0]),
        AppInformation(),
    ]
    return collection


def build_quit_confirmation():
    collection = [
        Logo(),
        ClockfaceDivider(),
        QuitMenu(),
        YesButton(init_position=[1, 1]),
        NoButton(init_position=[1, 2]),
        AppInformation(),
    ]
    return collection


def build_game_draw():
    collection = [
        Logo(),
        ClockfaceDivider(),
        GameDrawMenu(),
        ContinueButton(init_position=[4, 0]),
        QuitButton(init_position=[5, 0]),
        AppInformation(),
    ]
    return collection


class UI:
    def __init__(self):
        self.__mode = 0
        self.__prev = 0
        self.clockface = Clockface()
        self.collection = {0: build_main_menu(),                      # Main menu
                           1: build_settings_menu(),                  # Settings menu
                           2: build_active_game(),                    # Active game UI
                           3: build_paused_game(),                    # Paused game UI
                           4: build_start_new_confirmation(),         # Start new confirmation menu
                           5: build_end_current_confirmation(),       # End current confirmation menu
                           6: build_game_won(),                       # Game statistics UI (game won)
                           7: build_game_lost(),                      # Game statistics UI (game lost)
                           8: build_quit_confirmation(),              # App quit confirmation menu
                           9: build_game_draw(),                      # Game statistics UI (game draw)
                           }

        self.__show_clockface = False

    def reset_clockface(self):
        self.clockface.stopwatch.reset()

    @property
    def active_mode(self):
        return self.__mode

    @property
    def previous_mode(self):
        return self.__prev

    def set_mode(self, mode: int):
        self.__prev = self.__mode
        self.__mode = mode

    def hide_clockface(self):
        self.__show_clockface = False

    def show_clockface(self):
        self.__show_clockface = True

    def display(self):
        draw_rectangle_solid(
            rect_coord_x=UI_PANEL_POSITION_X,
            rect_coord_y=UI_PANEL_POSITION_Y,
            rect_width=UI_PANEL_WIDTH,
            rect_height=UI_PANEL_HEIGHT,
            rect_color=UI_PANEL_BACKGROUND_COLOR,
            rect_tilt=False
        )
        for stored in self.collection[self.__mode]:
            stored.display()
        if self.__show_clockface:
            self.clockface.display()


class Shell(arcade.Window):

    def __init__(self):

        super().__init__(
            width=GAME_WINDOW_WIDTH,
            height=GAME_WINDOW_HEIGHT,
            title=GAME_WINDOW_TITLE,
            fullscreen=GAME_WINDOW_FULLSCREEN,
            resizable=GAME_WINDOW_RESIZABLE,
            update_rate=GAME_WINDOW_UPDATE_RATE,
            antialiasing=GAME_WINDOW_ANTIALIASING
        )

        self.__dev_mode = True
        self.__test_mode = False
        self.__debug_mode = True

        self.board = Board()
        self.player = None
        self.ui = UI()

        self.active_player = 1                          # 1 = White, 2 = Black;
        self.active_checker = None                      # None, if deselected;

        self.highlight_checkers_move = False
        self.highlight_checkers_attack = False

        self.display_checkers = False

        self.game_running = False
        self.game_paused = False

    @staticmethod
    def setup():
        pass

    @staticmethod
    def run():
        arcade.set_background_color(color=GAME_WINDOW_BACKGROUND_COLOR)
        arcade.run()
        return

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
        attack_checkers = get_checkers_that_can_attack()
        for checker in attack_checkers:
            if checker.color == self.__player_color():
                must_attack = True
                break
        return must_attack

    def __player_cannot_move(self):
        cannot_move = True
        move_checkers = get_checkers_that_can_move()
        for checker in move_checkers:
            if checker.color == self.__player_color():
                if checker.can_move:
                    cannot_move = False
                    break
        return cannot_move

    def __player_has_no_checkers(self):
        no_checkers = True
        for row in SURFACE_GRID:
            for column in SURFACE_GRID[row]:
                position = [row, column]
                checker = get_checker_by_position(position)
                if checker is not None:
                    if checker.color == self.__player_color():
                        no_checkers = False
        return no_checkers

    def __next_player_turn(self):
        self.active_player = 2 if self.active_player == 1 else 1
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
        self.board.update()
        self.__board_clear()
        self.__board_fill()
        self.__board_update()

    def __board_update(self):
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
                        stamp_checker_highlight_attack(ch_coord_x=coordinates[0],
                                                       ch_coord_y=coordinates[1])

            def highlight_moves():
                for checker in checkers_move_list:
                    if checker.color == self.__player_color():
                        coordinates = checker.coordinates
                        stamp_checker_highlight_move(ch_coord_x=coordinates[0],
                                                     ch_coord_y=coordinates[1])

            checkers_move_list = get_checkers_that_can_move()
            checkers_attack_list = get_checkers_that_can_attack()
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
                    stamp_checker_highlight_move(ch_coord_x=checker_coordinates[0],
                                                 ch_coord_y=checker_coordinates[1])
                for move_position in move_list:
                    coordinates = convert_board_position_to_coordinates(conv_position=move_position)
                    move_position_coord_x, move_position_coord_y = coordinates
                    stamp_board_tile_highlight_move(tile_coord_x=move_position_coord_x,
                                                    tile_coord_y=move_position_coord_y)

            def highlight_attack_tiles():
                if self.active_checker.can_kill:
                    checker_coordinates = self.active_checker.coordinates
                    stamp_checker_highlight_attack(ch_coord_x=checker_coordinates[0],
                                                   ch_coord_y=checker_coordinates[1])
                for attack_position in attack_list:
                    coordinates = convert_board_position_to_coordinates(conv_position=attack_position)
                    move_position_coord_x, move_position_coord_y = coordinates
                    stamp_board_tile_highlight_attack(tile_coord_x=move_position_coord_x,
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
                self.stop_game()
                self.ui.set_mode(mode=7)
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

            def select_checker(checker_object):
                self.active_checker = checker_object

            def deselect_checker():
                if self.active_checker is not None:
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
                        else:
                            deselect_checker()

            def try_attacking():
                if clicked_position in self.active_checker.kill_list:
                    self.active_checker.move(clicked_position)
                    self.__board_update()
                    if not self.active_checker.can_kill:
                        self.__next_player_turn()
                        deselect_checker()

            if test_coordinates_are_valid(coordinates):
                if test_coordinates_in_board_boundaries(coordinates):
                    self.__remove_all_highlights()
                    checker_clicked = get_checker_by_coordinates(coordinates)
                    if checker_clicked is None:
                        if self.active_checker is not None:
                            clicked_position = convert_coordinates_to_board_position(coordinates)
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

            def _spawn_checker():
                new_checker = spawn_checker(spawn_position=clicked_position,
                                            spawn_color='White',
                                            spawn_queen=False)
                new_checker.dev = True
                SURFACE_GRID[clicked_row][clicked_column] = new_checker

            def switch_color(checker_object):
                checker_object.color = 'White' if checker_object.color == 'Black' else 'Black'

            def promote_checker(checker_object):
                checker_object.promote()

            def remove_checker():
                SURFACE_GRID[clicked_row][clicked_column] = None

            if test_coordinates_are_valid(coordinates):
                if test_coordinates_in_board_boundaries(coordinates):
                    checker_clicked = get_checker_by_coordinates(coordinates)
                    clicked_position = convert_coordinates_to_board_position(coordinates)

                    if test_position_can_be_used(clicked_position):
                        clicked_row, clicked_column = clicked_position
                        if checker_clicked is None:
                            _spawn_checker()
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
                if not self.highlight_checkers_move:
                    self.highlight_checkers_move = True
                if not self.highlight_checkers_attack:
                    self.highlight_checkers_attack = True

            def hide_hint():
                if self.highlight_checkers_move:
                    self.highlight_checkers_move = False
                if self.highlight_checkers_attack:
                    self.highlight_checkers_attack = False

            def hint_enabled():
                hint_status = False
                if self.highlight_checkers_move and self.highlight_checkers_attack:
                    hint_status = True
                return hint_status

            for ui_element in self.ui.collection[self.ui.active_mode]:
                if isinstance(ui_element, Button):
                    if click_coordinates_in_button_boundaries(coordinates, ui_element):

                        # Main menu:
                        if self.ui.active_mode == 0:
                            if ui_element.ID == BUTTON_ID_START_GAME:
                                self.ui.set_mode(mode=2)
                                self.start_game()
                                self.display_checkers = True
                            elif ui_element.ID == BUTTON_ID_SETTINGS:
                                self.ui.hide_clockface()
                                self.ui.set_mode(mode=1)
                            elif ui_element.ID == BUTTON_ID_QUIT:
                                self.ui.set_mode(mode=8)

                        # Settings menu:
                        elif self.ui.active_mode == 1:
                            if ui_element.ID == BUTTON_ID_BACK:
                                if not self.game_running:
                                    self.ui.set_mode(mode=0)
                                else:
                                    self.ui.set_mode(mode=3)

                        # Active game mode:
                        elif self.ui.active_mode == 2:
                            if ui_element.ID == BUTTON_ID_PAUSE:
                                self.ui.set_mode(mode=3)
                                self.game_paused = True
                                self.ui.clockface.stopwatch.pause()
                                self.ui.hide_clockface()
                            elif ui_element.ID == BUTTON_ID_HINT:
                                if hint_enabled():
                                    hide_hint()
                                else:
                                    show_hint()
                            elif ui_element.ID == BUTTON_ID_UNDO:
                                pass

                        # Paused game mode:
                        elif self.ui.active_mode == 3:
                            if ui_element.ID == BUTTON_ID_RESUME:
                                self.ui.set_mode(mode=2)
                                if self.game_paused:
                                    self.game_paused = False
                                self.ui.show_clockface()
                                self.ui.clockface.stopwatch.unpause()
                            elif ui_element.ID == BUTTON_ID_RESTART_GAME:
                                self.ui.set_mode(mode=4)
                            elif ui_element.ID == BUTTON_ID_SETTINGS:
                                self.ui.set_mode(mode=1)
                            elif ui_element.ID == BUTTON_ID_MAIN_MENU:
                                self.ui.set_mode(mode=5)
                            elif ui_element.ID == BUTTON_ID_QUIT:
                                self.ui.set_mode(mode=8)

                        # Start new game confirmation menu:
                        elif self.ui.active_mode == 4:
                            if ui_element.ID == BUTTON_ID_YES:
                                self.ui.set_mode(mode=7)
                                self.stop_game()
                            elif ui_element.ID == BUTTON_ID_NO:
                                self.ui.set_mode(mode=3)

                        # End current game confirmation menu:
                        elif self.ui.active_mode == 5:
                            if ui_element.ID == BUTTON_ID_YES:
                                self.ui.set_mode(mode=7)
                                self.stop_game()
                            elif ui_element.ID == BUTTON_ID_NO:
                                self.ui.set_mode(mode=3)

                        # Game results (Game won):
                        elif self.ui.active_mode == 6:
                            if ui_element.ID == BUTTON_ID_CONTINUE:
                                self.ui.clockface.stopwatch.stop()
                                self.ui.clockface.stopwatch.reset()
                                self.ui.hide_clockface()
                                self.display_checkers = False
                                self.ui.set_mode(mode=0)
                            elif ui_element.ID == BUTTON_ID_QUIT:
                                self.ui.set_mode(mode=8)

                        # Game results (Game lost/force end):
                        elif self.ui.active_mode == 7:
                            if ui_element.ID == BUTTON_ID_CONTINUE:
                                self.ui.clockface.stopwatch.stop()
                                self.ui.clockface.stopwatch.reset()
                                self.ui.hide_clockface()
                                self.display_checkers = False
                                self.ui.set_mode(mode=0)
                            elif ui_element.ID == BUTTON_ID_QUIT:
                                self.ui.set_mode(mode=8)

                        # Quit confirmation menu:
                        elif self.ui.active_mode == 8:
                            if ui_element.ID == BUTTON_ID_YES:
                                quit()
                            elif ui_element.ID == BUTTON_ID_NO:
                                prev_mode = self.ui.previous_mode
                                self.ui.set_mode(mode=prev_mode)

                        # Game results (Game draw):
                        elif self.ui.active_mode == 9:
                            if ui_element.ID == BUTTON_ID_CONTINUE:
                                self.ui.clockface.stopwatch.stop()
                                self.ui.clockface.stopwatch.reset()
                                self.ui.hide_clockface()
                                self.display_checkers = False
                                self.ui.set_mode(mode=0)
                            elif ui_element.ID == BUTTON_ID_QUIT:
                                self.ui.set_mode(mode=8)


        click_coordinates = [x, y]
        if button == arcade.MOUSE_BUTTON_LEFT:
            if test_coordinates_in_board_boundaries(click_coordinates):
                if self.game_running and not self.game_paused:
                    handle_board_click(click_coordinates)
            else:
                handle_panel_click(click_coordinates)
        else:
            if self.__test_mode:
                handle_board_click_dev(click_coordinates)

    def update(self, delta_time: float):
        pass


zen_checkers_game_window = Shell()
zen_checkers_game_window.setup()
zen_checkers_game_window.run()
