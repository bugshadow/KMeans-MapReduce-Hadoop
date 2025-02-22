<div align="center">

# 🌟 KMeans avec MapReduce sous Hadoop

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=36BCF7FF&center=true&vCenter=true&random=false&width=600&lines=K-means+Clustering+avec+MapReduce;Big+Data+Processing;Distributed+Computing)](https://git.io/typing-svg)

<p align="center">
  <img src="https://img.shields.io/badge/Apache-Hadoop-%2300B4FF?style=for-the-badge&logo=apache-hadoop&logoColor=white" alt="Hadoop"/>
  <img src="https://img.shields.io/badge/Python-3.x-%233776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/MapReduce-Framework-%2300B4FF?style=for-the-badge&logoColor=white" alt="MapReduce"/>
</p>

![K-Means Clustering](https://upload.wikimedia.org/wikipedia/commons/e/ea/K-means_convergence.gif)


</div>

---

<div align="center">

## 🎯 Description

</div>

> Ce projet implémente l'algorithme **K-means** en utilisant **MapReduce** sous **Hadoop** avec Python. Il est conçu pour traiter de grandes quantités de données en distribuant le calcul sur un cluster Hadoop.

### 🔍 Fonctionnalités Principales

- ⚡ **Initialisation des centroïdes** : Les centroïdes initiaux sont définis ou générés aléatoirement
- 🔄 **Itérations MapReduce** : Les points sont assignés aux clusters (Map) et les centroïdes sont recalculés (Reduce)
- ✨ **Convergence** : L'algorithme s'arrête lorsque les centroïdes convergent
- 📊 **Résultats** : Les centroïdes finaux sont affichés et stockés dans HDFS

---

<div align="center">

## 📁 Structure du Projet

</div>

```bash
KMeans-MapReduce-Hadoop/
├── 📂 data/                  # Fichiers de données
├── 📂 scripts/               # Scripts Python
│   ├── 📜 mapper.py         # Script de mapping
│   ├── 📜 reducer.py        # Script de reduction
│   └── 📜 driver.py         # Script principal
├── 📂 output/               # Résultats des itérations
│   └── 📂 iter_0/           # Dossier pour chaque itération
├── 📝 README.md             # Documentation
└── 📋 requirements.txt      # Dépendances
```

---

<div align="center">

## ⚙️ Utilisation

</div>

### 📋 Prérequis

- ![Hadoop](https://img.shields.io/badge/Hadoop-Installed-%23FF7F0E?style=flat-square&logo=apache-hadoop)
- ![Python](https://img.shields.io/badge/Python-3.x-%233776AB?style=flat-square&logo=python)
- ![YARN](https://img.shields.io/badge/YARN-Running-%23E8E8E8?style=flat-square&logo=apache)

### 🚀 Étapes d'exécution

#### 1️⃣ Placer les fichiers dans HDFS

```bash
hdfs dfs -mkdir -p /input
hdfs dfs -put data/data.txt /input/
hdfs dfs -put data/centroids.txt /input/
```

#### 2️⃣ Rendre les scripts exécutables

```bash
chmod +x scripts/mapper.py scripts/reducer.py scripts/driver.py
```

#### 3️⃣ Exécuter le script principal

```bash
python3 scripts/driver.py
```

#### 4️⃣ Vérifier les résultats

```bash
# Liste des répertoires de sortie
hdfs dfs -ls /output

# Afficher les résultats
hdfs dfs -cat /output/iter_0/part-00000
```

---

<div align="center">

## 💻 Génération des Données

</div>

### 📊 Générer data.txt

```python
import random

num_points = 100  # Nombre de points
dimensions = 2    # Dimensions (x, y)

with open("data/data.txt", "w") as f:
    for _ in range(num_points):
        point = [random.uniform(0, 10) for _ in range(dimensions)]
        f.write(",".join(map(str, point)) + "\n")
```

### 🎯 Générer centroids.txt

```python
import random

with open("data/data.txt", "r") as f:
    points = [list(map(float, line.strip().split(','))) for line in f]

K = 3  # Nombre de clusters
centroids = random.sample(points, K)

with open("data/centroids.txt", "w") as f:
    for i, centroid in enumerate(centroids):
        f.write(f"{i}\t{','.join(map(str, centroid))}\n")
```

---







<div align="center">

## 👨‍💻 Auteur

# Omar Bouhaddach

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=36BCF7FF&center=true&vCenter=true&random=false&width=600&lines=Bugs+Shadow;D%C3%A9veloppeur+principal)](https://git.io/typing-svg)



<p align="center">
  <a href="mailto:bouhaddachomar@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red" />
  </a>
  <a href="https://www.linkedin.com/in/omar-bouhaddach-7420a02b4/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/bugshadow" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=bugshadow&color=blueviolet&style=for-the-badge&label=PROFILE+VIEWS" />
</p>

### 🛠️ Languages & Tools

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,hadoop,docker,git,ubuntu" />
</div>


### 📊 GitHub Stats

![GitHub Stats](https://github-readme-streak-stats.herokuapp.com/?user=bugshadow&theme=tokyonight&hide_border=true)

</div>

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer"/>
</div>
