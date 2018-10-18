from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA
import numpy as np
import csv
import matplotlib.pyplot as plt

fname = "ign_20_editors_num_2.csv"
data = np.genfromtxt(fname, delimiter=',')
data = np.delete(data,[0],1)
corr_data = np.corrcoef(data.T)
X = 1-abs(corr_data)
file = open("data_mds_diss2.csv",'w')
fieldnames = ["x","y","attribute"]
writer = csv.DictWriter(file, fieldnames=fieldnames,lineterminator='\n')
mds = manifold.MDS(n_components=2, max_iter=100, eps=1e-9,
                   dissimilarity="precomputed", n_jobs=1)

data_mds = mds.fit(X).embedding_
attributes = ["score", "release_year","release_month","release_day","score_phrase","platform","genre"]
attrNum = 0
for row in data_mds: 
    writer.writerow({"x":row[0],"y":row[1],"attribute":attributes[attrNum]})
    attrNum += 1
    print(attrNum)
     
print("done")
