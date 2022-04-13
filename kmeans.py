from typing import List
import numbers
import sys

class Vector:

    def __init__(self,v: List[numbers.Number]):
        self.vector = v
        self.n = len(v)

    ######################
    ## Instance Methods ##
    ######################

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
        arg_min = 0
        min = self[0]
        for i in range(self.n):
            if self[i]<min:
                arg_min = i
                min = self[i]
        return arg_min

    def _broadcast(self, constant)->'Vector':
        return Vector.create_vector(self.n, value=constant)

    def _agree_on_size(self, other: 'Vector')->bool:
        if self.n != other.n:
            return False
        return True
    ######################
    ### Static Methods ###
    ######################

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
        return Vector.dot(v,v)

class KMeans:

    def __init__(self, k, max_iter=200):
        self.k = k
        self.max_iter = max_iter
        self.epsilon = 0.001

    def fit(self, data: List[List[float]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        self.centroids = [Vector(c) for c in self.data[:self.k].copy()]

    def train(self):
        point_clusters = Vector.create_vector(self.rows, value=None)
        for iter in range(self.max_iter):
            # assign each point to closest cluster
            for i in range(self.rows):
                min_dist = float('inf')
                argmin = -1
                for j in range(self.k):
                    center = self.centroids[j]
                    dist_point_center = Vector.sqaured_norm(Vector(self.data[i]) - center)
                    if dist_point_center<min_dist:
                        min_dist = dist_point_center
                        argmin = j
                point_clusters[i] = argmin

            # calculate new centroids
            old_centroids = self.centroids.copy()
            cluster_sum = [Vector.create_vector(self.cols, value=0) for _ in range(self.k)]
            cluster_count = Vector.create_vector(self.k, value=0)
            for i in range(self.rows):
                idx = point_clusters[i]
                cluster_count[idx] += 1
                cluster_sum[idx] += Vector(self.data[i])
            centroids_change = Vector.create_vector(self.k, 0)
            counter = 0
            for i in range(self.k):
                self.centroids[i] = cluster_sum[i] / cluster_count[i]
                centroids_change[i] = Vector.sqaured_norm(self.centroids[i] - old_centroids[i]) ** 0.5
                if centroids_change[i] <= self.epsilon:
                    counter += 1
            # Check if changes<=epsilon
            if counter == self.k:
                break

        return self.centroids

    @staticmethod
    def get_input(name: str):
        data = []
        with open(name, "r") as file:
            for line in file:
                tmp = []
                for elem in line.strip().split(","):
                    tmp.append(float(elem))
                data.append(tmp)
        return data

    @staticmethod
    def write_output(centroids: List['Vector'], output_filename: str):
        with open(output_filename, "w") as file:
            for centroid in centroids:
                centroid_data =  KMeans.make_string(centroid.vector)
                file.writelines(centroid_data)
                file.write("\n")

    @staticmethod
    def make_string(centroid: List['float']):
        st=""
        for cell in centroid:
            tmp = "%.4f"%round(cell,4)
            st = st + tmp + ","
        return st[:len(st)-1]

    @ staticmethod
    def validate_input_args(argv: List[str])->bool:
        n = len(argv)

        if (n!=5 and n!=4):
            return True

        k = argv[1]
        if n==5:
            max_iter = argv[2]
        else:
            max_iter = "200"

        try:
            k, max_iter = float(k), float(max_iter)
        except:
            return True

        if k!=int(k) or max_iter!=int(max_iter) or k<=1 or max_iter<1:
            return True

        return False

if __name__=="__main__":
    argv = sys.argv

    if KMeans.validate_input_args(argv):
        print("Invalid Input!")

    try:
        if len(argv)==5:
            k, max_iter, input_name, output_name = int(argv[1]), int(argv[2]), argv[3], argv[4]
        else:
            k, max_iter, input_name, output_name = int(argv[1]), 200, argv[2], argv[3]

        classifier = KMeans(k)
        data = KMeans.get_input(input_name)
        classifier.fit(data)
        centroids = classifier.train()
        KMeans.write_output(centroids, output_name)
    except:
        print("An Error Has Occurred")



