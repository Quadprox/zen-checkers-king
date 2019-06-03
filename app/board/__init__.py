import app.board.mapping as mapping
import app.settings as settings


# Setting up mapping dictionary:
row_count_range = range(1, settings.BOARD_ROW_COUNT + 1)
column_count_range = range(1, settings.BOARD_COLUMN_COUNT + 1)
for row in row_count_range:
    if row not in mapping.SURFACE_GRID.keys():
        mapping.SURFACE_GRID[row] = {}
    for column in column_count_range:
        if column not in mapping.SURFACE_GRID[row].keys():
            mapping.SURFACE_GRID[row][column] = None
mapping.SURFACE_EMPTY = True
