from datetime import datetime


def get_seconds(datetime_value):
    converted = datetime.strftime(datetime_value, '%S')
    return converted


def get_minutes(datetime_value):
    converted = datetime.strftime(datetime_value, '%M')
    return converted


def get_hours(datetime_value):
    converted = datetime.strftime(datetime_value, '%H')
    return converted


def convert(datetime_value):
    seconds = get_seconds(datetime_value)
    minutes = get_minutes(datetime_value)
    hours = get_hours(datetime_value)
    converted = [hours, minutes, seconds]
    return converted


def now():
    time = datetime.now()
    return time
