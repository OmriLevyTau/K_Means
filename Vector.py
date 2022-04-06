from typing import List
import numbers

class Vector:

    def __init__(self,v: List[numbers.Number]):
        self.vector = v
        self.n = len(v)

    def __getitem__(self, item)->numbers.Number:
        return self.vector[item]

    def __setitem__(self, key, value):
        self.vector[key] = value

    def __str__(self)->str:
        return str(self.vector)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other)->'Vector':
        if isinstance(other,numbers.Number):
            other = self._broadcast(other)
        if not (self._agree_on_size(other)):
            raise ValueError("Must agree on size")
        result = self.copy()
        for i in range(self.n):
            result[i] += other[i]
        return result

    def __mul__(self, const)->'Vector':
        result = self.copy()
        for i in range(self.n):
            result[i] *= const
        return result

    def __sub__(self, other)->'Vector':
        if isinstance(other,numbers.Number):
            other = self._broadcast(-1*other)
        else:
            other *= -1
        return self.__add__(other)


    def __truediv__(self, other):
        result = self.copy()
        if isinstance(other,numbers.Number):
            other = self._broadcast(other)
        for i in range(self.n):
            result[i] /= other[i]
        return result

    def copy(self)->'Vector':
        result = Vector.create_vector(self.n,value=0)
        for i in range(self.n):
            result[i] = self[i]
        return result

    def argmin(self)->int:
        arg = 0
        min = self[0]
        for i in range(self.n):
            if self[i]<min:
                arg = i
        return arg

    def _broadcast(self, constant)->'Vector':
        return Vector.create_vector(self.n, value=constant)

    def _agree_on_size(self, other: 'Vector')->bool:
        if self.n != other.n:
            return False
        return True

    @staticmethod
    def create_vector(length: int, value=0.0)->'Vector':
        return Vector([value for _ in range(length)])

    @staticmethod
    def dot(u: 'Vector',v: 'Vector')->float:
        if u.n != v.n:
            raise ValueError("Input is not 1d Vector")
        s = 0
        for i in range(u.n):
            s += u[i]*v[i]
        return s

    @staticmethod
    def sqaured_norm(v: 'Vector')->float:
        return Vector.dot(v,v)**0.5

