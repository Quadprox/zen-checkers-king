from app.ui.elements import panel, button, clockface
from tools.clock import stopwatch


class UI:
    def __init__(self):
        self.__mode = 0
        self.collection = {0: [],       # Main menu
                           1: [],       # Settings menu
                           2: [],       # Active game
                           3: [],       # Paused game
                           4: [],       # Start new game confirmation
                           5: [],       # End current game confirmation
                           6: [],       # Game won menu
                           7: [],       # Game lost menu
                           }
        self.time = None

    def initialize(self):

        def main_menu():
            pass

        def settings_menu():
            pass

        def active_game():
            b_start = button.StartButton(init_position=[1, 0])
            b_start.set_size('large')
            self.collection[2].append(b_start)
            b_start = button.StartButton(init_position=[2, 0])
            b_start.set_size('large')
            self.collection[2].append(b_start)
            b_start = button.StartButton(init_position=[3, 0])
            b_start.set_size('large')
            self.collection[2].append(b_start)
            b_start = button.StartButton(init_position=[4, 0])
            b_start.set_size('large')
            self.collection[2].append(b_start)
            b_start = button.StartButton(init_position=[5, 0])
            b_start.set_size('large')
            self.collection[2].append(b_start)

            cface = clockface.Clockface()
            cface.insert(stopwatch.Stopwatch())
            cface.stopwatch.start()
            self.collection[2].append(cface)



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

    def reset_collection(self):
        self.collection = {}
        for collection_id in range(0, 7 + 1):
            self.collection[collection_id] = []
        self.initialize()

    @property
    def active_mode(self):
        return self.__mode

    def set_mode(self, mode: int):
        self.__mode = mode

    def display(self):
        panel.display()
        for stored in self.collection[self.__mode]:
            stored.display()