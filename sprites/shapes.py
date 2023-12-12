# coor

def get_rectangle_opposing_corners(center, width, height):
    return [(center[0] - width / 2, center[1] - height / 2), (center[0] + width / 2, center[1] + height / 2)]

def get_rectangle_corners(center, width, height):
    return [(center[0] - width / 2, center[1] - height / 2), (center[0] + width / 2, center[1] - height / 2), (center[0] + width / 2, center[1] + height / 2), (center[0] - width / 2, center[1] + height / 2)]


def get_circle_opposing_corners(center, radius):
    return [(center[0] - radius, center[1] - radius), (center[0] + radius, center[1] + radius)]


def rotate_coord(coord, center, angle):
    import math
    angle = math.radians(angle)
    x = coord[0] - center[0]
    y = coord[1] - center[1]
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return (new_x + center[0], new_y + center[1])

def rotate_coords(coords, center, angle):
    return [rotate_coord(coord, center, angle) for coord in coords]
