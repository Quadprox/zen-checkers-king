from datetime import datetime


def __now_dt():
    time = datetime.now()
    return time


def __now_formatted():
    time = datetime.strftime(__now_dt(), '%H:%M:%S')
    return time


def now(formatted: bool = True):
    generate = {
        True: lambda: __now_formatted(),
        False: lambda: __now_dt()
    }
    time = generate[formatted]()
    return time