import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class CG:
	def __init__(self, A, b, error = 0.001):
		assert A.shape[0] == b.shape[0]
		self.A = A
		self.x = np.random.rand(A.shape[1], 1)
		self.b = np.reshape(b, (b.shape[0], 1))
		self.b_origin = self.b.copy()
		self.b_norm = np.linalg.norm(self.b)
		self.r = self.b - self.A @ self.x
		self.p = self.r.copy()
		self.y = self.b.copy()
		self.alpha = 0
		self.beta = 0
		self.error = error
		self.errors = np.array([])
		self.solve_flag = 0

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
	
	def make_error_graph(self):
		iters = self.errors.shape[0]
		plt.yscale("log")
		plt.grid(which = "both")
		plt.plot(np.linspace(1, iters, iters), self.errors)
		plt.scatter(np.linspace(1, iters, iters), self.errors)
		plt.xlabel("iters")
		plt.ylabel("error")
		plt.savefig("errors.png")
		plt.clf()

	def cg(self):
		max_iter = 10000
		for i in range(max_iter):
			self.y = self.A @ self.p
			self.alpha = np.linalg.norm(self.r) ** 2 / (self.p.T @ self.y)[0, 0]
			self.x = self.x + self.alpha * self.p
			r = self.r.copy()
			self.r = self.r - self.alpha * self.y
			self.beta = (np.linalg.norm(self.r) / np.linalg.norm(r)) ** 2
			self.p = self.r + self.beta * self.p
			self.errors = np.append(self.errors, np.linalg.norm(self.r))
			if np.linalg.norm(self.A @ self.x - self.b) / self.b_norm < self.error:
				print("steps : ", i)
				break

	def solve(self):
		if self.solve_flag == 0:
			self.cg()
			self.make_error_graph()
			self.solve_flag = 1
		return self.x

	def __call__(self):
		if self.solve_flag == 0:
			self.cg()
			self.make_error_graph()
			self.solve_flag = 1
		print("x = ")
		print(self.x)
		self.correct()

class Poisson:
	def __init__(self, size, u, f):
		self.size = size
		self.num = size - 1
		self.cells = self.num * self.num
		self.range = np.linspace(0, self.num - 1, self.num)

		self.u = u
		self.f = f
		
		I = np.eye(self.num)
		O = np.ones((self.num, self.num))
		U = np.triu(O, k = 1) - np.triu(O, k = 2)
		L = np.triu(O, k = -1) - np.triu(O, k = 0)
		B = U + L
		self.A = - 4 * np.kron(I, I) + np.kron(B, I) + np.kron(I, B)
		self.b = np.reshape(self.calc_b(), self.cells)

	def calc_b(self):
		b = np.zeros((self.num, self.num))
		for i, x in enumerate(self.range):
			for j, y in enumerate(self.range):
				b[i, j] = self.f(x, y)
		return b

	def calc_u(self):
		u = np.zeros((self.num, self.num))
		for i, x in enumerate(self.range):
			for j, y in enumerate(self.range):
				u[i, j] = self.u(x, y)
		return u

	def plot(self, values, name):
		plt.pcolor(self.range, self.range, values)
		plt.gca().set_aspect('equal', adjustable='box')
		plt.colorbar()
		plt.savefig("%s.png" %(name))
		plt.clf()

	def plot3d(self, values, name):
		x_range, y_range = np.meshgrid(self.range, self.range)  # 上述のサンプリング点(x,y)を使ったメッシュ生成
		fig = plt.figure() #プロット領域の作成
		ax = fig.gca(projection='3d') #プロット中の軸の取得。gca は"Get Current Axes" の略。
		ax.plot_wireframe(x_range, y_range, values, color='blue',linewidth=0.3)
		plt.savefig("%s3d.png" %(name))
		plt.clf()

	def __call__(self):
		print(self.A)
		print(self.b)
		cg = CG(self.A, self.b)
		result = cg.solve()
		result = np.reshape(result, (self.num, self.num))
		print(result)
		self.plot(result, "poisson")
		self.plot3d(result, "poisson")

def u(x, y):
	return x * (x - 1) * y * (y - 1)

def f(x, y):
	return 2 * (x * (x - 1) + y * (y - 1))

if __name__ == "__main__":
	#T = np.full((10, 10), 0.2)
	#B = np.eye(10) + np.triu(T, k = 1) - np.triu(T, k = 2) + np.triu(T, k = -1) - np.triu(T, k = 0)
	#b = np.array([1,2,3,4,5,6,7,8,9,10])
	#print(B)
	#CG(B, b, error = 0.000000000001)()
	size = 5
	Poisson(size, u, f)()
