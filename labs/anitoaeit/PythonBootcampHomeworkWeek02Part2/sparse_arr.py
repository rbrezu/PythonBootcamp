
class Sparse2D:
    def __init__(self, arr):
        self.index = {}
        self.lines = len(arr)
        self.columns = max([len(x) for x in arr])
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] is not 0:
                    self.index[(i, j)] = arr[i][j]

    def __len__(self):
        return self.lines * self.columns

    def __repr__(self):
        return 'Sparse2D({}, {})'.format(self.lines, self.columns)

    def __str__(self):
        strng = ''
        for i in range(self.lines):
            for j in range(self.columns):
                if (i, j) in self.index.keys():
                    strng += '{} '.format(self.index[(i, j)])
                else:
                    strng += '0 '
            strng += '\n'
        return strng

    def __setitem__(self, key, value):
        if isinstance(key, tuple) is False:
            raise TypeError('The index must be a tuple!')

        line = key[0]
        column = key[1]
        if line > self.lines:
            self.lines = line + 1
        if column > self.columns:
            self.columns = column + 1
        if value is not 0:
            self.index[key] = value
        elif key in self.index:
            self.index.pop(key)

    def __getitem__(self, key):
        if isinstance(key, tuple) is False:
            raise TypeError('The index must be a tuple!')
        if 0 <= key[0] < self.lines is False:
            raise IndexError('Index out of range.')
        if 0 <= key[1] < self.columns is False:
            raise IndexError('Index out of range.')

        if key in self.index:
            return self.index[key]
        return 0

    def __delitem__(self, key):
        if isinstance(key, tuple) is False:
            raise TypeError('The index must be a tuple!')
        if 0 <= key[0] < self.lines is False:
            raise IndexError('Index out of range.')
        if 0 <= key[1] < self.columns is False:
            raise IndexError('Index out of range.')

        if key in self.index:
            self.index.pop(key)




arr2d = Sparse2D([[1, 0, 0], [2, 3], [0, 0, 0, 0, 1]])
print(arr2d)

