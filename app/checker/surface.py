import app.session as session
from tools.pencil import texture, stamp


def __render_opengl(coord_x: int, coord_y: int, color: str, queen: bool = False):
    stamp.checker(
        ch_coord_x=coord_x,
        ch_coord_y=coord_y,
        ch_color=color,
        ch_queen=queen,
    )


def __render_texture(coord_x: int, coord_y: int, color: str, queen: bool = False):
    texture.render(
        texture_filename='checker_{color}{type}.png'.format(color=color.lower(),
                                                            type='_queen' if queen else ''),
        texture_coord_x=coord_x,
        texture_coord_y=coord_y,
    )


def display(coord_x: int, coord_y: int, color: str, queen: bool = False):
    mode = session.RENDER_MODE_GLOBAL
    render = {
        0: lambda: __render_opengl(coord_x, coord_y, color, queen),
        1: lambda: __render_texture(coord_x, coord_y, color, queen),
    }
    render[mode]()
