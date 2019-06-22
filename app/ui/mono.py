from app.ui.elements import panel, button, clockface


class UI:
    def __init__(self):
        self.__mode = 0
        self.clockface = None
        self.collection = {0: [],               # Main menu
                           1: [],               # Settings menu
                           2: [],                   # Active game
                           3: [],                   # Paused game
                           4: [],                       # Start new game confirmation
                           5: [],                       # End current game confirmation
                           6: [],                           # Game won menu
                           7: [],                           # Game lost menu
                           }


    def initialize(self):

        def main_menu():
            pass

        def settings_menu():
            pass

        def active_game():
            pass

        def paused_game():
            pass

        def start_new():
            pass

        def end_current():
            pass

        def game_won():
            pass

        def game_lost():
            pass

        main_menu()
        settings_menu()
        active_game()
        paused_game()
        start_new()
        end_current()
        game_won()
        game_lost()

        self.clockface = clockface.Clockface()

    def reset_clockface(self):
        self.clockface.reset()

    @property
    def active_mode(self):
        return self.__mode

    def set_mode(self, mode: int):
        self.__mode = mode

    def display(self):
        panel.display()
        for stored in self.collection[self.__mode]:
            stored.display()
        self.clockface.display()