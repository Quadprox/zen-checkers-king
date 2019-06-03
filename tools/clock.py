import time


def now():
    current_time = time.time()
    return current_time


def convert(value: float):
    seconds_in_minute = 60
    minutes_in_hour = 60
    seconds = value
    minutes = seconds // seconds_in_minute
    seconds = seconds - minutes * seconds_in_minute
    hours = minutes // minutes_in_hour
    minutes = minutes - hours * minutes_in_hour
    proper = [int(hours),
              int(minutes),
              int(seconds)]
    return proper
