from typing import List

class Matrix:

    def __init__(self, matrix: List[List[float]]):
        self.matrix = matrix
        if not(self._is_valid_matrix(matrix)):
            raise ValueError("Not a Valid matrix")
        self.shape = (len(self.matrix),len(self.matrix[0]))

    def __add__(self, other: 'Matrix')->'Matrix':
        if not (self._agree_on_size(other)):
            raise ValueError("Must agree on size")
        rows,cols = self.get_shape()[0],self.get_shape()[1]
        result = []
        for i in range(rows):
            tmp = []
            for j in range(cols):
                tmp.append(self.matrix[i][j]+other.matrix[i][j])
            result.append(tmp)
        mat = Matrix(result)
        return mat

    def __sub__(self, other: 'Matrix')->'Matrix':
        if not (self._agree_on_size(other)):
            raise ValueError("Must agree on size")
        rows,cols = self.get_shape()[0],self.get_shape()[1]
        result = []
        for i in range(rows):
            tmp = []
            for j in range(cols):
                tmp.append(self.matrix[i][j]-other.matrix[i][j])
            result.append(tmp)
        mat = Matrix(result)
        return mat

    def __mul__(self, constant: float)->'Matrix':
        # multiplies by a scalar, returns new Matrix
        rows,cols = self.get_shape()[0],self.get_shape()[1]
        result = []
        for i in range(rows):
            tmp = []
            for j in range(cols):
                tmp.append(self.matrix[i][j]*constant)
            result.append(tmp)
        mat = Matrix(result)
        return mat

    def dot(self,other: 'Matrix'):
        if not self._agree_on_size_dot(other):
            raise ValueError("Matrices must agree on size")
        rows,cols = self.get_shape()[0],self.get_shape()[1]
        result = [[0]*other.get_shape()[1] for k in range(self.get_shape()[0])]
        for i in range(rows):
            for k in range(other.get_shape()[1]):
                tmp_sum = 0
                for j in range(cols):
                    tmp_sum += self.matrix[i][j]*other.matrix[j][k]
                result[i][k] = tmp_sum
        return Matrix(result)

    def transpose(self)->'Matrix':
        rows,cols = self.get_shape()[0],self.get_shape()[1]
        result = [[0]*rows for k in range(cols)]

        for j in range(cols):
            for i in range(rows):
                result[j][i] = self.matrix[i][j]

        return Matrix(result)

    def norm(self)->float:
        return (self.dot(self.transpose()).matrix[0][0])**0.5



    def __str__(self):
        return "\n".join([str(row) for row in self.matrix])

    def _is_valid_matrix(self, matrix: List[List[float]])-> bool:
        # assures valid matrix. all rows are of the same length
        # converts 1-dim input to 1-dim Matrix
        if not isinstance(matrix[0],list):
            matrix = [matrix]
            self.matrix = matrix

        n = len(matrix[0])
        for row in matrix:
            if len(row)!=n:
                return False
        self.matrix = matrix
        return True

    def _agree_on_size(self,other: 'Matrix')-> bool:
        if (self.get_shape() == other.get_shape()):
            return True
        return False

    def _agree_on_size_dot(self,other: 'Matrix')->bool:
        if self.get_shape()[1] == other.get_shape()[0]:
            return True
        return False

    def get_shape(self):
        return self.shape


# a = Matrix([[1,2],[3,4]])
# b = Matrix([[1,2],[3,4]])
# print((a))
# print(a+b)
# print()
# print(a*5)
m1 = Matrix([[1,2,3],[6,2,5]])
print(m1)
print()
print(m1.transpose())

# m2 = Matrix([[1,4,7,0],[2,5,8,0],[3,6,9,0]])
# print(m1)
# print()
# print(m2)
# print()
# print(m1.dot(m2))


print("\nVectors")
v = Matrix([1,1,1,1])
print(v)
print(v.norm())
# u = Matrix([[1],[2],[3]])
# print(v)
# print(v.transpose())
# print((u+v))
# print((v*3))
# print(v.dot(u))
