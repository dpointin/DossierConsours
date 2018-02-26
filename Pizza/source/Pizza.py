import numpy as np
import tqdm


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
