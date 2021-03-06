import csv
import dispy
import numpy
from scipy.cluster.vq import kmeans, vq

### OWN CODE ###
def distance(a, b):
    from math import sqrt
    sum = 0.0
    for i in (a-b):
        sum += (i*i)
    return sqrt(sum)

def compute(centroids, dataset):
    import numpy
    idx = 0
    min_dist = float('inf')
    for i in range(len(centroids)):
        dist = distance(dataset, centroids[i])
        if dist < min_dist:
            min_dist = dist
            idx = i
    return idx

def load_csv(file):
    temp1 = []
    with open(file) as f:
        reader = f.readlines()
        size = len(reader)
        for row in xrange(size):
            temp = []
            t = reader[row].split('\r')
            d = t[0].split(',')
            for i in xrange(len(d)):
                c = float(d[i])
                temp.append(c)
            temp1.append(temp)
    dataset = numpy.array(temp1)
    print "number of dataset", len(dataset)
    return dataset
### OWN CODE ###

if __name__ == '__main__':
    dataset = load_csv("../dataset/kddcup.newtestdata_10_percent_unlabeled.csv")
    datasize = len(dataset)
    centroids,_ = kmeans(dataset, 4)

    result = []
    for i in range(len(centroids)):
        result.append([])
        result[i] = []

    for i in range(datasize):
        c = compute(centroids, dataset[i])
        print('dataset %s: cluster %s' % (i, c))
        result[int(c)].append(i)

    for i in range(len(centroids)):
        print "Anggota klaster ke:", i
        print result[i]
