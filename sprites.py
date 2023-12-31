# This file just contains a bunch of functions that generate sprites for the game.
# The sprites don't have to be generated by these functions, they can be made by hand or any other way.

from PIL import Image, ImageDraw
import shapes

DEFAULT_TILE_HEIGHT = 2000
DEFAULT_TILE_WIDTH = 2000

DEFAULT_ROAD_THICKNESS = 0.25 * DEFAULT_TILE_HEIGHT
DEFAULT_FILLET_RADIUS = 0.5 * DEFAULT_ROAD_THICKNESS

DEFAULT_ROAD_COLOUR = (255, 255, 255)
DEFAULT_BACKGROUND_COLOUR = (40, 40, 50)



def generate_straight(rotation=0, tile_size=(DEFAULT_TILE_WIDTH, DEFAULT_TILE_HEIGHT), road_thickness=DEFAULT_ROAD_THICKNESS, road_colour=DEFAULT_ROAD_COLOUR, background_colour=DEFAULT_BACKGROUND_COLOUR):
    image = Image.new('RGB', tile_size, background_colour)
    draw = ImageDraw.Draw(image)
    tile_width = tile_size[0]
    tile_height = tile_size[1]
    draw.rectangle([(0, (tile_height - road_thickness) / 2), (tile_width, (tile_height + road_thickness) / 2)], fill=road_colour)
    return image.rotate(rotation, expand=True)

def generate_4_way_intersection(fillet_radii=DEFAULT_FILLET_RADIUS, tile_size=(DEFAULT_TILE_WIDTH, DEFAULT_TILE_HEIGHT), road_thickness=DEFAULT_ROAD_THICKNESS, road_colour=DEFAULT_ROAD_COLOUR, background_colour=DEFAULT_BACKGROUND_COLOUR):
    image = Image.new('RGB', tile_size, background_colour)
    draw = ImageDraw.Draw(image)
    tile_width = tile_size[0]
    tile_height = tile_size[1]
    draw.rectangle([(0, (tile_height - road_thickness) / 2), (tile_width, (tile_height + road_thickness) / 2)], fill=road_colour)
    draw.rectangle([((tile_width - road_thickness) / 2, 0), ((tile_width + road_thickness) / 2, tile_height)], fill=road_colour)

    rect = shapes.get_rectangle_opposing_corners((tile_width / 2, tile_height / 2), road_thickness + 2*fillet_radii , road_thickness + 2*fillet_radii)
    draw.rectangle(rect, fill=road_colour)

    rect_corners = shapes.get_rectangle_corners((tile_width / 2, tile_height / 2), road_thickness + 2*fillet_radii , road_thickness + 2*fillet_radii)
    for corner in rect_corners:
        draw.ellipse(shapes.get_rectangle_opposing_corners(corner, 2*fillet_radii-2, 2*fillet_radii-2), fill=background_colour)

    return image

def generate_3_way_intersection(rotation=0, fillet_radii=DEFAULT_FILLET_RADIUS, tile_size=(DEFAULT_TILE_WIDTH, DEFAULT_TILE_HEIGHT), road_thickness=DEFAULT_ROAD_THICKNESS, road_colour=DEFAULT_ROAD_COLOUR, background_colour=DEFAULT_BACKGROUND_COLOUR):
    image = generate_4_way_intersection(fillet_radii, tile_size, road_thickness, road_colour, background_colour)
    draw = ImageDraw.Draw(image)
    tile_width = tile_size[0]
    tile_height = tile_size[1]
    draw.rectangle([(0, 0), (tile_width - road_thickness) / 2, tile_height + road_thickness], fill=background_colour)
    return image.rotate(rotation, expand=True)

def generate_right_turn(rotation=0, fillet_radii=DEFAULT_FILLET_RADIUS, tile_size=(DEFAULT_TILE_WIDTH, DEFAULT_TILE_HEIGHT), road_thickness=DEFAULT_ROAD_THICKNESS, road_colour=DEFAULT_ROAD_COLOUR, background_colour=DEFAULT_BACKGROUND_COLOUR):
    image = Image.new('RGB', tile_size, background_colour)
    draw = ImageDraw.Draw(image)
    tile_width = tile_size[0]
    tile_height = tile_size[1]
    rect1 = [
        (tile_width / 2 - road_thickness / 2, tile_height / 2 + road_thickness / 2),
        (tile_width / 2 + road_thickness / 2, tile_height)
    ]
    draw.rectangle(rect1, fill=road_colour)

    rect2 = shapes.rotate_coords(rect1, (tile_width / 2, tile_height / 2), -90)
    if rect2[0][0] > rect2[1][0]:
        rect2 = [rect2[1], rect2[0]]
    if rect2[0][1] > rect2[1][1]:
        # swap y coords
        rect2 = [(rect2[0][0], rect2[1][1]), (rect2[1][0], rect2[0][1])]
    draw.rectangle(rect2, fill=road_colour)

    # circ = shapes.get_circle_opposing_corners((tile_width / 2 + road_thickness / 2, tile_height / 2 + road_thickness / 2), road_thickness)
    # draw.ellipse(circ, fill=road_colour)

    draw.pieslice(shapes.get_circle_opposing_corners((tile_width / 2 + road_thickness / 2, tile_height / 2 + road_thickness / 2), road_thickness), 180, 270, fill=road_colour)

    fillet_rect = shapes.get_rectangle_opposing_corners((tile_width / 2 + road_thickness / 2, tile_height / 2 + road_thickness / 2), 2*fillet_radii, 2*fillet_radii)
    draw.rectangle(fillet_rect, fill=road_colour)

    fillet_circ = shapes.get_circle_opposing_corners((tile_width / 2 + road_thickness / 2 + fillet_radii, tile_height / 2 + road_thickness / 2 + fillet_radii), fillet_radii - 1)
    draw.ellipse(fillet_circ, fill=background_colour)

    return image.rotate(rotation, expand=True)

def generate_left_turn(rotation=0, fillet_radii=DEFAULT_FILLET_RADIUS, tile_size=(DEFAULT_TILE_WIDTH, DEFAULT_TILE_HEIGHT), road_thickness=DEFAULT_ROAD_THICKNESS, road_colour=DEFAULT_ROAD_COLOUR, background_colour=DEFAULT_BACKGROUND_COLOUR):
    image = generate_right_turn(rotation, fillet_radii, tile_size, road_thickness, road_colour, background_colour)
    # flip image
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return image

def generate_empty(tile_size=(DEFAULT_TILE_WIDTH, DEFAULT_TILE_HEIGHT), road_thickness=DEFAULT_ROAD_THICKNESS, road_colour=DEFAULT_ROAD_COLOUR, background_colour=DEFAULT_BACKGROUND_COLOUR):
    image = Image.new('RGB', tile_size, background_colour)
    return image

def generat_dead_end(rotation=0, fillet_radii=DEFAULT_FILLET_RADIUS, tile_size=(DEFAULT_TILE_WIDTH, DEFAULT_TILE_HEIGHT), road_thickness=DEFAULT_ROAD_THICKNESS, road_colour=DEFAULT_ROAD_COLOUR, background_colour=DEFAULT_BACKGROUND_COLOUR):
    image = Image.new('RGB', tile_size, background_colour)
    draw = ImageDraw.Draw(image)
    tile_width = tile_size[0]
    tile_height = tile_size[1]
    rect = [((tile_width - road_thickness) / 2, tile_height), ((tile_width + road_thickness) / 2, (tile_height) / 2)]
    if rect[0][0] > rect[1][0]:
        rect = [rect[1], rect[0]]
    if rect[0][1] > rect[1][1]:
        # swap y coords
        rect = [(rect[0][0], rect[1][1]), (rect[1][0], rect[0][1])]
    # add one pixel to second coord to include corner in rectangle
    rect[1] = (rect[1][0], rect[1][1])
    print(rect)
    rect = shapes.symmetrically_round(rect)
    print(rect)
    draw.rectangle(rect, fill=road_colour)

    circ = shapes.get_circle_opposing_corners((tile_width / 2, tile_height / 2), road_thickness / 2)
    draw.ellipse(circ, fill=road_colour)

    return image.rotate(rotation, expand=True)

if __name__ == '__main__':
    print("Saving images...")
    # generate_straight(rotation=0).save('sprites/straight.png')
    # generate_4_way_intersection().save('sprites/cross_intersection.png')
    # generate_right_turn(rotation=0).save('sprites/right_turn.png')
    # generate_left_turn(rotation=0).save('sprites/left_turn.png')
    # generate_3_way_intersection(rotation=0).save('sprites/t_intersection.png')
    # generate_empty().save('sprites/empty.png')
    generat_dead_end().save('sprites/dead_end.png')
    print("Done.")
