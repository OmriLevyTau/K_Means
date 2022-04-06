from typing import List, Tuple
import numbers

class Matrix:

    def __init__(self, matrix: List[List[float]]):
        self.matrix = matrix
        if not(self._is_valid_matrix(matrix)):
            raise ValueError("Not a Valid matrix")
        self.shape = (len(self.matrix),len(self.matrix[0]))

######################
## Instance Methods ##
######################

    def __getitem__(self, item):
        return self.matrix[0][item]

    def __add__(self, other)->'Matrix':
        """ add matrices element wise, return new Matrix.
            add scalar and matrix using broadcasting """
        if isinstance(other,numbers.Number):
            other = self._broadcast(other)

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

    def __sub__(self, other)->'Matrix':
        """ subtract matrices element wise, return new Matrix
            subtract scalar and matrix using broadcasting"""
        if isinstance(other,numbers.Number):
            other = self._broadcast(other)
        if not (self._agree_on_size(other)):
            raise ValueError("Must agree on size")
        rows,cols = self.get_shape()[0],self.get_shape()[1]
        result = []
        for i in range(rows):
            tmp = []
            for j in range(cols):
                tmp.append(self.matrix[i][j]-other.matrix[i][j])
            result.append(tmp)
        return Matrix(result)

    def __mul__(self, constant: float)->'Matrix':
        """multiplies by a scalar, returns new Matrix"""
        rows,cols = self.get_shape()[0],self.get_shape()[1]
        result = []
        for i in range(rows):
            tmp = []
            for j in range(cols):
                tmp.append(self.matrix[i][j]*constant)
            result.append(tmp)
        return Matrix(result)


    def transpose(self)->'Matrix':
        rows,cols = self.get_shape()[0],self.get_shape()[1]
        result = Matrix.create_matrix((cols,rows))
        for j in range(cols):
            for i in range(rows):
                result[j][i] = self.matrix[i][j]
        return result

    def get_shape(self):
        return self.shape

    def copy(self):
        rows,cols = self.get_shape()[0],self.get_shape()[1]
        result = Matrix.create_matrix(shape=(rows,cols))
        for i in range(rows):
            for j in range(cols):
                result[i][j] = self.matrix[i][j]
        return result


    def __str__(self):
        return "\n".join([str(row) for row in self.matrix])

    def __repr__(self):
        return self.__str__()

    def _is_valid_matrix(self, matrix: List[List[float]])-> bool:
        """assures valid matrix. all rows are of the same length,
            converts 1-dim input to 1-dim Matrix
        """
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
        """check if matrices have same shape for element wise operations"""
        if (self.get_shape() == other.get_shape()):
            return True
        return False

    def _agree_on_size_dot(self,other: 'Matrix')->bool:
        """check if matrices have approporiate shape for matmul and dot"""
        if self.get_shape()[1] == other.get_shape()[0]:
            return True
        return False

    def _broadcast(self, value: numbers.Number):
        """ broadcast scalars to a matrix shape
            for adding and subtracting scalars"""
        rows, cols = self.get_shape()[0], self.get_shape()[1]
        return Matrix.create_matrix((rows,cols),value)


######################
### Class Methods ####
######################

    @staticmethod
    def create_matrix(shape: Tuple[int,int], value=0.0)->'Matrix':
        rows, cols = shape[0], shape[1]
        result = [[value]*cols for _ in range(rows)]
        return Matrix(result)

    @staticmethod
    def matmul(mat1:'Matrix', mat2: 'Matrix'):
        """"Matrix multiplication, return new Matrix"""
        if not mat1._agree_on_size_dot(mat2):
            raise ValueError("Matrices must agree on size")
        rows,cols = mat1.get_shape()[0], mat1.get_shape()[1]
        result = Matrix.create_matrix((mat1.get_shape()[0], mat2.get_shape()[1]))
        for i in range(rows):
            for k in range(mat2.get_shape()[1]):
                tmp_sum = 0
                for j in range(cols):
                    tmp_sum += mat1.matrix[i][j] * mat2.matrix[j][k]
                result[i][k] = tmp_sum
        return result

    @staticmethod
    def dot(vec1: 'Matrix', vec2: 'Matrix')->float:
        """" dot product of two vectors"""
        if vec1.get_shape()[0] != 1 or vec2.get_shape()[0]!=1:
            raise ValueError("Dot product between 1d vectors only")
        return Matrix.matmul(vec1,vec2.transpose()).matrix[0][0]

    @staticmethod
    def norm(vector)->float:
        if vector.get_shape()[0]!=1:
            raise ValueError("Input is not 1d Vector")
        return Matrix.dot(vector,vector)**0.5

    @staticmethod
    def argmin(vector):
        if vector.get_shape()[0]!=1:
            raise ValueError("Input is not 1d Vector")
        arg = 0
        min = vector[0]
        for i in range(vector.get_shape()[1]):
            if vector[i]<min:
                arg = i
        return arg

# class KMeans:
#
#     def __init__(self,k, max_iter=200):
#         self.k = k
#         self.max_iter = max_iter
#         self.epsilon = 0.001
#
#     def fit(self,data):
#         self.data = Matrix(data)
#         self.centroids = data.copy()[:self.k]
#         self.rows = self.data.get_shape()[0]
#         self.cols = self.data.get_shape()[1]
#
#     def train(self):
#         points_clusters = Matrix.create_matrix((1,self.rows), value=0)
#         for iter in range(self.max_iter):
#             # assign each point to closest cluster
#             for i in range(self.rows):
#                 point = Matrix(self.data[i])
#                 dist_point_center = Matrix.create_matrix((1,self.k),value=0)
#                 for j in range(self.k):
#                     center = Matrix(self.centroids[j])
#                     dist = Matrix.norm(point-center)**2
#                     dist_point_center[j] = dist
#                 points_clusters[i] = Matrix.argmin(dist_point_center)
#             # calculate new centroids
#             cluster_sum = Matrix.create_matrix((self.cols,self.k),value=0)
#             cluster_count = Matrix.create_matrix((1,self.k),value=0)
#             for i in range(self.rows):
#                 c = points_clusters[i]
#                 cluster_count[c] += 1
#                 u = Matrix(cluster_sum[c])
#                 v = Matrix(self.data[i])
#                 cluster_sum[c] += 0











