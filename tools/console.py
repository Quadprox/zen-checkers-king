from datetime import datetime


def timestamp():
    time = datetime.now()
    timestamp = datetime.strftime(time, '%H:%M:%S')
    return timestamp


def echo(message: str):
    response = f'{timestamp()} -- {message}'
    print(response)

echo(1)