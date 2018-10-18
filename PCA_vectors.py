import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
import csv 

def doPCA(data):
            pca = PCA(n_components=2)
            pca.fit(data)
            return pca
            
fname = "ign_20_editors_num_2.csv"
data = np.genfromtxt(fname, delimiter=',')
data = np.delete(data,[0,1,3,4,5,7],1)
pca = doPCA(data)
data_transformed = pca.transform(data)
comp_1 = pca.components_[0]
comp_2 = pca.components_[1]
file = open("data_pca.csv",'w')
fieldnames = ["x","y","color"]
writer = csv.DictWriter(file, fieldnames=fieldnames,lineterminator='\n')
#create the points to plot 
writer.writeheader()
for ii,jj in zip(data_transformed,data):
    writer.writerow({"x":comp_1[0]*ii[0],"y":comp_1[1]*ii[0],"color":"r"})
    writer.writerow({"x":comp_2[0]*ii[1],"y":comp_2[1]*ii[1],"color":"c"})
    writer.writerow({"x":ii[0],"y":ii[1],"color":"b"})