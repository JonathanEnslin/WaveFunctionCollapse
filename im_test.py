from PIL import Image
import numpy as np

def find_non_base_indices(im, check_row=0, check_col=None, base_colour=np.array([40, 40, 50])):

    pixel_vals_flat = list(im.getdata())

    width, height = im.size

    pixel_mat = np.array(pixel_vals_flat).reshape((height, width, 3))

    # find the first and last x-vals on the bottom edge where the colour does not match the base colour, print sorted
    if check_col is None:
        check_edge = pixel_mat[check_row,:]
    else:
        check_edge = pixel_mat[:,check_col]

    indices = []
    for idx, pixel in enumerate(check_edge):
        if not np.array_equal(pixel, base_colour):
            indices.append(idx)

    print(indices[0], indices[-1])

im = Image.open('sprites/dead_end.png', 'r')
find_non_base_indices(im, -1)
rot_im = im.rotate(180)
find_non_base_indices(rot_im)

hor_im = im.rotate(90)
find_non_base_indices(hor_im, None, -1)

hor_im_rot = im.rotate(270)
find_non_base_indices(hor_im_rot, None, 0)
