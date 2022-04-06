from typing import List
from Vector import Vector


class KMeans:

    def __init__(self,k,max_iter=200):
        self.k = k
        self.max_iter = max_iter
        self.epsilon = 0.001

    def fit(self,data:List[List[float]]):
        self.data = data
        self.rows = len(data)
        self.centroids = [Vector(c) for c in self.data[:self.k].copy()]

    def train(self):
        point_clusters = Vector.create_vector(self.rows,value=0)
        for iter in range(self.max_iter):

            # assign each point to closest cluster
            for i in range(self.rows):
                point = Vector(self.data[i])
                dist_point_center = Vector.create_vector(self.k,value=0)
                for j in range(self.k):
                    center = self.centroids[j]
                    dist_point_center[j] = Vector.sqaured_norm(point-center)
                point_clusters[i] = dist_point_center.argmin()

            # calculate new centroids
            old_centroids = self.centroids.copy()
            cluster_sum = self.centroids.copy()
            cluster_count = Vector.create_vector(self.k, value=1)
            for i in range(self.rows):
                idx = point_clusters[i]
                cluster_count[idx] += 1
                cluster_sum[idx] += Vector(self.data[i])
            centeroids_change = Vector.create_vector(self.k,0)
            counter = 0
            for i in range(self.k):
                self.centroids[i] = cluster_sum[i]/cluster_count[i]
                centeroids_change[i] = Vector.sqaured_norm(self.centroids[i]-old_centroids[i])**0.5
                if centeroids_change[i]<=self.epsilon:
                    counter+=1
            # Check if changes<=epsilon
            if counter==self.k:
                print(iter)
                return self.centroids

        return self.centroids





