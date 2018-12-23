import numpy as np

class CG:
	def __init__(self, A, b, error = 0.001):
		self.A = A
		self.x = np.random.rand(A.shape[1], 1)
		self.b = np.reshape(b, (b.shape[0], 1))
		self.b_origin = self.b.copy()
		self.r = self.b - self.A @ self.x
		self.p = self.r.copy()
		self.y = self.b.copy()
		self.alpha = 0
		self.beta = 0
		self.error = error

	def dumpall(self):
		print("A = \n", self.A)
		print("x = \n", self.x)
		print("b = \n", self.b)
		print("r = \n", self.r)
		print("p = \n", self.p)
		print("y = \n", self.y)
		print("alpha = \n", self.alpha)
		print("beta = \n", self.beta)
		print("error = \n", self.error)
	
	def correct(self):
		print("correct answer = ")
		print(np.linalg.solve(self.A, self.b_origin))

	def cg(self):
		max_iter = 1000
		for i in range(max_iter):
			#print("\n\n\nloop = ", i)
			#self.dumpall()
			self.y = self.A @ self.p
			self.alpha = (self.r.T @ self.r)[0, 0] / (self.p.T @ self.y)[0, 0]
			self.x = self.x + self.alpha * self.p
			r = self.r.copy()
			self.r = self.r - self.alpha * self.y
			self.beta = (self.r.T @ self.r)[0, 0] / (r.T @ r)[0, 0]
			self.p = self.r + self.beta * self.p
			if (self.r.T @ self.r)[0, 0] < self.error:
				break

	def __call__(self):
		self.cg()
		print("x = \n", self.x)
		self.correct()

if __name__ == "__main__":
	A = np.array([[1,2,3],[4,5,6],[7,8,9]])
	b = np.array([10,11,12])
	CG(A, b, error = 0.000001)()
	T = np.full((10, 10), 0.2)
	B = np.eye(10) + np.triu(T, k = 1) - np.triu(T, k = 2) + np.triu(T, k = -1) - np.triu(T, k = 0)
	b = np.array([1,2,3,4,5,6,7,8,9,10])
	print(B)
	CG(B, b, error = 0.000000001)()
