from tools.clock import mono as clock, convert
from app import session


def timestamp():
    time_unrefined = clock.now(formatted=False)
    time_formatted = convert.dt_to_list(time_unrefined)
    hours, minutes, seconds = time_formatted
    time = f'{hours}:{minutes}:{seconds}'
    return time


def echo(message: str, level: int = 1):
    separator = ''
    if level > 1:
        separator += '˪ ' * (level - 1)
    if session.DEBUG_MODE:
        if level == 1:
            print()
        response = f'{timestamp()} - DEBUG MODE: {separator}{message}'
        print(response)
