from tools.pencil import stamp
from app.ui import mapping


class Button:
    def __init__(self, init_caption: str, init_position: list, init_size: str, init_filled: bool = False):
        self.__caption = init_caption
        self.__position = init_position
        self.__size = init_size
        
        self.filled = init_filled

    @property
    def size(self):
        return self.__size

    @property
    def caption(self):
        return self.caption

    @property
    def position(self):
        return self.__position

    @property
    def coordinates(self):
        conv_coordinates = mapping.convert_grid_position_to_coordinates(self.__position)
        return conv_coordinates

    def display(self):
        coordinate_x, coordinate_y = self.coordinates
        stamp.button(
            b_coord_x=coordinate_x,
            b_coord_y=coordinate_y,
            b_size=self.size,
            b_caption=self.caption,
            b_filled=self.filled
        )