# DBSCAN (Density-based spatial clustering of applications with noise)

Analysis of Clustering Based on DBSCAN

### DBSCAN란?
>Density-based spatial clustering of applications with noise (DBSCAN) is a data clustering algorithm proposed by Martin Ester, Hans-Peter Kriegel, Jörg Sander and Xiaowei Xu in 1996.[1] It is a density-based clustering non-parametric algorithm: given a set of points in some space, it groups together points that are closely packed together (points with many nearby neighbors), marking as outliers points that lie alone in low-density regions (whose nearest neighbors are too far away). DBSCAN is one of the most common clustering algorithms and also most cited in scientific literature.
[WIKIPEDIA](https://en.wikipedia.org/wiki/DBSCAN)

## 설치 방법
- 실행 환경 (테스트 환경)
  - Windows 10 or Ubuntu Linux
  - Python3.x

## 사용 방법

- Input : example_of_input.csv 

`python3 DBSCAN.py`

- Output : example_of_output.csv

# Significant eps parameter settings in DBSCAN

DBSCAN 기반 클러스터링 분석에 있어서 input 데이터에 맞는 적절한 eps값 세팅을 결정하고 분석하기 위함

## DBSCAN Graph in Example Data

>![Pic1](https://github.com/Xenia101/DBSCAN/blob/master/pic/1.png)
>
>k=4 Graph

>![Pic2](https://github.com/Xenia101/DBSCAN/blob/master/pic/2.png)
>
>k=100 Graph
