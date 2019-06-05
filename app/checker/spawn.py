import app.board.test as test
import app.checker.mono as mono


def __checker_empty():
    new_checker = mono.Checker(init_position=[],
                               init_color='',
                               init_type_queen=False)
    return new_checker


def __checker_predefined(spawn_position: list, spawn_color: str, spawn_queen: bool = False):
    new_checker = mono.Checker(init_position=spawn_position,
                               init_color=spawn_color,
                               init_type_queen=spawn_queen)
    return new_checker


def __checker_undefined(spawn_position: list):
    spawn_color = 'White' if spawn_position[0] in (1, 2, 3) else 'Black'
    new_checker = mono.Checker(init_position=spawn_position,
                               init_color=spawn_color,
                               init_type_queen=False)
    return new_checker


def checker(spawn_position: list, spawn_color: str, spawn_queen: bool = False):
    if test.position_can_spawn_checker(spawn_position):
        if spawn_color in ('White', 'Black'):
            return __checker_predefined(spawn_position, spawn_color, spawn_queen)
        else:
            return __checker_undefined(spawn_position)
    else:
        return __checker_empty()
