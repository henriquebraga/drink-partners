
import math


def get_coordinate_distance_points(a, b):
    return math.sqrt(
        ((a[0]-b[0])**2) +
        ((a[1]-b[1])**2)
    )
