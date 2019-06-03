from app import settings, session
from tools import pencil, stamp, texture


def __render_opengl():

    def render_outer_margin():
        pencil.square_solid(
            sq_coord_x=settings.BOARD_POSITION_X,
            sq_coord_y=settings.BOARD_POSITION_Y,
            sq_side_len=settings.BOARD_SIDE_LEN,
            sq_color=settings.BOARD_MARGIN_COLOR_OUTER,
            sq_tilt=False
        )

    def render_inner_margin():
        pencil.square_solid(
            sq_coord_x=settings.BOARD_POSITION_X,
            sq_coord_y=settings.BOARD_POSITION_Y,
            sq_side_len=int(settings.BOARD_SIDE_LEN - settings.BOARD_MARGIN_OUTER_LEN * 2),
            sq_color=settings.BOARD_MARGIN_COLOR_INNER,
            sq_tilt=False
        )

    def render_tiles():
        init_coord_x = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2)
        init_coord_y = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2)
        color = 'White'
        for row in range(1, settings.BOARD_ROW_COUNT + 1):
            for column in range(1, settings.BOARD_COLUMN_COUNT + 1):
                if color == 'Black':
                    stamp.board_tile(
                        tile_coord_x=init_coord_x,
                        tile_coord_y=init_coord_y,
                        tile_color=color
                    )
                init_coord_x += settings.TILE_SIDE_LEN
                color = 'White' if color == 'Black' else 'Black'
            init_coord_x = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2)
            init_coord_y += settings.TILE_SIDE_LEN
            color = 'White' if color == 'Black' else 'Black'

    def render_letter_index():
        for side in ('bottom', 'top'):
            letter_coord_x = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2)
            letter_coord_y = int(settings.BOARD_MARGIN_LEN / 2)
            letter_rotation = 0
            if side == 'top':
                letter_coord_x = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2)
                letter_coord_y = int(settings.BOARD_SIDE_LEN - settings.BOARD_MARGIN_OUTER_LEN / 2)
                letter_rotation = 180
            for letter in settings.BOARD_LETTER_INDEX:
                pencil.character(
                    char_string=letter,
                    char_coord_x=letter_coord_x,
                    char_coord_y=letter_coord_y,
                    char_color=settings.BOARD_MARGIN_COLOR_INNER,
                    char_font_size=settings.BOARD_INDEX_FONT_SIZE,
                    char_font_name=settings.BOARD_INDEX_FONT_NAME,
                    char_rotation_angle=letter_rotation,
                    char_font_bold=settings.BOARD_INDEX_STYLE_BOLD,
                    char_font_italic=settings.BOARD_INDEX_STYLE_ITALIC,
                    char_anchor=True
                )
                letter_coord_x += settings.TILE_SIDE_LEN

    def render_numeric_index():
        for side in ('left', 'right'):
            number_coord_x = int(settings.BOARD_MARGIN_LEN / 2)
            number_coord_y = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2)
            number_rotation = 0
            if side == 'right':
                number_coord_x = int(settings.BOARD_SIDE_LEN - settings.BOARD_MARGIN_OUTER_LEN / 2)
                number_coord_y = int(settings.BOARD_MARGIN_LEN + settings.TILE_SIDE_LEN / 2)
                number_rotation = 180
            for number in settings.BOARD_NUMBER_INDEX:
                pencil.character(
                    char_string=number,
                    char_coord_x=number_coord_x,
                    char_coord_y=number_coord_y,
                    char_color=settings.BOARD_MARGIN_COLOR_INNER,
                    char_font_size=settings.BOARD_INDEX_FONT_SIZE,
                    char_font_name=settings.BOARD_INDEX_FONT_NAME,
                    char_rotation_angle=number_rotation,
                    char_font_bold=settings.BOARD_INDEX_STYLE_BOLD,
                    char_font_italic=settings.BOARD_INDEX_STYLE_ITALIC,
                    char_anchor=True
                )
                number_coord_y += settings.TILE_SIDE_LEN

    render_outer_margin()
    render_inner_margin()
    render_tiles()
    render_letter_index()
    render_numeric_index()


def __render_texture():
    texture.render(
        texture_filename='board_surface.png',
        texture_coord_x=settings.BOARD_POSITION_X,
        texture_coord_y=settings.BOARD_POSITION_Y,
        texture_mirrored=False
    )


def display():
    mode = session.RENDER_MODE_GLOBAL
    render = {
        0: lambda: __render_opengl(),
        1: lambda: __render_texture(),
    }
    render[mode]()
