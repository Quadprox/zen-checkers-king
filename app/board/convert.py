import app.board.test as test
from app import settings, session
from tools import console


def board_position_to_coordinates(conv_position: list):
    if test.position_is_valid(conv_position):
        row, column = conv_position
        coord_x = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2 + settings.TILE_SIDE_LEN * (column - 1))
        coord_y = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2 + settings.TILE_SIDE_LEN * (row - 1))
        coordinates = [coord_x, coord_y]
        return coordinates
    else:
        error_message = f'Unable to convert board position {conv_position} to coordinates.' \
                        f'Position {conv_position} is invalid!'
        console.error(error_message)


def board_position_to_alphanumeric_index(conv_position: list):
    if test.position_is_valid(conv_position):
        row, column = conv_position
        letter = settings.BOARD_LETTER_INDEX[column - 1]
        number = row
        alphanumeric_index = f'{letter}{number}'
        return alphanumeric_index
    else:
        error_message = f'Unable to convert board position {conv_position} to alphanumeric index.' \
                        f'Position {conv_position} is invalid!'
        console.error(error_message)


def coordinates_to_board_position(conv_coordinates: list):
    if test.coordinates_are_valid(conv_coordinates):
        coord_x, coord_y = conv_coordinates
        row = 1 + ((coord_y - settings.BOARD_MARGIN_LEN) // settings.TILE_SIDE_LEN)
        column = 1 + ((coord_x - settings.BOARD_MARGIN_LEN) // settings.TILE_SIDE_LEN)
        position = [row, column]
        return position
    else:
        error_message = f'Unable to convert coordinates {conv_coordinates} to board position.' \
                        f'Coordinates {conv_coordinates} are invalid!'
        console.error(error_message)
