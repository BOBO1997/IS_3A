import numpy as np

class LU:
	def __init__(self, A, b):
		self.A = A
		self.A_org = A
		self.b = b
		self.L = np.eye(A.shape[0])
		self.U = np.zeros_like(A)
		self.P = np.zeros_like(A)

	def lu_decomposition(self, focus):
		if focus == self.A.shape[0] - 1:
			self.U[focus, focus] = self.A[focus, focus]
		else:
			An = self.A[focus + 1:, focus + 1:]
			a11 = self.A[focus, focus]
			al = self.A[focus + 1:, focus]
			ac = self.A[focus, focus + 1:]
			self.U[focus, focus] = a11
			l = al / a11
			self.L[focus + 1:, focus] = l
			self.U[focus, focus + 1:] = ac
			#print("l.T = \n", l.T)
			#print("ac = \n", ac)
			#print("l.T @ ac = \n", l.T @ ac)
			#print("A = \n", self.A)
			self.A[focus + 1:, focus + 1:] = An - l.T @ ac
			#print("A = \n", self.A)
			self.lu_decomposition(focus + 1)

	def solve(self):
		return

	def __call__(self):
		self.lu_decomposition(0)
		print("L = \n", self.L)
		print("U = \n", self.U)
		print("LU = \n", self.L @ self.U)
		return

if __name__ == "__main__":
	size = 6
	A = np.zeros((size, size), dtype = float)
	for i in range(size):
		for j in range(size):
			A[i, j] = 1 / (i + j + 1)
			A[j, i] = 1 / (i + j + 1)
	print(A)
	b = np.zeros(size)
	#LU(A, b)()
	LU(np.array([[8,72,32],[1,11,18],[5,54,86]], dtype = float), b)()
