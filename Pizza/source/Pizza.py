class Pizza:
    def __init__(self, grid, l, h):
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
        self.grid = grid
        self.min_ing_number = l
        self.max_size = h

    def __str__(self):
        s = "Pizza Size = {} rows * {} cols\n".format(self.n_rows, self.n_cols)
        s += "Min Number of each ingredient per slice = {}\n".format(self.min_ing_number)
        s += "Max Size of each slice = {}\n".format(self.max_size)
        s += "Pizza\n{}".format("\n".join(self.grid))
        return s
