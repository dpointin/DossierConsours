class Vehicle:
    def __init__(self, id, T):
        self.id = id;
        self.position=(0,0);
        self.list_rides=[];
        self.temps_total=T;

    def __str__(self):
        s = str(id)
        s +=  " ".join(str(r.id) for r in self.list_rides) + "\n"
        return s

