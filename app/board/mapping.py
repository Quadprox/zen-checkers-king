from app.board import test


SURFACE_GRID = {}


def clear():
    global SURFACE_GRID

    for row in SURFACE_GRID.keys():
        for column in SURFACE_GRID[row].keys():
            SURFACE_GRID[row][column] = None


def fill():
    global SURFACE_GRID

    for row in SURFACE_GRID.keys():
        for column in SURFACE_GRID[row].keys():
            pass
            # board_position = [row, column]
            # if test.position_can_spawn_checker(check_position=board_position):
            #     if SURFACE_GRID[row][column] is None:
            #         checker = spawn.checker(spawn_position=board_position,
            #                                 spawn_color='',
            #                                 spawn_queen=False)
            #         SURFACE_GRID[row][column] = checker
