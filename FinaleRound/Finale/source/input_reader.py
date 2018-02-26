from Pizza import Pizza


def pizza_parser(file_name):
    with open(file_name, "r") as f:
        r, c, l, h = map(int, f.readline().strip().split())
        grid = []
        for i in xrange(r):
            grid.append(f.readline().strip())
        return Pizza(grid, l, h)
