class Slide:
    def __init__(self, photos):
        self.photos=photos
        self.tags=set.union(*[photo.tags for photo in photos])

    def __str__(self):
        return "slide {}\n".format(str(self.photos))

    def score(self, autre_slide):
        common_tag = self.tags.intersection(autre_slide.tags)
        tag_only_S1 = self.tags.difference(autre_slide.tags)
        tag_only_S2 = autre_slide.tags.difference(self.tags)
        score = min(common_tag,tag_only_S1,tag_only_S2)
        return score
