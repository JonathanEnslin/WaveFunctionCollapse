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

def reposition_corners(rect):
    if rect[0][0] > rect[1][0]:
        rect = [rect[1], rect[0]]
    if rect[0][1] > rect[1][1]:
        # swap y coords
        rect = [(rect[0][0], rect[1][1]), (rect[1][0], rect[0][1])]
    return rect


def symmetrically_round(rect):
    # calculate x midpoint
    x_mid = (rect[0][0] + rect[1][0]) / 2
    # calculate y midpoint
    y_mid = (rect[0][1] + rect[1][1]) / 2

    cnr1 = list(rect[0])
    cnr2 = list(rect[1])

    cnr1_rounding_errors = [abs(round(val) - val) for val in cnr1]
    cnr2_rounding_errors = [abs(round(val) - val) for val in cnr2]

    if cnr1_rounding_errors[0] < cnr2_rounding_errors[0]:
        cnr1[0] = round(cnr1[0])
        # calculate new cnr2 x coord
        cnr2[0] = x_mid + (x_mid - cnr1[0])
    else:
        cnr2[0] = round(cnr2[0])
        # calculate new cnr1 x coord
        cnr1[0] = x_mid + (x_mid - cnr2[0])

    if cnr1_rounding_errors[1] < cnr2_rounding_errors[1]:
        cnr1[1] = round(cnr1[1])
        # calculate new cnr2 y coord
        cnr2[1] = y_mid + (y_mid - cnr1[1])
    else:
        cnr2[1] = round(cnr2[1])
        # calculate new cnr1 y coord
        cnr1[1] = y_mid + (y_mid - cnr2[1])
    rect = (tuple(cnr1), tuple(cnr2))
    return rect
