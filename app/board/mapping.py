from app.board import test
from app.checker import spawn


SURFACE_GRID = {}
SURFACE_EMPTY = False


def clear():
    global SURFACE_GRID, SURFACE_EMPTY

    for row in SURFACE_GRID.keys():
        for column in SURFACE_GRID[row].keys():
            if SURFACE_GRID[row][column] is not None:
                SURFACE_GRID[row][column] = None
    SURFACE_EMPTY = True


def fill():
    global SURFACE_GRID, SURFACE_EMPTY

    for row in SURFACE_GRID.keys():
        for column in SURFACE_GRID[row].keys():
            board_position = [row, column]
            if test.position_can_spawn_checker(check_position=board_position):
                if SURFACE_GRID[row][column] is None:
                    checker = spawn.checker(spawn_position=board_position,
                                            spawn_color='',
                                            spawn_queen=False)
                    SURFACE_GRID[row][column] = checker
    SURFACE_EMPTY = False


def empty():
    status = SURFACE_EMPTY
    return status

