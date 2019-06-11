import tools.clock.get as get


def dt_to_list(datetime_value):
    seconds = get.seconds_from_dt(datetime_value)
    minutes = get.minutes_from_dt(datetime_value)
    hours = get.hours_from_dt(datetime_value)
    converted = [hours, minutes, seconds]
    return converted


def list_to_seconds(conv_list: list):
    hours, minutes, seconds = conv_list
    seconds_in_minute = 60
    minutes_in_hour = 60
    converted_seconds = int(int(seconds) +
                            int(minutes) * seconds_in_minute +
                            int(hours) * minutes_in_hour * seconds_in_minute)
    return converted_seconds


def seconds_to_list(conv_seconds: int):
    seconds_in_minute = 60
    minutes_in_hour = 60
    hours = conv_seconds // seconds_in_minute // minutes_in_hour
    minutes = conv_seconds // seconds_in_minute
    seconds = conv_seconds - minutes * minutes_in_hour
    converted_list = [hours, minutes, seconds]
    return converted_list