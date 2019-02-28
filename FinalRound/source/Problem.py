
class Problem:
    def __init__(self, photos):
        self.slideshow = []
        self.photos = photos
        self.slides=self.slide_creator()

    def __str__(self):
        s = "Photos available {}\n".format(str(self.photos))
        s += "Slideshow \n{}\n".format("\n".join(str(slide) for slide in self.slideshow))
        return s

    def get_output(self):
        s = str(len(self.slideshow))+"\n"
        s += ["\n".join(" ".join(photo.id for photo in slide) for slide in self.slideshow)]
        return s

    def slide_creator(self):
        slides=[]
        bol=False
        enattente=None
        for f in self.photos:
            if f.is_horizontal:
                slides.append(f)
            elif enattente:
                slides.append(Slide(enattente,f))
                enattente=None
            else:
                enattente=f
        return slides

    def solve(self):
        pass