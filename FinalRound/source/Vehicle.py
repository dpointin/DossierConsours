class Vehicle:
    def __init__(self, id, T):
        self.id = id
        self.position = (0, 0)
        self.list_rides = []
        self.temps_total = T
        self.time=0

    def __str__(self):
        s = "ID = {}\nPosition = {} \n".format(self.id,self.position)
        s += "Total time= {}\n".format(self.temps_total)
        return s

    def affect_ride(self, ride, current_time):
        self.list_rides.append(ride)
        ###Ajouter le temps d'attente
        time=self.ride_cost(ride,current_time)
        position=ride.end_point

    def ride_cost(self, ride, current_time):
        score = max(ride.start_time  -current_time   ,(abs(ride.start_point[0] - self.position[0]) + abs(ride.start_point[1] - self.position[1])))
        score += abs(self.position[0] - ride.end_point[0]) + abs(self.position[1] - ride.end_point[1])
        return score



    def get_output(self):
        s = str(len(self.list_rides))+" "+" ".join(str(r.id) for r in self.list_rides)
        return s

