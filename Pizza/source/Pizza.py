import numpy as np
import tqdm
import logging
from collections import deque

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(module)s : %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")


class Pizza:
    def __init__(self, grid, l, h):
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
        self.grid = grid
        self.min_ing_number = l
        self.max_size = h
        self.slices = []

    def __str__(self):
        s = "Pizza Size = {} rows * {} cols\n".format(self.n_rows, self.n_cols)
        s += "Min Number of each ingredient per slice = {}\n".format(self.min_ing_number)
        s += "Max Size of each slice = {}\n".format(self.max_size)
        s += "Pizza\n{}".format(str(self.grid))
        return s

    def get_output(self):
        return str(len(self.slices)) + "\n" + \
               "\n".join(" ".join(str(c) for c in pizza_slice) for pizza_slice in self.slices)

    def get_possible_shapes(self):
        possible_shapes_set = set()
        for size in xrange(2 * self.min_ing_number, self.max_size):
            # https://stackoverflow.com/questions/16939402/quick-way-to-extend-a-set-if-we-know-elements-are-unique
            for i in xrange(1, int(pow(size, 0.5) + 1)):
                if size % i == 0:
                    possible_shapes_set.add((i, size // i))
                    possible_shapes_set.add((size // i, i))
        return possible_shapes_set

    def greedy_solve(self):
        possible_shapes = sorted(list(self.get_possible_shapes()), key=lambda s: s[0], reverse=False)
        logging.info("Input = {} \n".format(str(self)))
        logging.info("Possible shapes = " + str(possible_shapes))
        possible_locations = deque([(x, y) for x in xrange(self.n_rows) for y in xrange(self.n_cols)])
        empty_cells = set(possible_locations)
        for it in xrange(1000000):
            if it % 100 == 0:
                logging.info("Iteration = {} - Max Score = {} - Current Score = {} - Score % = {}".format(
                    it, self.n_cols * self.n_rows, self.n_cols * self.n_rows - len(empty_cells),
                    round(100 * (self.n_cols * self.n_rows - len(empty_cells)) / float(self.n_cols * self.n_rows), 2)))
            if not possible_locations:
                break
            location = possible_locations.popleft()
            for shape in possible_shapes:
                if self.slice_fits(location, shape, empty_cells) and \
                        self.is_slice_content_valid(location[0], location[1],
                                                    location[0] + shape[0], location[1] + shape[1]):
                    break
            else:
                continue
            self.slices.append((location[0], location[1],
                                location[0] + shape[0] - 1, location[1] + shape[1] - 1))
            for i in xrange(shape[0]):
                for j in xrange(shape[1]):
                    empty_cells.remove((location[0] + i, location[1] + j))
                    try :
                        possible_locations.remove((location[0] + i, location[1] + j))
                    except ValueError:
                        pass
        logging.info("FINAL --- Iteration = {} - Max Score = {} - Current Score = {} - Score % = {}".format(
            it, self.n_cols * self.n_rows, self.n_cols * self.n_rows - len(empty_cells),
            round(100 * (self.n_cols * self.n_rows - len(empty_cells)) / float(self.n_cols * self.n_rows), 2)))

    def guillotine_solve(self):
        """
        It creates slices by dividing each region either vertically or horizontal.
        Each sub region is then divided again until :
        - The area contains less ingredients than required
        - The area is a vaid slice
        http://tryalgo.org/fr/2017/01/22/google-hashcode-google-pizza/
        """
        pizza_slices = [(i, j, k, l)
                        for i in xrange(self.n_rows)
                        for j in xrange(self.n_cols)
                        for k in xrange(i + 1, self.n_rows + 1)
                        for l in xrange(j + 1, self.n_cols + 1)
                        if (k - i) * (l - j) >= 2 * self.min_ing_number]

        # pizza_slices = [pizza_slice for pizza_slice in pizza_slices if pizza_slice.slice_size >= min_slice_size]
        pizza_slices.sort(key=lambda (m, n, o, p): (o - m) * (p - n))

        slice_score = {}
        slice_cut = {}
        for (i, j, k, l) in tqdm.tqdm(pizza_slices):
            slice_score[(i, j, k, l)] = 0
            slice_cut[(i, j, k, l)] = None
            if not self.is_slice_content_valid(i, j, k, l):
                continue
            if self.is_slice_size_valid(i, j, k, l):
                slice_score[(i, j, k, l)] = (k - i) * (l - j)
            for vertical_cut in xrange(1, l - j):
                temp_score = slice_score[(i, j, k, j + vertical_cut)] \
                    if (i, j, k, j + vertical_cut) in slice_score else 0
                temp_score += slice_score[(i, j + vertical_cut, k, l)] \
                    if (i, j + vertical_cut, k, l) in slice_score else 0
                if temp_score > slice_score[(i, j, k, l)]:
                    slice_score[(i, j, k, l)] = temp_score
                    slice_cut[(i, j, k, l)] = vertical_cut
            for horizontal_cut in xrange(1, k - i):
                temp_score = slice_score[(i, j, i + horizontal_cut, l)] \
                    if (i, j, i + horizontal_cut, l) in slice_score else 0
                temp_score += slice_score[(i + horizontal_cut, j, k, l)] \
                    if (i + horizontal_cut, j, k, l) in slice_score else 0
                if temp_score > slice_score[(i, j, k, l)]:
                    slice_score[(i, j, k, l)] = temp_score
                    slice_cut[(i, j, k, l)] = -horizontal_cut

        stack = [(0, 0, self.n_rows, self.n_cols)]
        while stack:
            i, j, k, l = stack.pop()
            cut = slice_cut[(i, j, k, l)]
            if not cut:
                if slice_score[(i, j, k, l)]:
                    self.slices.append((i, j, k - 1, l - 1))
            elif cut > 0:
                stack.append((i, j, k, j + cut))
                stack.append((i, j + cut, k, l))
            elif cut < 0:
                stack.append((i, j, i - cut, l))
                stack.append((i - cut, j, k, l))

    def is_slice_content_valid(self, i, j, k, l):
        n_tomato = np.sum(self.grid[i:k, j:l])
        return (k - i) * (l - j) - self.min_ing_number >= n_tomato >= self.min_ing_number

    def is_slice_size_valid(self, i, j, k, l):
        return (k - i) * (l - j) <= self.max_size

    def slice_fits(self, random_location, shape, empty_cells):
        return all((random_location[0] + i, random_location[1] + j) in empty_cells
                   for i in xrange(shape[0]) for j in xrange(shape[1]))
