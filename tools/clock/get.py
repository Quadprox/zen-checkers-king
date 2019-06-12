from datetime import datetime


def seconds_from_dt(datetime_value):
    converted = datetime.strftime(datetime_value, '%S')
    return converted


def minutes_from_dt(datetime_value):
    converted = datetime.strftime(datetime_value, '%M')
    return converted


def hours_from_dt(datetime_value):
    converted = datetime.strftime(datetime_value, '%H')
    return converted
