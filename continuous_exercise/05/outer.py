import numpy as np
np.set_printoptions(precision = 3)

class outer:
	def __init__(self, A):
		self.size = A.shape[0]
		self.L = np.eye(self.size)
		self.U = A
		self.A_org = A

	def decompose(self, col):
		if col == self.size - 1:
			return
		else:
			for i in range(self.size - col - 1):
				self.L[i + col + 1, col] = self.U[i + col + 1, col] / self.U[col, col]
				self.U[i + col + 1, col:] = self.U[i + col + 1, col:] - self.L[i + col + 1, col] * self.U[col, col:]
			#print("L = \n", self.L)
			#print("U = \n", self.U)
			self.decompose(col + 1)

	def __call__(self):
		self.decompose(0)
		print("L = \n", self.L)
		print("U = \n", self.U)
		print("LU = \n", self.L @ self.U)

if __name__ == "__main__":
	T = np.full((10, 10), 0.2)
	B = np.eye(10) + np.triu(T, k = 1) - np.triu(T, k = 2) + np.triu(T, k = -1) - np.triu(T, k = 0)
	print("B = \n", B)
	outer(B)()
	A = np.array([[8,72,32],[1,11,18],[5,54,86]], dtype = float)
	print("A = \n", A)
	outer(A)()
