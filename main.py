from OutputSubmitter import OutputSubmitter
import importlib
import os


def get_input_files(project_name):
    input_folder = os.path.join(os.getcwd(), project_name, "input")
    return sorted(os.path.abspath(os.path.join(input_folder, path)) for path in os.listdir(input_folder))


def hash_code(project_name):
    project_module = importlib.import_module(project_name + ".source.main")
    output_folder = os.path.join(os.getcwd(), project_name, "output")
    getattr(project_module, "solve")(get_input_files(project_name), output_folder)


    output_submitter = OutputSubmitter(project_name)
    output_submitter.google_log_in()
    output_submitter.submit_output()
    raw_input()
    output_submitter.close()


if __name__ == '__main__':
    hash_code("FinalRound")
