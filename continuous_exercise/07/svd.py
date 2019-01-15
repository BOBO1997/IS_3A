import numpy as np
np.set_printoptions(precision = 3)

if __name__ == "__main__":
	A = np.array([[1,2,3,4,5,6],
				  [1,3,5,7,9,11],
				  [12,10,8,6,4,2],
				  [5,4,6,3,7,2],
				  [5,6,4,7,3,8],
				  [6,5,4,3,2,1]])
	print("A = ")
	print(A)
	U, s, V = np.linalg.svd(A, full_matrices=True)
	S = np.diag(s)
	print("U = ")
	print(U)
	print("S = ")
	print(S)
	print("V = ")
	print(V)
