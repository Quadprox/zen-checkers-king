import os
import arcade
import app.settings as settings


def __load_texture(texture_filename: str, texture_mirrored: bool = False):
    texture_path = os.path.join(settings.PROJECT_IMAGES_DIR, texture_filename)
    texture = arcade.load_texture(file_name=texture_path,
                                  mirrored=texture_mirrored,
                                  scale=1)
    return texture


def render(texture_filename: str, texture_coord_x: int, texture_coord_y: int, texture_mirrored: bool = False):
    texture_object = __load_texture(texture_filename=texture_filename, texture_mirrored=texture_mirrored)
    arcade.draw_texture_rectangle(
        center_x=texture_coord_x,
        center_y=texture_coord_y,
        texture=texture_object,
        width=texture_object.width,
        height=texture_object.height,
    )
