from PizzaParser import pizza_parser
import time

def solve(input_files):
    for file_name in input_files:
        print "******************* Reading file {} *******************".format(file_name)
        pizza = pizza_parser(file_name)
        print pizza
        time.sleep(1)
        #raw_input()
    print "SOLVED"
