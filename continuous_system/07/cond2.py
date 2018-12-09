import numpy as np

if __name__ == "__main__":
	for size in [3,6,9]:
		H = np.zeros((size, size), dtype = float)
		for i in range(size):
			for j in range(size):
				H[i, j] = 1 / (i + j + 1)
		eigs, _ = np.linalg.eig(H)
		print(np.abs(eigs.max()) / np.abs(eigs.min()))
