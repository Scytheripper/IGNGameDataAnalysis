import csv

file = open("ign_20_editors.csv", 'r')

reader = csv.reader(file)
data = list(reader)
file.close()
file = open("ign_20_editors_num.csv", 'w',newline='')
writer = csv.writer(file)
scores = []
platforms = []
count = 0
#for le in data:
#   if le[1] in scores:
#        x = 12
#   else:
#       scores.append(le[1])
#print(scores)
#for le in data:
#    le.append(scores.index(le[1]))
#    writer.writerow(le)
for le in data:
    if le[3] in platforms:
        x = 1
    else:
        platforms.append(le[3])
print(platforms)
for le in data:
    le.append(platforms.index(le[3]))
    #writer.writerow(le)
print(platforms.__len__())
file.close