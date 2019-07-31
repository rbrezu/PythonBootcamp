import os


def read_n_lines(simple_file, lines):
    with open(simple_file, 'r') as text_file:
        for i in range(lines):
            print(text_file.readline().strip())


curr_dir = os.path.curdir
file_path = os.path.join(curr_dir, 'some_text.txt')

read_n_lines(file_path, 5)

