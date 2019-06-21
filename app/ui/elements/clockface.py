from tools.pencil import stamp
from tools.clock.stopwatch import Stopwatch
from app.ui import mapping


class Clockface:
    def __init__(self):
        self.__position = 1
        self.stopwatch = Stopwatch()

    @property
    def time(self):
        return self.stopwatch.elapsed()

    def display(self):
        coordinate_x, coordinate_y = mapping.CLOCKFACE_POSITIONS[1]
        stamp.clockface(
            cf_coord_x=coordinate_x,
            cf_coord_y=coordinate_y,
            cf_value=self.time
        )