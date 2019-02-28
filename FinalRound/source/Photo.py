class Photo :
    def __init__(self, id, isH, tags):
        self.id = id
        self.is_horizontal = isH
        self.tags = set(tags)

    def __str__(self):
        return "{} - {}".format(self.id, self.is_horizontal)
        #return "id {} - horizontal {} - tags : {}".format(self.id, self.is_horizontal, self.tags)


