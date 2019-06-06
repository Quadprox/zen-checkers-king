import arcade
from app import settings, session


class Shell(arcade.Window):

    def __init__(self):
        super().__init__(
            width=settings.GAME_WINDOW_WIDTH,
            height=settings.GAME_WINDOW_HEIGHT,
            title=settings.GAME_WINDOW_TITLE,
            fullscreen=settings.GAME_WINDOW_FULLSCREEN,
            resizable=settings.GAME_WINDOW_RESIZABLE,
            update_rate=settings.GAME_WINDOW_UPDATE_RATE,
            antialiasing=settings.GAME_WINDOW_ANTIALIASING
        )

    def setup(self):
        pass

    def on_draw(self):
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_mouse_enter(x, y):
        pass

    def on_mouse_leave(x, y):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass

    def update(self, delta_time: float):
        pass
