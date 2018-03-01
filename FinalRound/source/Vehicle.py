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
        self.time = self.ride_duration(ride, current_time)
        self.position = ride.end_point

    def move_to_start_time(self, ride):
        return abs(ride.start_point[0] - self.position[0]) + abs(ride.start_point[1] - self.position[1])

    def wait_time(self, ride, current_time):
        return ride.start_time - current_time - self.move_to_start_time(ride)

    def ride_duration(self, ride, current_time):
        duration = self.move_to_start_time(ride)
        duration += max(0, self.wait_time(ride, current_time))
        duration += ride.length
        return duration

    def ride_score(self, ride, current_time, bonus):
        score = ride.length / float(self.move_to_start_time(ride) + max(0, self.wait_time(ride, current_time)) + 1)
        if self.wait_time(ride, current_time) >= 0:
            score += bonus / float(self.ride_duration(ride, current_time) + 1)
        return score

    def get_output(self):
        s = str(len(self.list_rides)) + " " + " ".join(str(r.id) for r in self.list_rides)
        return s
