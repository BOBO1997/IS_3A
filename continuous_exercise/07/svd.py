import numpy as np
np.set_printoptions(precision = 3)

if __name__ == "__main__":
	'''
	A = np.array([[1,2,3,4,5,6],
				  [1,3,5,7,9,11],
				  [12,10,8,6,4,2],
				  [5,4,6,3,7,2],
				  [5,6,4,7,3,8],
				  [6,5,4,3,2,1]])
	'''
	A = np.array([[8.79,  6.11, -9.15,  9.57, -3.49,  9.84],
				  [9.93,  6.91, -7.93,  1.64,  4.02,  0.15],
				  [9.83,  5.04,  4.86,  8.83,  9.80, -8.99],
				  [5.45, -0.27,  4.85,  0.74, 10.00, -6.02],
				  [3.16,  7.98,  3.01,  5.80,  4.27, -5.31]])
	A = A.T
	print("A = ")
	print(A)
	U, s, V = np.linalg.svd(A, full_matrices=True)
	S = np.concatenate((np.diag(s), np.array([[0,0,0,0,0]])))
	print("U = ")
	print(U)
	print("S = ")
	print(S)
	print("V = ")
	print(V)
