import app.settings as settings


def __is_type_list(value):
    return True if isinstance(value, list) else False


def __is_type_integer(value):
    return True if isinstance(value, int) else False


def __is_even(number: int):
    return True if number % 2 == 0 else False


def __is_positive(number: int):
    return True if number > 0 else False


def position_is_valid(check_position: list):
    test_result = False
    if __is_type_list(check_position):
        row = check_position[0]
        column = check_position[1]
        if __is_type_integer(row) and __is_type_integer(column):
            row_range = range(1, settings.BOARD_ROW_COUNT + 1)
            column_range = range(1, settings.BOARD_COLUMN_COUNT + 1)
            if row in row_range and column in column_range:
                test_result = True
    return test_result


def position_can_be_used(check_position: list):
    test_result = False
    if position_is_valid(check_position):
        row = check_position[0]
        column = check_position[1]
        if __is_even(row) and not __is_even(column) or \
           __is_even(column) and not __is_even(row):
            test_result = True
    return test_result


def position_can_spawn_checker(check_position: list):
    test_result = False
    if position_can_be_used(check_position):
        row = check_position[0]
        if row not in (4, 5):
            test_result = True
    return test_result


def coordinates_are_valid(check_coordinates: list):
    test_result = False
    if __is_type_list(check_coordinates):
        coord_x = check_coordinates[0]
        coord_y = check_coordinates[1]
        if __is_type_integer(coord_x) and __is_type_integer(coord_y):
            if __is_positive(coord_x) and __is_positive(coord_y):
                test_result = True
    return test_result



def coordinates_in_board_boundaries(check_coordinates: list):
    test_result = False
    if coordinates_are_valid(check_coordinates):
        boundaries_range_x = range(settings.BOARD_BOUNDARY_LEFT, settings.BOARD_BOUNDARY_RIGHT)
        boundaries_range_y = range(settings.BOARD_BOUNDARY_BOTTOM, settings.BOARD_BOUNDARY_TOP)
        coord_x = check_coordinates[0]
        coord_y = check_coordinates[1]
        coord_x_in_range = True if coord_x in boundaries_range_x else False
        coord_y_in_range = True if coord_y in boundaries_range_y else False
        if coord_x_in_range and coord_y_in_range:
            test_result = True
    return test_result
