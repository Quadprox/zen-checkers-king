from app.board import surface, mapping, get


class Board:

    def __init__(self):
        pass

    @staticmethod
    def clear():
        mapping.clear()

    @staticmethod
    def fill():
        mapping.fill()

    @property
    def map_is_cleared(self):
        status = mapping.SURFACE_EMPTY
        return status

    @staticmethod
    def display(render_checkers: bool = True):
        surface.display()
        if render_checkers:
            for row in mapping.SURFACE_GRID:
                for column in mapping.SURFACE_GRID[row]:
                    position = [row, column]
                    tile_contains_checker = False
                    if get.checker_by_position(check_position=position) is not None:
                        tile_contains_checker = True
                    if tile_contains_checker:
                        mapping.SURFACE_GRID[row][column].display()
