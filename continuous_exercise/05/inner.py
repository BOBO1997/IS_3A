import numpy as np
np.set_printoptions(3)

class inner:
	def __init__(self, A, b):
		self.A = A
		self.A_orig = A
		self.size = A.shape[0]
		self.b = b
		self.L = np.zeros_like(A)
		self.U = np.zeros_like(A)
		self.P = np.eye(A.shape[0])

	def dump_all(self):
		print("P= \n", self.P)
		print("A = \n", self.A)
		print("L = \n", self.L)
		print("U = \n", self.U)
		print("LU = \n", self.L @ self.U)
		print("PA = \n", self.P @ self.A_orig)

	def lu_decomposition(self, focus = 0):
		if focus == self.A.shape[0] - 1:
			self.L[focus, focus], self.U[focus, focus] = 1, self.A[focus, focus]
		else:
			pivot = focus
			for i in range(focus, self.size):
				if abs(self.A[pivot, focus]) < abs(self.A[i, focus]):
					pivot = i
			P = np.eye(self.size)
			P[focus, focus], P[pivot, pivot] = 0, 0
			P[focus, pivot], P[pivot, focus] = 1, 1
			self.P, self.A, self.L = P @ self.P, P @ self.A, P @ self.L

			An = self.A[focus + 1:, focus + 1:]
			a11 = self.A[focus, focus]
			al = self.A[focus + 1:, focus]
			ac = self.A[focus, focus + 1:]
			self.U[focus, focus] = a11
			self.L[focus, focus] = 1
			l = al / a11
			self.L[focus + 1:, focus] = l
			self.U[focus, focus + 1:] = ac
			self.A[focus + 1:, focus + 1:] = An - np.reshape(l, (l.shape[0], 1)) @ np.reshape(ac, (1,  ac.shape[0]))
			self.lu_decomposition(focus + 1)

	def solve(self):
		pivotted_b = self.P @ self.b
		return

	def __call__(self):
		self.lu_decomposition()
		print("\nprint result\n")
		self.dump_all()

if __name__ == "__main__":
	size = 6
	b = np.zeros(size)
	A = np.zeros((size, size), dtype = float)
	for i in range(size):
		for j in range(size):
			A[i, j] = 1 / (i + j + 1)
	print(A)
	inner(A, b)()
	T = np.full((10, 10), 0.2)
	B = np.eye(10) + np.triu(T, k = 1) - np.triu(T, k = 2) + np.triu(T, k = -1) - np.triu(T, k = 0)
	print(B)
	inner(B, b)()
	C = np.array([[8,72,32],[1,11,18],[5,54,86]], dtype = float)
	print(C)
	inner(C, b)()
