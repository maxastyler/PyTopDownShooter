from Vector2D import Vector2D
import copy
class Matrix22:
    def __init__(self, m11, m12, m21, m22):
        self.m11 = m11
        self.m12 = m12
        self.m21 = m21
        self.m22 = m22

    def __repr__(self):
        return 'm11: ' + str(self.m11) + ' m12: ' + str(self.m12) + ' m21: ' + str(self.m21) + ' m22: ' + str(self.m22)

    def __add__(self, other):
        return Matrix22(self.m11+other.m11, self.m12+other.m12,
                        self.m21+other.m21, self.m22+other.m22)

    def __sub__(self, other):
        return Matrix22(self.m11-other.m11, self.m12-other.m12,
                        self.m21-other.m21, self.m22-other.m22)

    def __mul__(self, other):
        if type(other).__name__=='Matrix22':
            return Matrix22(self.m11*other.m11+self.m12*other.m21, self.m11*other.m12+self.m12*other.m22,
                            self.m21*other.m11+self.m22*other.m21, self.m21*other.m12+self.m22*other.m22)
        elif type(other).__name__=='Vector2D':
            return Vector2D(self.m11*other.x+self.m12*other.y, self.m21*other.x+self.m22*other.y)
        elif type(other).__name__=='int' or type(other).__name__=='float':
            return Matrix22(other*self.m11, other*self.m12,
                            other*self.m21, other*self.m22)

    def __rmul__(self, other):
        if type(other).__name__=='int' or type(other).__name__=='float':
            return self*other

    def __truediv__(self, other):
        return self*(1/other)

    def __neg__(self, other):
        return -1*self

    def __pow__(self, other):
        if type(other).__name__=='int':
            x=copy.deepcopy(self)
            for p in range(other-1):
                x=x*self
            return x

    def __abs__(self):
        return self.m11*self.m22-self.m12*self.m21

    def __inv__(self):
        return (1/self.__abs__())*Matrix22(self.m22, -self.m12, -self.m21, self.m11)
