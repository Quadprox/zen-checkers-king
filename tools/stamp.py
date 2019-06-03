import tools.pencil as draw
from app import settings


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
                        settings.TILE_HIGHLIGHT_COLOR_KILL if tile_highlight_type.lower() == 'kill' else
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
        sq_border_color=settings.TILE_HIGHLIGHT_COLOR_KILL,
        sq_tilt=False
    )
