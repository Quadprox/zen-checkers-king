from tools.pencil import draw
from app.ui import mapping
from app import settings


class Logo:
    def __init__(self):
        self._upper_caption = 'zen'
        self._lower_caption = 'Checkers'

    def __str__(self):
        return f'UI element (app logo \"{self.caption}\")'

    @property
    def caption(self):
        caption = f'{self._upper_caption} {self._lower_caption}'
        return caption

    @property
    def coordinates(self):
        coordinates = [[660, 524],      # Upper caption
                       [660, 496]]      # Lower caption
        return coordinates

    def display(self):
        upper_coordinates, lower_coordinates = self.coordinates
        upper_coord_x, upper_coord_y = upper_coordinates
        lower_coord_x, lower_coord_y = lower_coordinates
        draw.character(
            char_string=self._upper_caption,
            char_coord_x=upper_coord_x,
            char_coord_y=upper_coord_y,
            char_color=settings.LOGO_CAPTION_COLOR,
            char_font_name=settings.LOGO_CAPTION_FONT_NAME,
            char_font_size=22,
            char_font_bold=settings.LOGO_CAPTION_STYLE_BOLD,
            char_font_italic=settings.LOGO_CAPTION_STYLE_ITALIC,
            char_rotation_angle=0,
            char_anchor=True
        )
        draw.character(
            char_string=self._lower_caption.upper(),
            char_coord_x=lower_coord_x,
            char_coord_y=lower_coord_y,
            char_color=settings.LOGO_CAPTION_COLOR,
            char_font_name=settings.LOGO_CAPTION_FONT_NAME,
            char_font_size=28,
            char_font_bold=settings.LOGO_CAPTION_STYLE_BOLD,
            char_font_italic=settings.LOGO_CAPTION_STYLE_ITALIC,
            char_rotation_angle=0,
            char_anchor=True
        )


class AppInformation:
    def __init__(self):
        self.__caption= settings.GAME_WINDOW_TITLE
        self.__position = 1

    @property
    def caption(self):
        return self.__caption

    @property
    def position(self):
        return self.__position

    @property
    def coordinates(self):
        coordinates = mapping.APP_INFORMATION[self.position]
        return coordinates

    def display(self):
        coordinate_x, coordinate_y = self.coordinates
        draw.character(
            char_string=self.caption,
            char_coord_x=coordinate_x,
            char_coord_y=coordinate_y,
            char_color=settings.CLOCKFACE_CAPTION_COLOR,
            char_rotation_angle=0,
            char_font_name='tahoma',
            char_font_size=12,
            char_font_bold=False,
            char_font_italic=False,
            char_anchor=True
        )


class TurnHistoryCaption:
    def __init__(self):
        self.__position = 0
        self.__caption = 'Turn history'

    def __str__(self):
        return f'UI element (turn history caption \"{self.caption}\")'

    @property
    def caption(self):
        return self.__caption

    @property
    def position(self):
        return self.__position

    @property
    def coordinates(self):
        coordinates = mapping.TURN_HISTORY_POSITIONS[self.position]
        return coordinates

    def set_caption(self, menu_caption: str):
        self.__caption = menu_caption

    def display(self):
        coordinate_x, coordinate_y = self.coordinates
        draw.character(
            char_string=self.caption,
            char_coord_x=coordinate_x,
            char_coord_y=coordinate_y,
            char_color=settings.CLOCKFACE_CAPTION_COLOR,
            char_font_name='georgia',
            char_font_size=12,
            char_font_bold=False,
            char_font_italic=False,
            char_rotation_angle=0,
            char_anchor=True
        )


class MenuName:
    def __init__(self):
        self.__position = 1
        self.__caption = 'NAME'

    def __str__(self):
        return f'UI element (menu name caption \"{self.caption}\")'

    @property
    def caption(self):
        return self.__caption

    @property
    def position(self):
        return self.__position

    @property
    def coordinates(self):
        coordinates = mapping.MENU_NAME_POSITION[self.position]
        return coordinates

    def set_caption(self, menu_caption: str):
        self.__caption = menu_caption

    def display(self):
        if self.caption != 'NAME':
            coordinate_x, coordinate_y = self.coordinates
            draw.character(
                char_string=self.caption,
                char_coord_x=coordinate_x,
                char_coord_y=coordinate_y,
                char_color=settings.MENU_CAPTION_COLOR,
                char_font_name=settings.MENU_CAPTION_FONT_NAME,
                char_font_size=settings.MENU_CAPTION_FONT_SIZE,
                char_font_bold=settings.MENU_CAPTION_STYLE_BOLD,
                char_font_italic=settings.MENU_CAPTION_STYLE_ITALIC,
                char_rotation_angle=0,
                char_anchor=True
            )


class MainMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Main Menu')


class SettingsMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Game settings')


class PauseMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Game paused')


class StartNewMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Start new game?')


class EndCurrentMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='End game?')


class GameWonMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Victory!')


class GameLostMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Defeat!')


class GameDrawMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Draw!')


class QuitMenu(MenuName):
    def __init__(self):
        super().__init__()
        self.set_caption(menu_caption='Quit?')
