import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._diameter = 2 * radius
        self._area = 2 * math.pi * radius

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(other * self.radius)

    def __rmul__(self, other):
        return Circle(other * self.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = value / 2
        self._area = self._diameter * math.pi

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        raise AttributeError('Cannot set area manually.')

    @classmethod
    def from_diameter(cls, value):
        return cls(value / 2)


circles = []
for i in range(10):
    circles.insert(0, Circle(i))

print(circles)
print(sorted(circles))