from Problem import Problem
from Photo import Photo


def problem_parser(file_name):
    with open(file_name, "r") as input_file:
        n = int(input_file.readline().strip())
        photos = []
        for i in xrange(n):
            l = input_file.readline().strip().split()
            is_horizontal = l[0] == "H"
            tags = l[2:]
            photos.append(Photo(i, is_horizontal, tags))
    return Problem(photos)
