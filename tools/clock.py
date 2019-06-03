import time
import math


def __round(value: float):
    rounded_value = math.floor(value)
    return rounded_value


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
    proper = [__round(hours),
              __round(minutes),
              __round(seconds)]
    return proper
