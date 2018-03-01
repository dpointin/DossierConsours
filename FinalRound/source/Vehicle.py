class Vehicle:
    def __init__(self, id, T):
        self.id = id
        self.position = (0, 0)
        self.list_rides = []
        self.temps_total = T

    def __str__(self):
        s = "ID = {}\nPosition = {} \n".format(self.id,self.position)
        s += "Total time= {}\n".format(self.temps_total)
        return s

    def get_output(self):
        s = str(len(self.list_rides))+" "+" ".join(str(r.id) for r in self.list_rides)
        return s