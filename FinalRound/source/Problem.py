from collections import deque

class Problem:
    def __init__(self, grille, list_vehicles, list_rides, T, B):
        self.grid = grille
        self.list_vehicles = list_vehicles

        self.list_rides =list_rides
        self.time = T
        self.bonus = B

    def __str__(self):
        s = "Grid {}\n".format(str(self.grid))
        s += "Vehicles \n{}\n".format("\n".join(str(vehicle) for vehicle in self.list_vehicles))
        s += "Rides \n{}\n".format("\n".join(str(ride) for ride in self.list_rides))
        return s

    def get_output(self):
        return "\n".join(v.get_output() for v in self.list_vehicles)

    def solve(self):
        self.list_rides = [r for r in self.list_rides if r.feasible]
        self.list_rides.sort(key=lambda x: x.length)
        self.list_rides = deque(self.list_rides)
        for vehicle in self.list_vehicles:
            if self.list_rides:
                vehicle.list_rides.append(self.list_rides.popleft())
        return ""
