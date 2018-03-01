from Problem import Problem
from Vehicle import Vehicle
from Ride import Ride
import numpy as np


def problem_parser(file_name):
    with open(file_name, "r") as input_file:
        r, c, f, n, b, t = map(int, input_file.readline().strip().split())
        grid = np.zeros(shape=(r, c))
        vehicles = [Vehicle(i, t) for i in xrange(f)]
        rides = []
        for i in xrange(n):
            a, b, x, y, s, t = map(int, input_file.readline().strip().split())
            rides.append(Ride(i, (a, b), (x, y), s, y))
        return Problem(grid, vehicles, rides, t, b)
