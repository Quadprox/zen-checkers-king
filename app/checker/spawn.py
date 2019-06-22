from app.checker import mono
from app.board import convert
from tools import console


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
    if spawn_color in ('White', 'Black'):
        spawned_checker = __checker_predefined(spawn_position, spawn_color, spawn_queen)
    else:
        spawned_checker = __checker_undefined(spawn_position)
    console.echo(
        message='Spawned {checker} at {position}'.format(
            checker=spawned_checker,
            position=convert.board_position_to_alphanumeric_index(conv_position=spawn_position)),
        level=2)
    return spawned_checker
