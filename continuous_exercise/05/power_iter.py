import numpy as np
#np.set_printoptions(3)

def normalize(v, axis=-1, order=2):
	l2 = np.linalg.norm(v, ord = order, axis=axis, keepdims=True)
	l2[l2 == 0] = 1
	return v / l2

def power_iter(A, size, max_iter):
	x = np.random.rand(size)
	x = normalize(x)
	x = np.reshape(x, (size, 1))
	for i in range(max_iter):
		x = A @ np.reshape(x, (size, 1))
		x = np.reshape(x, (1, size))
		x = normalize(x)
	lam = (x @ A @ x.T) / (x @ x.T)
	return lam, x

if __name__ == "__main__":
	size = 6
	max_iter = 1000
	H = np.eye(size)
	for i in range(size):
		for j in range(size):
			H[i, j] = 1 / (i + j + 1)
	print(H)
	lam, x = power_iter(H, size, max_iter)
	print("max lambda = ", lam[0, 0])
	print("eigenvector = ", x)
	lambdas, vectors = np.linalg.eig(H)
	print("lambdas via library = ", lambdas)
	print("vectors via library = \n", vectors)
