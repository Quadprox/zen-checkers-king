import tools.clock.convert as convert


def dt(dt_start, dt_end):
    list_start = convert.dt_to_list(dt_start)
    list_end = convert.dt_to_list(dt_end)
    difference = lists(list_start, list_end)
    return difference


def lists(list_start: list, list_end: list):
    start = convert.list_to_seconds(list_start)
    end = convert.list_to_seconds(list_end)
    difference = end - start
    return difference

