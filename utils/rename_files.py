import os
import glob

order = [
    'venv',
    'numbers',
    'strings',
    'lists',
    'dictionaries',
    'conditionals',
    'loops',
    'functions'
]

def rename():
    i = 0
    for filename in glob.glob('*.ipynb'):
        full = os.path.basename(filename)
        fname = os.path.splitext(full)[0]
        name = fname.split('_')[1]

        idx = order.index(name)
        renamed = '{0:02d}_{1}.ipynb'.format(idx, name)
        print(renamed)

        os.rename(full, renamed)

if __name__ == '__main__':
    rename()