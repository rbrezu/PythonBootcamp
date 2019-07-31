import os

curr_dir = os.path.abspath(os.path.curdir)
copy_dir = os.path.join(curr_dir, 'copy')

print('Files in directory: ', os.listdir(curr_dir))
os.mkdir(copy_dir)

for file in os.listdir(curr_dir):
    if file.endswith('.txt'):
        os.rename(os.path.join(curr_dir, file), os.path.join(copy_dir, file))

