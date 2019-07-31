import os


def get_dir_size(dirr, level):
    size = 0
    for i in range(level):
        print('\t', end = '')
    for file in os.listdir(dirr):
        if os.path.isdir(file):
            print('D {}'.format(file))
            size += get_dir_size(os.path.join(dirr, file), level + 1)
        else:
            file_size = os.path.getsize(os.path.join(dirr, file))
            print('F {:{}} - {:>20} Bytes'.format(file, 50 - 4 * level, file_size))
            size += file_size
    return size


curr_dir = os.path.curdir
print('Total size: {}'.format(get_dir_size(curr_dir, 0)))
