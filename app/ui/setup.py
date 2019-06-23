from app.ui.elements import button, divider, text


def build_main_menu():
    collection = [
        text.Logo(),
        divider.ClockfaceDivider(),
        text.MainMenu(),
        button.StartButton(init_position=[1, 0]),
        button.SettingsButton(init_position=[2, 0]),
        button.QuitButton(init_position=[5, 0]),
        text.AppInformation(),
    ]
    return collection


def build_settings_menu():
    collection = [
        text.Logo(),
        divider.ClockfaceDivider(),
        text.SettingsMenu(),
        button.BackButton(init_position=[5, 0]),
        text.AppInformation(),
    ]
    return collection


def build_active_game():
    collection = [
        divider.ClockfaceDivider(),
        divider.LowerDivider(),
        text.TurnHistoryCaption(),
        button.PauseButton(init_position=[4, 0]),
        button.HintButton(init_position=[5, 1]),
        button.UndoButton(init_position=[5, 2]),
        text.AppInformation(),
    ]
    return collection


def build_paused_game():
    collection = [
        text.Logo(),
        divider.ClockfaceDivider(),
        text.PauseMenu(),
        button.ResumeButton(init_position=[1, 0]),
        button.RestartButton(init_position=[2, 0]),
        button.SettingsButton(init_position=[3, 0]),
        button.MainMenuButton(init_position=[4, 0]),
        button.QuitButton(init_position=[5, 0]),
        text.AppInformation(),
    ]
    return collection


def build_start_new_confirmation():
    collection = [
        text.Logo(),
        divider.ClockfaceDivider(),
        text.StartNewMenu(),
        button.YesButton(init_position=[1, 1]),
        button.NoButton(init_position=[1, 2]),
        text.AppInformation(),
    ]
    return collection


def build_end_current_confirmation():
    collection = [
        text.Logo(),
        divider.ClockfaceDivider(),
        text.EndCurrentMenu(),
        button.YesButton(init_position=[1, 1]),
        button.NoButton(init_position=[1, 2]),
        text.AppInformation(),
    ]
    return collection


def build_game_won():
    collection = [
        text.Logo(),
        divider.ClockfaceDivider(),
        text.GameWonMenu(),
        button.ContinueButton(init_position=[4, 0]),
        button.QuitButton(init_position=[5, 0]),
        text.AppInformation(),
    ]
    return collection


def build_game_lost():
    collection = [
        text.Logo(),
        divider.ClockfaceDivider(),
        text.GameLostMenu(),
        button.ContinueButton(init_position=[4, 0]),
        button.QuitButton(init_position=[5, 0]),
        text.AppInformation(),
    ]
    return collection


def build_quit_confirmation():
    collection = [
        text.Logo(),
        divider.ClockfaceDivider(),
        text.QuitMenu(),
        button.YesButton(init_position=[1, 1]),
        button.NoButton(init_position=[1, 2]),
        text.AppInformation(),
    ]
    return collection

def build_game_draw():
    collection = [
        text.Logo(),
        divider.ClockfaceDivider(),
        text.GameDrawMenu(),
        button.ContinueButton(init_position=[4, 0]),
        button.QuitButton(init_position=[5, 0]),
        text.AppInformation(),
    ]
    return collection
