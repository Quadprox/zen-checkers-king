from app import settings


def get_button_boundary_range(button_object):
    coordinate_x, coordinate_y = button_object.coordinates
    boundary_top = int(coordinate_y + settings.BUTTON_SMALL_HEIGHT / 2)
    boundary_bottom = int(coordinate_y - settings.BUTTON_SMALL_HEIGHT / 2)
    boundary_right = int(coordinate_x + settings.BUTTON_SMALL_WIDTH / 2 if button_object.size == 'small' else \
                         coordinate_x + settings.BUTTON_LARGE_WIDTH / 2 if button_object.size == 'large' else 0)
    boundary_left = int(coordinate_x - settings.BUTTON_SMALL_WIDTH / 2 if button_object.size == 'small' else \
                        coordinate_x - settings.BUTTON_LARGE_WIDTH / 2 if button_object.size == 'large' else 0)
    boundaries = [range(boundary_left, boundary_right),
                  range(boundary_bottom, boundary_top)]
    return boundaries

def coordinates_in_button_boundaries(coordinates, button_object):
    coordinate_x, coordinate_y = coordinates
    boundary_x_range, boundary_y_range = get_button_boundary_range(button_object)
    in_boundaries = False
    if coordinate_x in boundary_x_range and coordinate_y in boundary_y_range:
        in_boundaries = True
    return in_boundaries




