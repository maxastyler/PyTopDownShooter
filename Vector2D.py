import math
class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'x: ' + str(self.x) + ', y: ' + str(self.y)


    def __name__(self):
        return 'vector2D'

    def __add__(self, other):
        if type(other).__name__=='tuple':
            return Vector2D(self.x+other[0], self.y+other[1])
        return Vector2D(self.x+other.x, self.y+other.y)

    def __radd__(self, other):
        return self+other

    def __iadd__(self, other):
        self.x+=other.x
        self.y+=other.y
        return self

    def __sub__(self, other):
        if type(other).__name__ == 'tuple':
            return Vector2D(self.x-other[0], self.y-other[1])

        return Vector2D(self.x-other.x, self.y-other.y)

    def __rsub__(self, other):
        if type(other).__name__ == 'tuple':
            return Vector2D(other[0]-self.x, other[1]-self.y)
        return Vector2D(other.x-self.x, other.y-self.y)

    def __isub(self, other):

        self.x-=other.x
        self.y-=other.y
        return self

    def __mul__(self, other):
        if type(other).__name__=='Vector2D':
            return self.x*other.x + self.y*other.y
        return Vector2D(self.x*other, self.y*other)

    def __rmul__(self, other):
        return Vector2D(self.x*other, self.y*other)

    def __imul__(self, other):
        if type(other).__name__=='Vector2D':
            self.x*=other.x
            self.y*=other.y
        else:
            self.x*=other
            self.y*=other
        return self

    def __truediv__(self, other):
        return Vector2D(self.x/other, self.y/other)

    def __idiv__(self, other):
        self.x/=other
        self.y/=other
        return self

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __abs__(self):
        return math.sqrt(math.pow(self.x, 2)+math.pow(self.y,2))

    def get_norm(self):
        try:
            return self/abs(self)
        except ZeroDivisionError:
            return Vector2D(0, 0)

    def norm(self):
        self = self.get_norm()

    def angle_from_vector(self):
        angle=math.acos(self.get_norm()*Vector2D(0, 1))
        if self.x < 0:
            angle=2*math.pi-angle
        return angle

    def to_tuple(self):
        return (self.x, self.y)
