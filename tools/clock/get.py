from datetime import datetime
from tools.clock import convert


def time_dt():
    time = datetime.now()
    return time


def time_formatted():
    time = convert.dt_to_list(datetime_value=time_dt())
    return time


def seconds_from_dt(datetime_value):
    converted = datetime.strftime(datetime_value, '%S')
    return converted


def minutes_from_dt(datetime_value):
    converted = datetime.strftime(datetime_value, '%M')
    return converted


def hours_from_dt(datetime_value):
    converted = datetime.strftime(datetime_value, '%H')
    return converted