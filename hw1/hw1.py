"""HW1: transform the four vehicle corners into the world frame."""

import numpy as np


def get_corners(xy, theta, corner1, corner2, corner3, corner4):
    """Return the four world-frame corner positions in the same order.

    Args:
        xy: Vehicle position as a NumPy array of shape (2, 1).
        theta: Vehicle heading in radians, measured counterclockwise.
        corner1, corner2, corner3, corner4: Vehicle-frame corner positions,
            each with shape (2, 1).

    Returns:
        A tuple of four NumPy arrays, each with shape (2, 1).
    """
    # TODO: implement the rotation and translation for each corner.

    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ]) # rotation matrix

    new_corner1 = R @ corner1 + xy
    new_corner2 = R @ corner2 + xy
    new_corner3 = R @ corner3 + xy
    new_corner4 = R @ corner4 + xy
    
    print([new_corner1, new_corner2, new_corner3, new_corner4])
    return new_corner1, new_corner2, new_corner3, new_corner4