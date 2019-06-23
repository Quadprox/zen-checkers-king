from app import session, settings
from tools.pencil import draw


def __render_opengl():
    draw.rectangle_solid(
        rect_coord_x=settings.UI_PANEL_POSITION_X,
        rect_coord_y=settings.UI_PANEL_POSITION_Y,
        rect_width=settings.UI_PANEL_WIDTH,
        rect_height=settings.UI_PANEL_HEIGHT,
        rect_color=settings.UI_PANEL_BACKGROUND_COLOR,
        rect_tilt=False
    )


def __render_texture():
    pass


def display():
    # mode = session.RENDER_MODE_GLOBAL
    render = {
        0: lambda: __render_opengl(),
        1: lambda: __render_texture(),
    }
    # render[mode]()
    render[0]()