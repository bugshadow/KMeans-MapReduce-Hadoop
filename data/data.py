import random

# Nombre de points de données
num_points = 30

# Dimensions des points (par exemple 2 dimensions : x, y)
dimensions = 2

with open("data.txt", "w") as f:
    for _ in range(num_points):
        point = [random.uniform(0, 10) for _ in range(dimensions)]
        f.write(",".join(map(str, point)) + "\n")

