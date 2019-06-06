from app.board import get, test, mapping


POINTER_POS_CHECKER = None
POINTER_POS_EMPTY = False
POINTER_POS_INVALID = False
POINTER_FORWARD = False


def __pointer(check_position: list):
    global POINTER_POS_CHECKER, POINTER_POS_EMPTY, POINTER_POS_INVALID

    POINTER_POS_CHECKER = None
    POINTER_POS_EMPTY = False
    POINTER_POS_INVALID = False

    if test.position_is_valid(check_position):
        POINTER_POS_INVALID = False
        POINTER_POS_CHECKER = get.checker_by_position(check_position)
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
            if not test.position_is_valid(position_between):
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
            mapping.SURFACE_GRID[row][column] = None

    # Moving the checker from old to new positions:
    mapping.SURFACE_GRID[checker_object.position[0]][checker_object.position[1]] = None     # Delete old instance
    mapping.SURFACE_GRID[new_position[0]][new_position[1]] = checker_object                 # Move instance to position
    checker_object.set_position(new_position)
