class Slide:
    def __init__(self, photos):
        self.photos=photos
        if len(photos) == 1 :
            self.tags = photos[0].tags
        else :
            self.tags = photos[0].tags.union(photos[1].tags)

    def __str__(self):
        return "slide {}\n".format(str(self.photos))

    def score(self, autre_slide):
        common_tag = len(self.tags.intersection(autre_slide.tags))
        tag_only_s1 = len(self.tags.difference(autre_slide.tags))
        tag_only_s2 = len(autre_slide.tags.difference(self.tags))
        score = min(common_tag, tag_only_s1, tag_only_s2)
        return score / self.score_ideal(autre_slide)

    def score_ideal(self, autre_slide):
        return (len(self.tags) + len(autre_slide.tags))/4