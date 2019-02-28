
class Problem:
    def __init__(self, photos):
        self.slideshow = []
        self.photos = photos

    def __str__(self):
        s = "Photos available {}\n".format(str(self.photos))
        s += "Slideshow \n{}\n".format("\n".join(str(slide) for slide in self.slideshow))
        return s

    def get_output(self):
        s = str(len(self.slideshow))+"\n"
        s += ["\n".join(" ".join(photo.id for photo in slide) for slide in self.slideshow)]
        return "\n".join(v.get_output() for v in self.list_vehicles)

    def solve(self):
        pass