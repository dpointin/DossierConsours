from FinalRound.source.Slide import Slide


class Problem:
    def __init__(self, photos):
        self.slideshow = []
        self.photos = photos
        self.slides = self.slide_creator()

    def __str__(self):
        s = "Photos available {}\n".format(str(self.photos))
        s += "Slideshow \n{}\n".format("\n".join(str(slide) for slide in self.slideshow))
        return s

    def get_output(self):
        s = str(len(self.slideshow)) + "\n"
        for slide in self.slideshow:
            s+= " ".join(str(photo.id) for photo in slide.photos) + "\n"
        return s

    def slide_creator(self):
        slides = []
        bol = False
        enattente = None
        for f in self.photos:
            if f.is_horizontal:
                slides.append(Slide([f]))
            elif enattente:
                slides.append(Slide([enattente, f]))
                enattente = None
            else:
                enattente = f
        return slides

    def solve(self):
        self.slideshow = self.slides
