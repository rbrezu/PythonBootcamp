class SparseArray:
    def __init__(self, l):
        self.d = {}
        self.length = len(l)

        for idx, item in enumerate(l):
            if item:
                self.d[idx] = item

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        if item >= self.length:
            raise IndexError('index is bigger than the length')

        if item not in self.d:
            return 0

        return self.d[item]

    def append(self, item):
        if item:
            self.d[self.length] = item

        self.length += 1

if __name__ == '__main__':
    s = SparseArray((1, 0, 0, 0, 2, 0, 0, 0, 5))

    print(len(s))
    print(s[4])

    s.append(2)
    s.append(3)

    print(len(s))
    print(s[8], s[9], s[10])

    print (s[11])