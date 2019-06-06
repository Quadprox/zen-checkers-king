


class Player:

    def __init__(self, player_name):
        self.__name = player_name

    @property
    def name(self):
        return self.__name.capitalize()
