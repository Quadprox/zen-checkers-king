from tools.pencil import stamp
from app.ui import mapping


class Button:
    def __init__(self,init_position: list, init_filled: bool = False):
        self.__caption = None
        self.__size = None
        self.__position = init_position
        
        self.filled = init_filled

    @property
    def size(self):
        return self.__size

    @property
    def caption(self):
        return self.__caption

    @property
    def position(self):
        return self.__position

    @property
    def coordinates(self):
        position, align = self.__position
        conv_coordinates = mapping.BUTTON_GRID_POSITIONS[position][align]
        return conv_coordinates

    @property
    def is_valid(self):
        result = True
        if self.caption is None or self.size is None:
            result = False
        return result

    def set_caption(self, caption: str):
        self.__caption = str(caption).lower()

    def set_size(self, size: str):
        self.__size = str(size).lower()

    def display(self):
        if self.is_valid:
            coordinate_x, coordinate_y = self.coordinates
            stamp.button(
                b_coord_x=coordinate_x,
                b_coord_y=coordinate_y,
                b_size=self.size,
                b_caption=self.caption,
                b_filled=self.filled
            )


class StartButton(Button):
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Start')


class SettingsButton(Button):
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Settings')


class QuitButton(Button):
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Quit')


class PauseButton(Button):
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Pause')


class RestartButton(Button):
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Restart')


class EndCurrentButton(Button):
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('End game')


class HintButton(Button):
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Hint')


class UndoButton(Button):
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Undo')
