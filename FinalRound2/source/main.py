from input_reader import problem_parser
import os


def write_output(input_file, output_folder, output):
    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + ".out")
    with open(output_file, "w+") as f:
        f.write(output)


def solve(input_files, output_folder):
    for file_name in input_files:
        print "******************* Reading file {} *******************".format(file_name)
        problem = problem_parser(file_name)
        print "\n\nINPUT = "
        #print problem
        problem.solve()
        output = problem.get_output()
        #print "\n\nOUTPUT = "
        #print output
        write_output(file_name, output_folder, problem.get_output())
        print "******************** Solved file {} *******************".format(file_name)
