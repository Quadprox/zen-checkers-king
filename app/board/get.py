from app.board import test, convert, mapping


def checker_by_position(check_position: list):
    if test.position_can_be_used(check_position):
        row = check_position[0]
        column = check_position[1]
        if mapping.SURFACE_GRID[row][column] is not None:
            checker = mapping.SURFACE_GRID[row][column]
            return checker


def checker_by_coordinates(check_coordinates: list):
    if test.coordinates_in_board_boundaries(check_coordinates):
        board_position = convert.coordinates_to_board_position(check_coordinates)
        return checker_by_position(board_position)


def checkers_that_can_move():
    checkers_can_attack_list = []
    for row in mapping.SURFACE_GRID:
        for column in mapping.SURFACE_GRID[row]:
            if mapping.SURFACE_GRID[row][column] is not None:
                checker = mapping.SURFACE_GRID[row][column]
                if checker.can_move:
                    checkers_can_attack_list.append(checker)
    return checkers_can_attack_list


def checkers_that_can_attack():
    checkers_can_attack_list = []
    for row in mapping.SURFACE_GRID:
        for column in mapping.SURFACE_GRID[row]:
            if mapping.SURFACE_GRID[row][column] is not None:
                checker = mapping.SURFACE_GRID[row][column]
                if checker.can_kill:
                    checkers_can_attack_list.append(checker)
    return checkers_can_attack_list
