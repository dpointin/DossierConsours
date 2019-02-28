class Slide:
    def __init__(self, photos):
        self.photos=photos
        self.tags=set.union(*[photo.tags for photo in photos])

    def __str__(self):
        return "slide {}\n".format(str(self.photos))

    def score(self, autre_slide):
        score = min()
