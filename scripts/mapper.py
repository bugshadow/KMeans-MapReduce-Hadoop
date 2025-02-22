#!/usr/bin/env python3
import sys

def load_centroids(centroid_file='centroids.txt'):
    centroids = []
    with open(centroid_file, 'r') as f:
        for line in f:
            key, centroid = line.strip().split('\t')
            centroids.append(list(map(float, centroid.split(','))))
    return centroids

def closest_centroid(point, centroids):
    min_dist_sq = float('inf')
    closest = -1
    for i, centroid in enumerate(centroids):
        dist_sq = sum((p - c)**2 for p, c in zip(point, centroid))
        if dist_sq < min_dist_sq:
            min_dist_sq = dist_sq
            closest = i
    return closest

centroids = load_centroids()

for line in sys.stdin:
    point = list(map(float, line.strip().split(',')))
    c = closest_centroid(point, centroids)
    print(f"{c}\t{','.join(map(str, point))}")
