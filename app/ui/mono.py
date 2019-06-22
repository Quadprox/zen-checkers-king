from app.ui.elements import panel, clockface
from app.ui import setup


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
                           }

        self.__show_clockface = False

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