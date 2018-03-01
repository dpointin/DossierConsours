class Problem:
    def __init__(self, grille, list_vehicle, list_rides, T, B):
        self.grid = grille
        self.list_vehicle=list_vehicle
        self.list_rides = list_rides
        self.time = T
        self.bonus = B



    def __str__(self):
        s = "\n".join(str(r) for r in self.list_vehicle)
        return s

    def get_output(self):
        return str(len(self.slices)) + "\n" + \
               "\n".join(" ".join(str(c) for c in pizza_slice) for pizza_slice in self.slices)

    def solve(self):
        return ""

