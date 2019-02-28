class Photo :
    def __init__(self, id, isH, tags):
        self.id = id
        self.is_horizontal = isH
        self.tags = tags

    def __str__(self):
        return "id {id} - horizontal {isH} - tags : {tags}"


