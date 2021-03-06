from collections import deque
import tqdm


class Problem:
    def __init__(self, grille, list_vehicles, list_rides, t, b):
        self.grid = grille
        self.list_vehicles = list_vehicles

        self.list_rides = list_rides
        self.time = t
        self.bonus = b

    def __str__(self):
        s = "Grid {}\n".format(str(self.grid))
        s += "Vehicles \n{}\n".format("\n".join(str(vehicle) for vehicle in self.list_vehicles))
        s += "Rides \n{}\n".format("\n".join(str(ride) for ride in self.list_rides))
        s += "Max time {} / Bonus {}".format(self.time, self.bonus)
        return s

    def get_output(self):
        return "\n".join(v.get_output() for v in self.list_vehicles)

    def solve(self):
        excluded_rides = [r for r in self.list_rides if r.feasible and r.end_point[0]>9000 or r.end_point[1]>9000]
        self.list_rides = [r for r in self.list_rides if r.feasible and r.end_point[0]<9000 and r.end_point[1]<9000]
        print "Max score = ", sum(r.length for r in self.list_rides)+self.bonus * len(self.list_rides)
        self.list_rides.sort(key=lambda x: x.length, reverse=True)
        self.list_rides = deque(self.list_rides)
        remaining_rides_id = set(r.id for r in self.list_rides)
        remaining_excluded_rides_id = set(r.id for r in self.list_rides)

        for current_time in tqdm.tqdm(xrange(self.time)):
            # print self
            for vehicle in self.list_vehicles:
                if vehicle.time == 0:
                    possible_excluded_rides=[r for r in excluded_rides if
                                      r.id in remaining_excluded_rides_id and 25> r.end_time -vehicle.ride_duration(r, current_time)+  current_time]
                    if possible_excluded_rides:
                        best_ride = max(possible_excluded_rides,
                                        key=lambda ride: vehicle.ride_score(ride, current_time, self.bonus))
                        vehicle.affect_ride(best_ride, current_time)
                        remaining_excluded_rides_id.remove(best_ride.id)
                    if vehicle.time == 0:
                        possible_rides = [r for r in self.list_rides if
                                      r.id in remaining_rides_id and vehicle.ride_duration(r, current_time)+  current_time < r.end_time]
                        if possible_rides:
                            best_ride = max(possible_rides, key=lambda ride: vehicle.ride_score(ride, current_time, self.bonus))
                            #  vehicle.ride_score_recursif(ride, current_time, possible_rides,remaining_rides_id,1,self.bonus))
                            vehicle.affect_ride(best_ride, current_time)
                            remaining_rides_id.remove(best_ride.id)
                vehicle.time -= 1
        return ""
