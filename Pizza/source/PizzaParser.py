from Pizza import Pizza
import numpy as np


def pizza_parser(file_name):
    with open(file_name, "r") as f:
        r, c, l, h = map(int, f.readline().strip().split())
        grid = np.array([list(map(lambda x: 1 if x == 'T' else 0, f.readline().strip())) for _ in xrange(r)])
        return Pizza(grid, l, h)
