from tools.pencil import stamp
from tools import console
from app.ui import mapping
from app import settings


class Button:

    ID = None

    def __init__(self,init_position: list, init_filled: bool = False):
        self.__caption = None
        self.__position = init_position
        self.__size = 'large' if init_position[1] == 0 else 'small'
        
        self.filled = init_filled

    def __str__(self):
        return f'UI element ({self.size} button \"{self.caption}\")'

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
        self.__caption = str(caption).upper()

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
    ID = settings.BUTTON_ID_START_GAME
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Start')


class SettingsButton(Button):
    ID = settings.BUTTON_ID_SETTINGS
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Settings')


class QuitButton(Button):
    ID = settings.BUTTON_ID_QUIT
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Quit')


class PauseButton(Button):
    ID = settings.BUTTON_ID_PAUSE
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Pause')


class ResumeButton(Button):
    ID = settings.BUTTON_ID_RESUME
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Resume')


class RestartButton(Button):
    ID = settings.BUTTON_ID_RESTART_GAME
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Restart')


class YesButton(Button):
    ID = settings.BUTTON_ID_YES
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Yes')


class NoButton(Button):
    ID = settings.BUTTON_ID_NO
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('No')


class HintButton(Button):
    ID = settings.BUTTON_ID_HINT
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Hint')


class UndoButton(Button):
    ID = settings.BUTTON_ID_UNDO
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Undo')


class BackButton(Button):
    ID = settings.BUTTON_ID_BACK
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Back')


class MainMenuButton(Button):
    ID = settings.BUTTON_ID_MAIN_MENU
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Main Menu')

class ContinueButton(Button):
    ID = settings.BUTTON_ID_CONTINUE
    def __init__(self, init_position: list, init_filled: bool = False):
        super().__init__(init_position, init_filled)
        self.set_caption('Continue')