import pandas as pd 
from sklearn.cluster import k_means
from scipy.spatial import distance

# nc is number of clusters
# to be implemented without the use of any libraries (from the scratch)

def find_s(i, x, labels, clusters):
	s = 0
	for x in clusters:
		s += distance.euclidean(x, clusters[i])
	return s

def find_Rij(i, j, x, labels, clusters, nc):
	Rij = 0
	try:
		d = distance.euclidean(clusters[i],clusters[j])
		Rij = (find_s(i, x, labels, clusters) + find_s(j, x, labels, clusters))/d
	except:
		Rij = 0	
	return Rij

def find_R(i, x, labels, clusters, nc): 
	list_r = []
	for i in range(nc):
		for j in range(nc):
			if(i!=j):
				temp = find_Rij(i, j, x, labels, clusters, nc)
				list_r.append(temp)

	return max(list_r)

def find_DB_index(x, labels, clusters, nc):
	sigma_R = 0.0
	for i in range(nc):
		sigma_R = sigma_R + find_R(i, x, labels, clusters, nc)

	DB_index = float(sigma_R)/float(nc)
	return DB_index

def main():
	df = pd.read_csv("Dataset_Assignment_1.csv")
	df = df.dropna()
	x1 = df.copy()
	del x1['Customer']
	del x1['Effective To Date']
	x4 = pd.get_dummies(x1)
	n = 10
	clf = k_means(x4, n_clusters = n)
	centroids = clf[0] 
	# 10 clusters
	labels = clf[1]
	index_db_val = find_DB_index(x4, labels, centroids, n)
	print ("The value of Davies Bouldin index for a K-Means cluser of size " + str(n) + " is: " + str(index_db_val))


if __name__ == "__main__":
	main()
