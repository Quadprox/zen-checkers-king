import os


# General project information and directories:
PROJECT_NAME = 'Zen Checkers King'
PROJECT_APP_VERSION = '0.7.0'
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
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
UI_PANEL_WIDTH = TILE_SIDE_LEN * 3
UI_PANEL_HEIGHT = BOARD_SIDE_LEN
UI_PANEL_BACKGROUND_COLOR = CHECKER_COLOR_WHITE_MAIN
UI_PANEL_POSITION_X = int(BOARD_SIDE_LEN + UI_PANEL_WIDTH / 2)
UI_PANEL_POSITION_Y = int(BOARD_SIDE_LEN / 2)

# Button surface settings:
BUTTON_MARGIN_X = 8
BUTTON_MARGIN_Y = 12
BUTTON_LARGE_WIDTH = int(UI_PANEL_WIDTH - BUTTON_MARGIN_X * 2)
BUTTON_LARGE_HEIGHT = 64
BUTTON_SMALL_WIDTH = int(UI_PANEL_WIDTH / 2 - BUTTON_MARGIN_X + BUTTON_MARGIN_X / 2)
BUTTON_SMALL_HEIGHT = BUTTON_LARGE_HEIGHT
BUTTON_BORDER_LEN = 4
BUTTON_BORDER_COLOR = TILE_COLOR_BLACK
BUTTON_FILLED_COLOR = TILE_HIGHLIGHT_COLOR_ATTACK
BUTTON_CAPTION_FONT_SIZE = 12
BUTTON_CAPTION_FONT_NAME = 'Monospaced'.lower()
BUTTON_CAPTION_STYLE_BOLD = False
BUTTON_CAPTION_STYLE_ITALIC = False
BUTTON_CAPTION_COLOR = BUTTON_BORDER_COLOR
BUTTON_SMALL_POSITION_X_LEFT = int(BOARD_SIDE_LEN + BUTTON_MARGIN_X + BUTTON_SMALL_WIDTH / 2)
BUTTON_SMALL_POSITION_X_RIGHT = int(BOARD_SIDE_LEN + BUTTON_MARGIN_X * 2 + BUTTON_SMALL_WIDTH / 2)

#
CLOCKFACE_CAPTION_COLOR = TILE_COLOR_BLACK
CLOCKFACE_CAPTION_FONT_SIZE = 24
CLOCKFACE_CAPTION_FONT_NAME = 'Monospaced'.lower()
CLOCKFACE_CAPTION_STYLE_BOLD = False
CLOCKFACE_CAPTION_STYLE_ITALIC = False

# Game window settings:
GAME_WINDOW_BACKGROUND_COLOR = ERROR_COLOR_MAIN
GAME_WINDOW_WIDTH = BOARD_SIDE_LEN + UI_PANEL_WIDTH
GAME_WINDOW_HEIGHT = BOARD_SIDE_LEN
GAME_WINDOW_TITLE = f'{PROJECT_NAME} v{PROJECT_APP_VERSION}'
GAME_WINDOW_RESIZABLE = False
GAME_WINDOW_FULLSCREEN = False
GAME_WINDOW_UPDATE_RATE = 1/60
GAME_WINDOW_ANTIALIASING = True
