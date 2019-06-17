import tools.pencil.draw as draw
from app import settings, session


def board_tile(tile_coord_x: int, tile_coord_y: int, tile_color: str):
    draw.square_solid(
        sq_coord_x=tile_coord_x,
        sq_coord_y=tile_coord_y,
        sq_side_len=settings.TILE_SIDE_LEN,
        sq_color=settings.TILE_COLOR_WHITE if tile_color.lower() == 'white' else
                 settings.TILE_COLOR_BLACK if tile_color.lower() == 'black' else
                 settings.ERROR_COLOR_MAIN,
        sq_tilt=False
    )


def board_highlighted_tile(tile_coord_x: int, tile_coord_y: int, tile_highlight_type: str):
    draw.square_outline(
        sq_coord_x=tile_coord_x,
        sq_coord_y=tile_coord_y,
        sq_side_len=settings.TILE_HIGHLIGHT_SIDE_LEN,
        sq_border_width=settings.TILE_HIGHLIGHT_BORDER_SIDE_LEN,
        sq_border_color=settings.TILE_HIGHLIGHT_COLOR_MOVE if tile_highlight_type.lower() == 'move' else
                        settings.TILE_HIGHLIGHT_COLOR_ATTACK if tile_highlight_type.lower() == 'kill' else
                        settings.ERROR_COLOR_ALT,
        sq_tilt=False
    )


def board_tile_highlight_move(tile_coord_x: int, tile_coord_y: int):
    draw.square_outline(
        sq_coord_x=tile_coord_x,
        sq_coord_y=tile_coord_y,
        sq_side_len=settings.TILE_HIGHLIGHT_SIDE_LEN,
        sq_border_width=settings.TILE_HIGHLIGHT_BORDER_SIDE_LEN,
        sq_border_color=settings.TILE_HIGHLIGHT_COLOR_MOVE,
        sq_tilt=False
    )


def board_tile_highlight_attack(tile_coord_x: int, tile_coord_y: int):
    draw.square_outline(
        sq_coord_x=tile_coord_x,
        sq_coord_y=tile_coord_y,
        sq_side_len=settings.TILE_HIGHLIGHT_SIDE_LEN,
        sq_border_width=settings.TILE_HIGHLIGHT_BORDER_SIDE_LEN,
        sq_border_color=settings.TILE_HIGHLIGHT_COLOR_ATTACK,
        sq_tilt=False
    )


def __checker_complex_queen_index(ch_coord_x: int, ch_coord_y: int, ch_color: str):
    draw.character(
        char_string='Q',
        char_coord_x=ch_coord_x,
        char_coord_y=ch_coord_y + 2,
        char_color=settings.CHECKER_COLOR_WHITE_ALT if ch_color.lower() == 'white' else
                   settings.CHECKER_COLOR_BLACK_ALT if ch_color.lower() == 'black' else
                   settings.ERROR_COLOR_ALT,
        char_font_size=round(settings.CHECKER_QUEEN_INDEX_FONT_SIZE * 2.2, 0),
        char_font_name=settings.CHECKER_QUEEN_INDEX_FONT_NAME,
        char_font_bold=False,
        char_font_italic=False,
        char_anchor=True,
        char_rotation_angle=0
    )


def __checker_simple_queen_index(ch_coord_x: int, ch_coord_y: int, ch_color: str):
    draw.line(
        line_start_x=int(ch_coord_x - settings.CHECKER_RADIUS_OUTER) + 5,
        line_start_y=ch_coord_y - 15,
        line_end_x=int(ch_coord_x + settings.CHECKER_RADIUS_OUTER) - 5,
        line_end_y=ch_coord_y + 15,
        line_color=settings.CHECKER_COLOR_WHITE_MAIN if ch_color.lower() == 'white' else
                   settings.CHECKER_COLOR_BLACK_MAIN if ch_color.lower() == 'black' else
                   settings.ERROR_COLOR_MAIN,
        line_width=settings.CHECKER_QUEEN_LINE_WIDTH
    )


def __checker_simple(ch_coord_x: int, ch_coord_y: int, ch_color: str, ch_queen: bool = False):

    def render_outline():
        draw.circle_outline(
            circle_coord_x=ch_coord_x,
            circle_coord_y=ch_coord_y,
            circle_radius=settings.CHECKER_RADIUS_OUTER,
            circle_border_color=settings.CHECKER_COLOR_WHITE_MAIN if ch_color.lower() == 'white' else
                                settings.CHECKER_COLOR_BLACK_MAIN if ch_color.lower() == 'black' else
                                settings.ERROR_COLOR_MAIN,
            circle_border_width=settings.CHECKER_SIMPLE_BORDER_LEN,
            circle_segments=settings.CHECKER_SEGMENTS
        )

    def render_queen_index():
        __checker_simple_queen_index(ch_coord_x, ch_coord_y, ch_color)

    render_outline()
    if ch_queen:
        render_queen_index()


def __checker_complex(ch_coord_x: int, ch_coord_y: int, ch_color: str, ch_queen: bool = False):

    def render_outer_radius():
        draw.circle_solid(
            circle_coord_x=ch_coord_x + settings.CHECKER_SHADOW_SHIFT_X,
            circle_coord_y=ch_coord_y + settings.CHECKER_SHADOW_SHIFT_Y,
            circle_radius=settings.CHECKER_RADIUS_OUTER,
            circle_color=settings.CHECKER_COLOR_WHITE_ALT if ch_color.lower() == 'white' else
                         settings.CHECKER_COLOR_BLACK_ALT if ch_color.lower() == 'black' else
                         settings.ERROR_COLOR_ALT,
            circle_segments=settings.CHECKER_SEGMENTS
        )
        draw.circle_solid(
            circle_coord_x=ch_coord_x - settings.CHECKER_SHADOW_SHIFT_X,
            circle_coord_y=ch_coord_y - settings.CHECKER_SHADOW_SHIFT_Y,
            circle_radius=settings.CHECKER_RADIUS_OUTER,
            circle_color=settings.CHECKER_COLOR_WHITE_MAIN if ch_color.lower() == 'white' else
                         settings.CHECKER_COLOR_BLACK_MAIN if ch_color.lower() == 'black' else
                         settings.ERROR_COLOR_MAIN,
            circle_segments=settings.CHECKER_SEGMENTS
        )

    def render_outer_inner():
        draw.circle_solid(
            circle_coord_x=ch_coord_x - settings.CHECKER_SHADOW_SHIFT_X,
            circle_coord_y=ch_coord_y - settings.CHECKER_SHADOW_SHIFT_Y,
            circle_radius=settings.CHECKER_RADIUS_INNER,
            circle_color=settings.CHECKER_COLOR_WHITE_ALT if ch_color.lower() == 'white' else
                         settings.CHECKER_COLOR_BLACK_ALT if ch_color.lower() == 'black' else
                         settings.ERROR_COLOR_ALT,
            circle_segments=settings.CHECKER_SEGMENTS
        )
        draw.circle_solid(
            circle_coord_x=ch_coord_x + settings.CHECKER_SHADOW_SHIFT_X,
            circle_coord_y=ch_coord_y + settings.CHECKER_SHADOW_SHIFT_Y,
            circle_radius=settings.CHECKER_RADIUS_INNER,
            circle_color=settings.CHECKER_COLOR_WHITE_MAIN if ch_color.lower() == 'white' else
                         settings.CHECKER_COLOR_BLACK_MAIN if ch_color.lower() == 'black' else
                         settings.ERROR_COLOR_MAIN,
            circle_segments=settings.CHECKER_SEGMENTS
        )

    def render_queen_index():
        __checker_complex_queen_index(ch_coord_x, ch_coord_y, ch_color)

    render_outer_radius()
    render_outer_inner()
    if ch_queen:
        render_queen_index()


def checker(ch_coord_x: int, ch_coord_y: int, ch_color: str, ch_queen: bool = False):
    style = session.RENDER_MODE_CHECKER
    render_checker = {
        0: lambda: __checker_simple(ch_coord_x, ch_coord_y, ch_color, ch_queen),
        1: lambda: __checker_complex(ch_coord_x, ch_coord_y, ch_color, ch_queen)
    }
    render_checker[style]()


def __button_large(b_coord_x: int, b_coord_y: int, b_caption: str, b_filled: bool = False):
    if b_filled:
        draw.rectangle_solid(
            rect_coord_x=b_coord_x,
            rect_coord_y=b_coord_y,
            rect_width=settings.BUTTON_LARGE_WIDTH,
            rect_height=settings.BUTTON_LARGE_HEIGHT,
            rect_color=settings.BUTTON_FILLED_COLOR,
            rect_tilt=False
        )
    draw.rectangle_outline(
        rect_coord_x=b_coord_x,
        rect_coord_y=b_coord_y,
        rect_width=settings.BUTTON_LARGE_WIDTH,
        rect_height=settings.BUTTON_LARGE_HEIGHT,
        rect_border_color=settings.BUTTON_BORDER_COLOR,
        rect_border_width=settings.BUTTON_BORDER_LEN,
        rect_tilt=False
    )
    draw.character(
        char_string=b_caption,
        char_coord_x=b_coord_x,
        char_coord_y=b_coord_y,
        char_color=settings.BUTTON_CAPTION_COLOR,
        char_font_size=settings.BUTTON_CAPTION_FONT_SIZE,
        char_font_name=settings.BUTTON_CAPTION_FONT_NAME,
        char_rotation_angle=12 if b_filled else 0,
        char_font_bold=settings.BUTTON_CAPTION_STYLE_BOLD,
        char_font_italic=settings.BUTTON_CAPTION_STYLE_ITALIC,
        char_anchor=True
    )


def __button_small(b_coord_x: int, b_coord_y: int, b_caption: str, b_filled: bool = False):
    if b_filled:
        draw.rectangle_solid(
            rect_coord_x=b_coord_x,
            rect_coord_y=b_coord_y,
            rect_width=settings.BUTTON_SMALL_WIDTH,
            rect_height=settings.BUTTON_SMALL_HEIGHT,
            rect_color=settings.BUTTON_FILLED_COLOR,
            rect_tilt=False
        )
    draw.rectangle_outline(
        rect_coord_x=b_coord_x,
        rect_coord_y=b_coord_y,
        rect_width=settings.BUTTON_SMALL_WIDTH,
        rect_height=settings.BUTTON_SMALL_HEIGHT,
        rect_border_color=settings.BUTTON_BORDER_COLOR,
        rect_border_width=settings.BUTTON_BORDER_LEN,
        rect_tilt=False
    )
    draw.character(
        char_string=b_caption,
        char_coord_x=b_coord_x,
        char_coord_y=b_coord_y,
        char_color=settings.BUTTON_CAPTION_COLOR,
        char_font_size=settings.BUTTON_CAPTION_FONT_SIZE,
        char_font_name=settings.BUTTON_CAPTION_FONT_NAME,
        char_rotation_angle=12 if b_filled else 0,
        char_font_bold=settings.BUTTON_CAPTION_STYLE_BOLD,
        char_font_italic=settings.BUTTON_CAPTION_STYLE_ITALIC,
        char_anchor=True
    )


def button(b_coord_x: int, b_coord_y: int, b_size: str, b_caption: str, b_filled: bool = False):
    size = b_size.lower()
    render_button = {
        'large': lambda: __button_large(b_coord_x, b_coord_y, b_caption, b_filled),
        'small': lambda: __button_small(b_coord_x, b_coord_y, b_caption, b_filled),
    }
    render_button[size]()