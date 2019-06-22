import app.board.convert as convert
from app.checker import surface, behavior


class Checker:

    ID = 0

    @classmethod
    def __update_id(cls):
        cls.ID += 1

    def __init__(self, init_position: list, init_color: str, init_type_queen: bool = False):

        # Public attributes:
        self.position = init_position       # List type collection, eg. [1, 2]
        self.color = init_color             # White / Black
        self.queen = init_type_queen        # True / False (default)
        self.dev = False                    # True, if force-spawn / False (default)

        # Protected private attributes:
        self.__move_list = []               # Contains board positions current checker can move to
        self.__kill_list = []               # Contains board positions current checker must move to

        # Initialisation methods and setups:
        self.__update_id()                  # Updates checker class object's ID value (unique)

    def __str__(self):
        checker_information = '{color} {checker}'.format(
            color=self.color,
            checker="checker (queen)" if self.queen else "checker",
        )
        return checker_information

    @property
    def coordinates(self):
        coordinates = convert.board_position_to_coordinates(conv_position=self.position)
        return coordinates

    @property
    def index(self):
        alphanumeric_index = convert.board_position_to_alphanumeric_index(conv_position=self.position)
        return alphanumeric_index

    @property
    def can_promote(self):
        status = False
        color = self.color.lower()
        row = self.position[0]
        if color == 'white' and row == 8 or color == 'black' and row == 1:
            status = True
        return status

    @property
    def can_move(self):
        status = False
        if len(self.__move_list) > 0:
            status = True
        return status

    @property
    def can_kill(self):
        status = False
        if len(self.__kill_list) > 0:
            status = True
        return status

    @property
    def move_list(self):
        return self.__move_list

    @property
    def kill_list(self):
        return self.__kill_list

    def set_color(self, new_color: str):
        self.color = new_color

    def set_position(self, new_position: str):
        self.position = new_position

    def promote(self):
        if not self.queen:
            self.queen = True

    def move(self, position):
        behavior.move(checker_object=self, new_position=position)

    def update(self):
        if self.can_promote and not self.dev:
            self.promote()

        updated_move_list = behavior.get_move_list(checker_object=self)
        if updated_move_list is not None:
            self.__move_list = updated_move_list[0]         # Move list
            self.__kill_list = updated_move_list[1]         # Attack list

    def display(self):
        coordinates = self.coordinates
        coordinate_x, coordinate_y = coordinates
        surface.display(
            coord_x=coordinate_x,
            coord_y=coordinate_y,
            color=self.color,
            queen=self.queen
        )
