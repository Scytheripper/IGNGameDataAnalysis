import numpy as np
from random import randrange

fname = "ign_20_editors_num_2.csv"
data = np.genfromtxt(fname, delimiter=',')
sample_data = []
for x in range (0,500):
    index = randrange(0,data.__len__())
    sample_data.append(data[index])
distanceMatrix = np.zeros((sample_data.__len__(), sample_data.__len__()))
for i in range(0,sample_data.__len__()):
    for ii in range(i,sample_data.__len__()):
        distanceMatrix[i][ii] = np.linalg.norm(data[i]-data[ii])
np.savetxt('euclidian.txt', distanceMatrix,'%5.5f',delimiter=',')
print("done")