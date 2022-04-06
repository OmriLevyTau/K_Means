from typing import List
import numbers

class Vector:

    def __init__(self,v: List[numbers.Number]):
        self.vector = v
        self.n = len(v)

    def __getitem__(self, item):
        return self.vector[item]

    def __setitem__(self, key, value):
        self.vector[key] = value

    def __str__(self):
        return str(self.vector)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other,numbers.Number):
            other = self._broadcast(other)
        if not (self._agree_on_size(other)):
            raise ValueError("Must agree on size")
        result = self.copy()
        for i in range(self.n):
            result[i] += other[i]
        return result

    def __mul__(self, const):
        result = self.copy()
        for i in range(self.n):
            result[i] *= const
        return result

    def __sub__(self, other):
        if isinstance(other,numbers.Number):
            other = self._broadcast(-1*other)
        else:
            other *= -1
        return self.__add__(other)

    def copy(self):
        result = Vector.create_vector(self.n,value=0)
        for i in range(self.n):
            result[i] = self[i]
        return result

    def _broadcast(self,constant):
        return Vector.create_vector(self.n, value=constant)

    def _agree_on_size(self, other: 'Vector'):
        if self.n != other.n:
            return False
        return True

    @staticmethod
    def create_vector(length, value=0.0):
        return Vector([value for _ in range(length)])

    @staticmethod
    def dot(u: 'Vector',v: 'Vector'):
        if u.n != v.n:
            raise ValueError("Input is not 1d Vector")
        s = 0
        for i in range(u.n):
            s += u[i]*v[i]
        return s
    @staticmethod
    def norm(v):
        return Vector.dot(v,v)**0.5


