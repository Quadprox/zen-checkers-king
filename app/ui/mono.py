from app.ui.elements import panel, clockface, button
from app.ui import setup, mapping
from tools import console


class UI:
    def __init__(self):
        self.__mode = 0
        self.__prev = 0
        self.clockface = clockface.Clockface()
        self.collection = {0: setup.build_main_menu(),                      # Main menu
                           1: setup.build_settings_menu(),                  # Settings menu
                           2: setup.build_active_game(),                    # Active game UI
                           3: setup.build_paused_game(),                    # Paused game UI
                           4: setup.build_start_new_confirmation(),         # Start new confirmation menu
                           5: setup.build_end_current_confirmation(),       # End current confirmation menu
                           6: setup.build_game_won(),                       # Game statistics UI (game won)
                           7: setup.build_game_lost(),                      # Game statistics UI (game lost)
                           8: setup.build_quit_confirmation(),              # App quit confirmation menu
                           9: setup.build_game_draw(),                      # Game statistics UI (game draw)
                           }

        self.__show_clockface = False

        console.echo(
            message='Initialized UI',
            level=1)
        for preset in self.collection:
            preset_name = mapping.PRESET_NAMES[preset]
            for ui_element in self.collection[preset]:
                console.echo(
                    message='Created {object} {position} {collection}'.format(
                        object=ui_element,
                        position=f'at {ui_element.position}' if isinstance(ui_element, button.Button) else '',
                        collection=f'at {preset_name}'),
                    level=2)

    def reset_clockface(self):
        self.clockface.stopwatch.reset()

    @property
    def active_mode(self):
        return self.__mode

    @property
    def previous_mode(self):
        return self.__prev

    def set_mode(self, mode: int):
        self.__prev = self.__mode
        self.__mode = mode
        console.echo(
            message='Switching to {mode}...'.format(
                mode=mapping.PRESET_NAMES[mode]),
            level=3)

    def hide_clockface(self):
        self.__show_clockface = False

    def show_clockface(self):
        self.__show_clockface = True

    def display(self):
        panel.display()
        for stored in self.collection[self.__mode]:
            stored.display()
        if self.__show_clockface:
            self.clockface.display()