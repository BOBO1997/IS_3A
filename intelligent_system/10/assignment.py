import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn import datasets

if __name__ == "__main__":
	iris = datasets.load_iris()

	pca = PCA(n_components = 2)
	dim_2 = pca.fit_transform(iris.data)
	plt.scatter(dim_2[:, 0], dim_2[:, 1])
	plt.title("PCA")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.savefig("pca.png")
	plt.clf()
	
	clusters = KMeans(n_clusters = 3).fit(dim_2)
	red, green, blue = np.zeros((0, 2)), np.zeros((0, 2)), np.zeros((0, 2))
	for i, label in enumerate(clusters):
		if label == 0:
			red = np.append(red, np.expand_dims(dim_2[i, :], axis = 0))
		elif label == 1:
			green = np.append(green, np.expand_dims(dim_2[i, :], axis = 0))
		else:
			blue = np.append(blue, np.expand_dims(dim_2[i, :], axis = 0))
	red = np.reshape(red, (red.shape[0] // 2, 2))
	green = np.reshape(green, (green.shape[0] // 2, 2))
	blue = np.reshape(blue, (blue.shape[0] // 2, 2))
	plt.scatter(red[:, 0], red[:, 1], c = "r")
	plt.scatter(green[:, 0], green[:, 1], c = "g")
	plt.scatter(blue[:, 0], blue[:, 1], c = "b")
	plt.title("k-means clustering (k = 3)")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.savefig("kmeans.png")
	plt.clf()
