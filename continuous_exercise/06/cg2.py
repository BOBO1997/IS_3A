import time
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class CG:
	def __init__(self, A, b, error = 0.00000000001):
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
	
	def correct(self, print_flag):
		ans = np.linalg.solve(self.A, self.b_origin)
		if print_flag == 1:
			print("correct answer = ")
			print(ans)
			return None
		else:
			return ans
	
	def make_error_graph(self):
		iters = self.errors.shape[0]
		plt.yscale("log")
		plt.grid(which = "both")
		plt.plot(np.linspace(1, iters, iters), self.errors)
		plt.scatter(np.linspace(1, iters, iters), self.errors, c = "r", s = 10)
		plt.xlabel("iters")
		plt.ylabel("error")
		plt.savefig("errors.png")
		plt.clf()

	def cg(self):
		max_iter = 10000
		step = 0
		t1 = time.time()
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
				step = i + 1
				break
		t2 = time.time()
		print("time = ", t2 - t1)
		return i

	def solve(self):
		if self.solve_flag == 0:
			step = self.cg()
			self.make_error_graph()
			self.solve_flag = 1
		return self.x, step

	def __call__(self):
		if self.solve_flag == 0:
			self.cg()
			self.make_error_graph()
			self.solve_flag = 1
		print("x = ")
		print(self.x)
		self.correct(1)

class Poisson:
	def __init__(self, size, num, f, u):
		self.size = size
		self.num = num - 1 # 内部の点の個数
		self.cells = self.num * self.num
		self.h = size / num
		self.range = np.linspace(0, size, self.num)
		self.f = f
		self.u = u

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

	def diffsum(self, result, u):
		return np.sum((result - u) ** 2) / 2

	def diffmap(self, result, u):
		return result - u

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
		#ax.plot_surface(x_range, y_range, result, rstride=1, cstride=1, cmap='hsv', linewidth=0.3)
		plt.savefig("%s3d.png" %(name))
		plt.clf()
		
	def __call__(self):
		I = np.eye(self.num)
		O = np.ones((self.num, self.num))
		U = np.triu(O, k = 1) - np.triu(O, k = 2)
		L = np.triu(O, k = -1) - np.triu(O, k = 0)
		B = U + L
		A = - 4 * np.kron(I, I) + np.kron(B, I) + np.kron(I, B)
		#print(A)
		x = np.zeros(self.cells)
		b = np.reshape(self.calc_b(), self.cells)
		#print(b)
		
		result, step = CG(A / self.h ** 2, b).solve() # ここのxは端っこは含まれていない
		#result = CG(A / self.h ** 2, b).correct(0) # ここのxは端っこは含まれていない
		result = np.reshape(result, (self.num, self.num))
		self.plot(result, "cg_poisson")
		self.plot3d(result, "cg_poisson")
		print("diff = ", self.diffsum(result, self.calc_u()))
		diff = self.diffmap(result, self.calc_u())
		#self.plot(diff, "diff")
		#self.plot3d(diff, "diff")
		return step
		
def f(x, y):
	return 2 * (x * (x - 1) + y * (y - 1))

def u(x, y):
	return x * (x - 1) * y * (y - 1)

if __name__ == "__main__":
	steps = []
	size_range = [11,21,31,41,51]
	for i in size_range:
		size, num = 1, i
		step = Poisson(size, num, f, u)()
		steps.append(step)
	plt.xlabel("size")
	plt.ylabel("steps")
	plt.plot(size_range, steps)
	plt.scatter(size_range, steps)
	plt.savefig("steps.png")
	plt.clf()
