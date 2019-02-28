from FinalRound.source.Slide import Slide


class Problem:
    def __init__(self, photos):
        self.slideshow = []
        self.photos = photos
        self.slides = self.slide_creator()

    def __str__(self):
        s = "Slides available {}\n".format("\n".join(str(slide) for slide in self.slides))
        # s += "Slideshow \n{}\n".format("\n".join(str(slide) for slide in self.slideshow))
        return s

    def get_output(self):
        s = str(len(self.slideshow)) + "\n"
        for slide in self.slideshow:
            s += " ".join(str(photo.id) for photo in slide.photos) + "\n"
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

    def slide_creator2(self):
        slides = []
        enattente = []
        for f in self.photos:
            if f.is_horizontal:
                slides.append(Slide([f]))
            else:
                enattente.append(f)

        enattente.sort(key=lambda x: len(x.tags), reverse=False)
        while (len(enattente) > 1):
            slides.append(Slide([enattente.pop(0), enattente.pop(-1)]))

        return slides

    def solve(self):
        # Clean slides with one tag
        # self.slides = [slide for slide in self.slides if slide.tags < 1]
        print "****", self
        curr_slide = self.slides[0]
        self.slideshow.append(curr_slide)
        self.slides.remove(curr_slide)
        i = 0
        s = len(self.slides)
        while self.slides:
            if i % 100 == 0:
                print "{} loops done over {}".format(i, s)
            max_score = -1
            max_slide = None
            for slide in self.slides:
                slide_score = slide.score(curr_slide)
                if slide_score > max_score:
                    max_score = slide_score
                    max_slide = slide
            self.slideshow.append(max_slide)
            self.slides.remove(max_slide)
            curr_slide = max_slide
            i += 1

    def solve_example_b(self):
        self.slides.sort(key=lambda x: len(x.tags))
        curr_slide = self.slides[0]
        i = 0
        s = len(self.slides)
        while self.slides:
            if i % 100 == 0:
                print "{} loops done over {}".format(i, s)
            for slide in self.slides:
                slide_score = slide.score(curr_slide)
                if slide_score > 0:
                    self.slideshow.append(slide)
                    self.slideshow.remove(slide)
                    curr_slide = slide
                    break
            else:
                break
            i += 1
