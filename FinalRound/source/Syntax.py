class Request:
    def __init__(self, id, video, end_point, number):
        self.nb = number
        self.end_point = end_point
        self.id = id
        self.video = video

    def __str__(self):
        return "Request id {id} - End Point {ep} - Video {v} - NB  {nb}".format(id=self.id, ep=self.end_point,
                                                                                v=self.video, nb=self.nb)

    @property
    def size(self):
        return self.id * self.nb


def print_requests(req):
    print "\n".join(str(r) for r in req)


def print_requests_dict(d):
    print "\n".join(str(i) + " = " + str(d[i]) for i in d)


if __name__ == '__main__':
    requests = [Request(1, None, None, 10), Request(2, None, None, 15), Request(3, None, None, 12)]
    print "**************** LISTS ***************"
    print "------- List comprehension"
    print_requests([request for request in requests if request.nb > 10])
    print "------- Requests"
    print_requests(requests)
    requests.append(Request(4, None, None, 26))
    print "------- Append new request "
    print_requests(requests)
    requests.remove(requests[3])
    print "------- Remove request "
    print_requests(requests)
    print "------- Reverse - two methods"
    print "Method 1"
    print_requests(reversed(requests))
    print "Method 2"
    requests.reverse()
    print_requests(requests)
    print "------- Sort by nb desc"
    print_requests(sorted(requests, key=lambda x: x.nb, reverse=True))
    print "\n**************** DICTS ***************"
    print "------- Dict, key = request id, value = id"
    requests_dict = {key: value for key, value in zip([x.id for x in requests], requests)}
    print_requests_dict(requests_dict)
    print "------- Modify dict element at id 2"
    requests_dict[2] = Request(5, None, None, 25)
    print_requests_dict(requests_dict)
    print "------- Delete element at 1"
    del requests_dict[1]
    print_requests_dict(requests_dict)
    print "------- Modify video attribute of element at id 2"
    requests_dict[2].end_point = "TEST"
    print_requests_dict(requests_dict)
