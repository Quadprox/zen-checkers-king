import arcade


def rectangle_solid(rect_coord_x: int, rect_coord_y: int, rect_width: int, rect_height: int,
                    rect_color: list, rect_tilt: bool = False):
    arcade.draw_rectangle_filled(
        center_x=rect_coord_x,
        center_y=rect_coord_y,
        width=rect_width,
        height=rect_height,
        color=rect_color,
        tilt_angle=12 if rect_tilt else 0
    )


def rectangle_outline(rect_coord_x: int, rect_coord_y: int, rect_width: int, rect_height: int,
                      rect_border_color: list, rect_border_width: int, rect_tilt: bool = False):
    arcade.draw_rectangle_outline(
        center_x=rect_coord_x,
        center_y=rect_coord_y,
        width=rect_width,
        height=rect_height,
        color=rect_border_color,
        border_width=rect_border_width,
        tilt_angle=12 if rect_tilt else 0
    )


def square_solid(sq_coord_x: int, sq_coord_y: int, sq_side_len: int,
                 sq_color: list, sq_tilt: bool = False):
    rectangle_solid(
        rect_coord_x=sq_coord_x,
        rect_coord_y=sq_coord_y,
        rect_width=sq_side_len,
        rect_height=sq_side_len,
        rect_color=sq_color,
        rect_tilt=sq_tilt
    )


def square_outline(sq_coord_x: int, sq_coord_y: int, sq_side_len: int,
                   sq_border_color: list, sq_border_width: int, sq_tilt: bool = False):
    rectangle_outline(
        rect_coord_x=sq_coord_x,
        rect_coord_y=sq_coord_y,
        rect_width=sq_side_len,
        rect_height=sq_side_len,
        rect_border_color=sq_border_color,
        rect_border_width=sq_border_width,
        rect_tilt=sq_tilt
    )


def circle_solid(circle_coord_x: int, circle_coord_y: int, circle_radius: int,
                 circle_color: list, circle_segments: int):
    arcade.draw_circle_filled(
        center_x=circle_coord_x,
        center_y=circle_coord_y,
        radius=circle_radius,
        color=circle_color,
        num_segments=circle_segments
    )


def circle_outline(circle_coord_x: int, circle_coord_y: int, circle_radius: int,
                   circle_border_color: list, circle_border_width: int, circle_segments: int):
    arcade.draw_circle_outline(
        center_x=circle_coord_x,
        center_y=circle_coord_y,
        radius=circle_radius,
        color=circle_border_color,
        border_width=circle_border_width,
        num_segments=circle_segments
    )


def character(char_string: str, char_coord_x: int, char_coord_y: int, char_color: list,
              char_font_size: int, char_font_name: str, char_rotation_angle: int,
              char_font_bold: bool = False, char_font_italic: bool = False,
              char_anchor: bool = True):
    arcade.draw_text(
        text=char_string,
        start_x=char_coord_x,
        start_y=char_coord_y,
        color=char_color,
        font_size=char_font_size,
        font_name=char_font_name,
        bold=char_font_bold,
        italic=char_font_italic,
        anchor_x='center' if char_anchor else 'left',
        anchor_y='center' if char_anchor else 'left',
        rotation=char_rotation_angle
    )


def line(line_start_x: int, line_start_y: int, line_end_x: int, line_end_y: int,
         line_color: list, line_width: int):
    arcade.draw_line(
        start_x=line_start_x,
        start_y=line_start_y,
        end_x=line_end_x,
        end_y=line_end_y,
        color=line_color,
        line_width=line_width
    )
