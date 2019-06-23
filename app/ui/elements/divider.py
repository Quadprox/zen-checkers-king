from tools.pencil import stamp
from app.ui import mapping


class Divider:
    def __init__(self):
        self.__position = 1

    def __str__(self):
        return f'UI element (block line divider)'

    @property
    def position(self):
        return self.__position

    def set_position(self, new_position: int):
        self.__position = new_position

    @property
    def coordinates(self):
        coordinates = mapping.DIVIDER_POSITIONS[self.position]
        return coordinates

    def display(self):
        coordinate_x, coordinate_y = self.coordinates
        stamp.div(
            div_coord_x=coordinate_x,
            div_coord_y=coordinate_y
        )


class ClockfaceDivider(Divider):
    def __init__(self):
        super().__init__()
        self.set_position(new_position=1)


class LowerDivider(Divider):
    def __init__(self):
        super().__init__()
        self.set_position(new_position=2)