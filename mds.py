from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA
import numpy as np
import csv

fname = "ign_20_editors_num_2.csv"
data = np.genfromtxt(fname, delimiter=',')
data = np.delete(data,[0],1)
data = data-(data.mean())
lol = euclidean_distances(data)
file = open("data_mds.csv",'w')
writer = csv.DictWriter(file, fieldnames=fieldnames,lineterminator='\n')
fieldnames = ["x","y"]
mds = manifold.MDS(n_components=2, max_iter=100, eps=1e-9,
                   dissimilarity="precomputed", n_jobs=1)

data_mds = mds.fit(lol).embedding_

for row in data_mds: 
     writer.writerow({"x":row[0],"y":row[1]})
     
print("done")
