import app.board.test as test
import app.settings as settings


def board_position_to_coordinates(conv_position: list):
    if test.position_is_valid(conv_position):
        row, column = conv_position[0], conv_position[1]
        coord_x = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2 + settings.TILE_SIDE_LEN * (column - 1))
        coord_y = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2 + settings.TILE_SIDE_LEN * (row - 1))
        coordinates = [coord_x, coord_y]
        return coordinates


def board_position_to_alphanumeric_index(conv_position: list):
    if test.position_is_valid(conv_position):
        row, column = conv_position[0], conv_position[1]
        letter = settings.BOARD_LETTER_INDEX[column - 1]
        number = row
        alphanumeric_index = f'{letter}{number}'
        return alphanumeric_index


def coordinates_to_board_position(conv_coordinates: list):
    if test.coordinates_are_valid(conv_coordinates):
        coord_x, coord_y = conv_coordinates[0], conv_coordinates[1]
        row = 1 + ((coord_y - settings.BOARD_MARGIN_LEN) // settings.TILE_SIDE_LEN)
        column = 1 + ((coord_x - settings.BOARD_MARGIN_LEN) // settings.TILE_SIDE_LEN)
        position = [row, column]
        return position
