from app.board import surface, mapping
from tools import console


class Board:

    def __init__(self):
        pass

    @staticmethod
    def clear():
        console.echo(
            message='Cleared board surface',
            level=1)
        mapping.clear()

    @staticmethod
    def fill():
        console.echo(
            message='Filling board surface with checker objects...',
            level=1)
        mapping.fill()

    @staticmethod
    def update():
        for row in mapping.SURFACE_GRID:
            for column in mapping.SURFACE_GRID[row]:
                if mapping.SURFACE_GRID[row][column] is not None:
                    checker = mapping.SURFACE_GRID[row][column]
                    checker.update()

    @property
    def map_is_cleared(self):
        status = mapping.SURFACE_EMPTY
        return status

    @staticmethod
    def display():
        surface.display()

    @staticmethod
    def display_checkers():
        for row in mapping.SURFACE_GRID:
            for column in mapping.SURFACE_GRID[row]:
                if mapping.SURFACE_GRID[row][column] is not None:
                    mapping.SURFACE_GRID[row][column].display()