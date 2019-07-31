import math

class Circle:
    def __init__(self, r):
        self.r = r

    @classmethod
    def from_diameter(cls, d):
        return cls(d / 2)

    @property
    def diameter(self):
        return self.r * 2

    @diameter.setter
    def diameter(self, d):
        self.r = d / 2

    @property
    def area(self):
        return self.r ** 2 * math.pi

    def __str__(self):
        return 'Circle with radius {}'.format(self.r)

    def __repr__(self):
        return 'Circle({})'.format(self.r)

    def __add__(self, other):
        if not isinstance(other, Circle):
            raise NotImplemented

        return Circle(other.r + self.r)

    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            raise NotImplemented

        return Circle(other * self.r)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise NotImplemented

        return Circle(other * self.r)

    def __lt__(self, other):
        if not isinstance(other, Circle):
            raise NotImplemented

        return self.r < other.r

    def __gt__(self, other):
        if not isinstance(other, Circle):
            raise NotImplemented

        return self.r > other.r

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise NotImplemented

        return self.r == other.r


if __name__ == '__main__':
    c = Circle(2)
    f = Circle.from_diameter(4)

    print (c)
    print (f)
    print (c.diameter)

    c.diameter = 4
    print (c)
    print (c.area)

    d = c + f
    print (d)
    print (d * 2)
    print (2 * d)

    print (sorted([d, c, f]))