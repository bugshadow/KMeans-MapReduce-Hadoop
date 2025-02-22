#!/usr/bin/env python3
import os
import subprocess
import numpy as np

# Configuration
K = 3  # Nombre de clusters
MAX_ITERATIONS = 10
THRESHOLD = 0.01
HDFS_INPUT = "/input/data.txt"  # Fichier d'entrée dans HDFS
HDFS_OUTPUT_TEMPLATE = "/output/iter_{}"  # Répertoire de sortie dans HDFS

# Centroïdes initiaux (stockés dans une liste Python)
INITIAL_CENTROIDS = [
    [1.0, 2.0],  # Cluster 0
    [4.0, 5.0],  # Cluster 1
    [7.0, 8.0],  # Cluster 2
]

def hdfs_cat(hdfs_path):
    """Lit un fichier depuis HDFS et retourne son contenu sous forme de lignes."""
    cmd = f"hdfs dfs -cat {hdfs_path}"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return proc.stdout.read().decode('utf-8').splitlines()

def hdfs_put(local_path, hdfs_path):
    """Place un fichier local dans HDFS."""
    subprocess.run(f"hdfs dfs -rm -f {hdfs_path}", shell=True, stderr=subprocess.DEVNULL)
    subprocess.run(f"hdfs dfs -put {local_path} {hdfs_path}", shell=True, check=True)

def save_centroids_to_file(centroids, filename):
    """Sauvegarde les centroïdes dans un fichier local."""
    with open(filename, "w") as f:
        for i, centroid in enumerate(centroids):
            f.write(f"{i}\t{','.join(map(str, centroid))}\n")

def load_centroids_from_file(filename):
    """Charge les centroïdes depuis un fichier local."""
    centroids = {}
    with open(filename, "r") as f:
        for line in f:
            key, centroid = line.strip().split('\t')
            centroids[int(key)] = list(map(float, centroid.split(',')))
    return centroids

def compute_convergence(old_centroids, new_centroids):
    """Vérifie si les centroïdes ont convergé."""
    if not old_centroids:
        return False
    max_diff = max(
        np.linalg.norm(np.array(old_centroids[k]) - np.array(new_centroids.get(k, old_centroids[k])))
        for k in old_centroids
    )
    return max_diff < THRESHOLD

def main():
    # Initialiser les centroïdes
    centroids = INITIAL_CENTROIDS
    save_centroids_to_file(centroids, "centroids.txt")
    hdfs_put("centroids.txt", "/input/centroids.txt")

    old_centroids = {i: centroid for i, centroid in enumerate(centroids)}

    # Boucle d'itération
    for i in range(MAX_ITERATIONS):
        output_dir = HDFS_OUTPUT_TEMPLATE.format(i)
        subprocess.run(f"hdfs dfs -rm -r {output_dir}", shell=True, stderr=subprocess.DEVNULL)

        # Commande Hadoop Streaming
        cmd = (
            f"hadoop jar /home/omar/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar "
            f"-files centroids.txt,mapper.py,reducer.py "
            f"-mapper 'python3 mapper.py' "
            f"-reducer 'python3 reducer.py' "
            f"-input {HDFS_INPUT} "
            f"-output {output_dir} "
        )
        subprocess.run(cmd, shell=True, check=True)

        # Charger les nouveaux centroïdes
        new_centroids = load_centroids_from_file("centroids.txt")

        # Vérifier la convergence
        if compute_convergence(old_centroids, new_centroids):
            print("Convergence atteinte!")
            break

        # Mettre à jour les centroïdes
        save_centroids_to_file(list(new_centroids.values()), "centroids.txt")
        hdfs_put("centroids.txt", "/input/centroids.txt")
        old_centroids = new_centroids.copy()

    # Afficher les centroïdes finaux
    print("Centroïdes finaux:")
    for k, centroid in old_centroids.items():
        print(f"Cluster {k}: {centroid}")

if __name__ == "__main__":
    main()
