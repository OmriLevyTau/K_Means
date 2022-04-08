from typing import List
from Vector import Vector

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
    def get_data(name: str):
        data = []
        with open(name, "r") as file:
            for line in file:
                tmp = []
                for elem in line.strip().split(","):
                    tmp.append(float(elem))
                data.append(tmp)
        return data
