import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
import csv
import pandas as pd
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import make_pipeline

data = []
with open('INPUT/example_of_Input.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        data.append(row)

edit_data = []

for x in range(1,139): # 1~139
    data[x][1:] = [float(i) for i in data[x][1:]]
    edit_data.append(data[x][1:])

X = np.array(edit_data)
print('> INPUT')
print(X)
print('\n')

# DBSCAN
eps = 1.2 
min_samples = 2

db=DBSCAN(eps=eps, min_samples=min_samples, metric='euclidean')
y_db = db.fit_predict(X)

print("Number of Data : {0}\n".format(len(db.labels_)))
print("params : eps = {0}, min_samples = {1}\n". format(eps,min_samples))
print('※ cluster labels : -1 is noise point\n')
print('> OUTPUT')
print(db.labels_)

print('\nnumber of clusters : ', end='')
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print(n_clusters_)

f=open('OUTPUT/example_of_output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
output=[]
for x in db.labels_:
    output.append(x)
for x in output:
    wr.writerow([x])
f.close()


