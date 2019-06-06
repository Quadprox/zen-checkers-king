from app.board import get, test


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


def get_move_list(checker_object):

    def add_to_moves(position):
        checker_move_list[0].append(position)

    def add_to_attacks(position):
        checker_move_list[1].append(position)

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
                                add_to_moves(peek_position)
                                if not checker_queen:
                                    break
                            else:
                                if not checker_queen:
                                    break
                                else:
                                    add_to_moves(peek_position)
                        else:
                            add_to_moves(peek_position)
                            add_to_attacks(peek_position)
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
