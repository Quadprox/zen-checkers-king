from app.ui.elements import button


def build_main_menu():
    collection = [button.StartButton(init_position=[1, 0]),
                  button.SettingsButton(init_position=[2, 0]),
                  button.QuitButton(init_position=[5, 0])]
    return collection


def build_settings_menu():
    collection = [button.BackButton(init_position=[5, 0])]
    return collection


def build_active_game():
    collection = [button.PauseButton(init_position=[4, 0]),
                  button.HintButton(init_position=[5, 1]),
                  button.UndoButton(init_position=[5, 2])]
    return collection


def build_paused_game():
    collection = [button.ResumeButton(init_position=[1, 0]),
                  button.RestartButton(init_position=[2, 0]),
                  button.SettingsButton(init_position=[3, 0]),
                  button.MainMenuButton(init_position=[4, 0]),
                  button.QuitButton(init_position=[5, 0])]
    return collection


def build_start_new_confirmation():
    collection = [button.YesButton(init_position=[1, 1]),
                  button.NoButton(init_position=[1, 2])]
    return collection


def build_end_current_confirmation():
    collection = [button.YesButton(init_position=[1, 1]),
                  button.NoButton(init_position=[1, 2])]
    return collection


def build_game_won():
    collection = [button.MainMenuButton(init_position=[4, 0]),
                  button.QuitButton(init_position=[5, 0])]
    return collection


def build_game_lost():
    collection = [button.MainMenuButton(init_position=[4, 0]),
                  button.QuitButton(init_position=[5, 0])]
    return collection
