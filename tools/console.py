import tools.clock as clock


def timestamp():
    time_unrefined = clock.convert(clock.now())
    hours, minutes, seconds = time_unrefined
    time = f'{hours}:{minutes}:{seconds}'
    return time


def echo(message: str):
    response = f'{timestamp()} -- {message}'
    print(response)

echo(1)