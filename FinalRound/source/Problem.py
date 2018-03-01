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
        return str(self)

    def solve(self):
        return ""

