import random

# Lire les points de données depuis data.txt
with open("data.txt", "r") as f:
    points = [list(map(float, line.strip().split(','))) for line in f]

# Nombre de clusters
K = 3

# Choisir K points aléatoires comme centroïdes
centroids = random.sample(points, K)

# Écrire les centroïdes dans centroids.txt
with open("centroids.txt", "w") as f:
    for i, centroid in enumerate(centroids):
        f.write(f"{i}\t{','.join(map(str, centroid))}\n")

