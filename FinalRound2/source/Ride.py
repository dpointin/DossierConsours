class Ride:
    def __init__(self, id, start_point, end_point, start_time, end_time):
        self.id = id
        self.start_point = start_point
        self.end_point = end_point
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        s = "ID = {}\nStart Point = {} \n".format(self.id,self.start_point)
        s += "End Point = {}\n".format(self.end_point)
        s += "Minimum start time = {}\n".format(self.start_time)
        s += "Maximum end time = {}\n".format(self.end_time)
        s += "Length = {}\n".format(self.length)
        return s

    @property
    def length(self):
        return abs(self.start_point[0] - self.end_point[0]) + abs(self.start_point[1] - self.end_point[1])

    @property
    def feasible(self):
        return self.length <= (self.end_time - self.start_time) and self.start_time < self.end_time

