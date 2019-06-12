from tools.clock import convert


def __is_type_list(value):
    return True if isinstance(value, list) else False


def __is_type_integer(value):
    return True if isinstance(value, int) else False


def list_adjust(adj_list: list, mod: int, number: int):
    if __is_type_list(adj_list):
        if __is_type_integer(mod) and __is_type_integer(number):
            conv_seconds = convert.list_to_seconds(adj_list)
            adj_seconds = conv_seconds + int(mod) * int(number)
            adjusted_list = convert.seconds_to_list(adj_seconds)
            return adjusted_list


