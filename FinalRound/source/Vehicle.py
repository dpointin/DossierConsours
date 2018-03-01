class Vehicle:
    def __init__(self, id, T):
        self.id = id
        self.position = (0, 0)
        self.list_rides = []
        self.temps_total = T
        self.time = 0

    def __str__(self):
        s = "ID = {}\nPosition = {} \n".format(self.id, self.position)
        s += "Time= {}\n".format(self.time)
        return s

    def affect_ride(self, ride, current_time):
        self.list_rides.append(ride)
        ###Ajouter le temps d'attente
        self.time = self.ride_cost(ride, current_time)
        self.position = ride.end_point

    def ride_cost(self, ride, current_time):
        score = max(ride.start_time - current_time,
                    (abs(ride.start_point[0] - self.position[0]) + abs(ride.start_point[1] - self.position[1])))
        score += abs(ride.start_point[0] - ride.end_point[0]) + abs(ride.start_point[1] - ride.end_point[1])
        return score

    def ride_score(self, ride, current_time):
        return float(
            abs(ride.start_point[0] - ride.end_point[0]) + abs(ride.start_point[1] - ride.end_point[1])) / float(
            max(ride.start_time - current_time,
                (abs(ride.start_point[0] - self.position[0]) + abs(ride.start_point[1] - self.position[1])))+1)

    def get_output(self):
        s = str(len(self.list_rides)) + " " + " ".join(str(r.id) for r in self.list_rides)
        return s
