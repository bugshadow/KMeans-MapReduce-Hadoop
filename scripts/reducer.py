#!/usr/bin/env python3
import sys

current_key = None
points = []

for line in sys.stdin:
    key, point_str = line.strip().split('\t')
    point = list(map(float, point_str.split(',')))
    key = int(key)
    
    if key != current_key:
        if current_key is not None:
            avg = [sum(dim)/len(points) for dim in zip(*points)]
            print(f"{current_key}\t{','.join(map(str, avg))}")
            points = []
        current_key = key
    points.append(point)

if current_key is not None:
    avg = [sum(dim)/len(points) for dim in zip(*points)]
    print(f"{current_key}\t{','.join(map(str, avg))}")
