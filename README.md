# DBSCAN (Density-based spatial clustering of applications with noise)

Analysis of Clustering Based on DBSCAN

### DBSCAN란?
>Density-based spatial clustering of applications with noise (DBSCAN) is a data clustering algorithm proposed by Martin Ester, Hans-Peter Kriegel, Jörg Sander and Xiaowei Xu in 1996.[1] It is a density-based clustering non-parametric algorithm: given a set of points in some space, it groups together points that are closely packed together (points with many nearby neighbors), marking as outliers points that lie alone in low-density regions (whose nearest neighbors are too far away). DBSCAN is one of the most common clustering algorithms and also most cited in scientific literature.
[WIKIPEDIA](https://en.wikipedia.org/wiki/DBSCAN)

## Example
```python
from sklearn.cluster import DBSCAN
import numpy as np

clustering = DBSCAN(eps=eps, min_samples=min_samples, metric='euclidean').fit(X)
```

## Execution / Test Environment
  - Windows 10 or Ubuntu Linux
  - Python 3.x

## Usage

- Input : ```example_of_input.csv```

  `python3 DBSCAN.py`

- Output : ```example_of_output.csv```

# Significant eps parameter settings in DBSCAN

DBSCAN 기반 클러스터링 분석에 있어서 input 데이터에 맞는 적절한 eps값 세팅을 결정하고 분석하기 위함

## DBSCAN Graph in Example Data

```python
#Example
total_node = np.array(total_node, dtype=np.float64)
nbrs = NearestNeighbors(n_neighbors=ns).fit(total_node)
distances, indices = nbrs.kneighbors(total_node)
distanceDec = sorted(distances[:,ns-1], reverse=False)

plt.plot(list(range(1,len(total_node)+1)), distanceDec)
plt.show()
```
- Graph with k=4

![Pic1](https://github.com/Xenia101/DBSCAN/blob/master/pic/1.png)

- Graph with k=100

![Pic2](https://github.com/Xenia101/DBSCAN/blob/master/pic/2.png)
