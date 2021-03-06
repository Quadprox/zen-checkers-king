from app import settings


PRESET_NAMES = {
    0: 'Main menu',
    1: 'Settings menu',
    2: 'Active game GUI',
    3: 'Paused menu',
    4: 'Start new game menu',
    5: 'End current game menu',
    6: 'Game results (game won)',
    7: 'Game results (game lost/force restarted)',
    8: 'Quit app confirmation menu',
    9: 'Game results (game draw)',
}


CLOCKFACE_POSITIONS = {
    1: [settings.CLOCKFACE_POSITION_X, settings.CLOCKFACE_POSITION_Y],      # Default position
    2: [0, 0]                                                               # Alternative position
}

MENU_NAME_POSITION = {
    1: [660, 452]
}

APP_INFORMATION = {
    1: [660, 20]
}

TURN_HISTORY_POSITIONS = {
    0: [settings.DIVIDER_POSITION_X, 182],
    1: [],
    2: []
}

DIVIDER_POSITIONS = {
    1: [settings.DIVIDER_POSITION_X, 472],
    2: [settings.DIVIDER_POSITION_X, 192],
    3: []
}

BUTTON_GRID_POSITIONS = {

    # 1 to 5 are positions from top to bottom displayed on the panel surface. The lower the number, the higher the
    # button is situated on the grid. Inner position 0 sets the button object to the center point, 1 and 2 set the
    # object alignment to left or right side accordingly:

    1: {0: [settings.BUTTON_LARGE_POSITION_X_MIDDLE,
            settings.BUTTON_LARGE_HEIGHT * 5 + settings.BUTTON_MARGIN_Y * 5],
        1: [settings.BUTTON_SMALL_POSITION_X_LEFT,
            settings.BUTTON_LARGE_HEIGHT * 5 + settings.BUTTON_MARGIN_Y * 5],
        2: [settings.BUTTON_SMALL_POSITION_X_RIGHT,
            settings.BUTTON_LARGE_HEIGHT * 5 + settings.BUTTON_MARGIN_Y * 5]},

    2: {0: [settings.BUTTON_LARGE_POSITION_X_MIDDLE,
            settings.BUTTON_LARGE_HEIGHT * 4 + settings.BUTTON_MARGIN_Y * 4],
        1: [settings.BUTTON_SMALL_POSITION_X_LEFT,
            settings.BUTTON_LARGE_HEIGHT * 4 + settings.BUTTON_MARGIN_Y * 4],
        2: [settings.BUTTON_SMALL_POSITION_X_RIGHT,
            settings.BUTTON_LARGE_HEIGHT * 4 + settings.BUTTON_MARGIN_Y * 4]},

    3: {0: [settings.BUTTON_LARGE_POSITION_X_MIDDLE,
            settings.BUTTON_LARGE_HEIGHT * 3 + settings.BUTTON_MARGIN_Y * 3],
        1: [settings.BUTTON_SMALL_POSITION_X_LEFT,
            settings.BUTTON_LARGE_HEIGHT * 3 + settings.BUTTON_MARGIN_Y * 3],
        2: [settings.BUTTON_SMALL_POSITION_X_RIGHT,
            settings.BUTTON_LARGE_HEIGHT * 3 + settings.BUTTON_MARGIN_Y * 3]},

    4: {0: [settings.BUTTON_LARGE_POSITION_X_MIDDLE,
            settings.BUTTON_LARGE_HEIGHT * 2 + settings.BUTTON_MARGIN_Y * 2],
        1: [settings.BUTTON_SMALL_POSITION_X_LEFT,
            settings.BUTTON_LARGE_HEIGHT * 2 + settings.BUTTON_MARGIN_Y * 2],
        2: [settings.BUTTON_SMALL_POSITION_X_RIGHT,
            settings.BUTTON_LARGE_HEIGHT * 2 + settings.BUTTON_MARGIN_Y * 2]},

    5: {0: [settings.BUTTON_LARGE_POSITION_X_MIDDLE,
            settings.BUTTON_LARGE_HEIGHT + settings.BUTTON_MARGIN_Y],
        1: [settings.BUTTON_SMALL_POSITION_X_LEFT,
            settings.BUTTON_LARGE_HEIGHT + settings.BUTTON_MARGIN_Y],
        2: [settings.BUTTON_SMALL_POSITION_X_RIGHT,
            settings.BUTTON_LARGE_HEIGHT + settings.BUTTON_MARGIN_Y]},
}
