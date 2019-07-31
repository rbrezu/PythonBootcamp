import os


def read_last_n(f, lines):
    buffer_size = 8
    total_lines_wanted = lines + 1
    total_lines_found = 0
    f.seek(0, 2)
    total_bytes = f.tell()
    size = total_bytes
    data = []
    block = 1

    while total_bytes > 0 and total_lines_found <= total_lines_wanted:
        if total_bytes > buffer_size:
            f.seek(size - block * buffer_size, 0)
            line = f.read(buffer_size)
        else:
            f.seek(0, 0)
            line = f.read(total_bytes)

        total_bytes -= buffer_size
        total_lines = line.count('\n')
        total_lines_found += total_lines
        block += 1
        data.insert(0, line)

    return ''.join(data).splitlines()[-lines:]


curr_path = os.path.curdir
file_path = os.path.join(curr_path, 'another_txt_file.txt')
text_file = open(file_path, 'r')
print(read_last_n(text_file, 3))
text_file.close()