import time
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class OptCG:
	def __init__(self, num, b, h, error = 0.00000000001):
		self.num = num
		self.h = h
		self.x = np.random.rand(num ** 2, 1)
		self.b = np.reshape(b, (b.shape[0], 1))
		self.b_origin = self.b.copy()
		self.b_norm = np.linalg.norm(self.b)
		self.r = self.b - self.calc_matrix(self.x)
		self.p = self.r.copy()
		self.y = self.b.copy()
		self.alpha = 0
		self.beta = 0
		self.error = error
		self.errors = np.array([])
		self.solve_flag = 0

	def dumpall(self):
		print("x = \n", self.x)
		print("b = \n", self.b)
		print("r = \n", self.r)
		print("p = \n", self.p)
		print("y = \n", self.y)
		print("alpha = \n", self.alpha)
		print("beta = \n", self.beta)
		print("error = \n", self.error)
	
	def calc_matrix(self, vector):
		ret = np.zeros(vector.shape)
		for i, v in enumerate(vector):
			if i < self.num:
				if i % self.num == 0:
					ret[i] = vector[i + self.num] + vector[i + 1] - 4 * vector[i]
				elif (i + 1) % self.num == 0:
					ret[i] = vector[i + self.num] + vector[i - 1] - 4 * vector[i]
				else:
					ret[i] = vector[i + self.num] + vector[i - 1] + vector[i + 1] - 4 * vector[i]
			elif i >= self.num ** 2 - self.num:
				if i % self.num == 0:
					ret[i] = vector[i - self.num] + vector[i + 1] - 4 * vector[i]
				elif (i + 1) % self.num == 0:
					ret[i] = vector[i - self.num] + vector[i - 1] - 4 * vector[i]
				else:
					ret[i] = vector[i - self.num] + vector[i - 1] + vector[i + 1] - 4 * vector[i]
			else:
				if i % self.num == 0:
					ret[i] = vector[i - self.num] + vector[i + self.num] + vector[i + 1] - 4 * vector[i]
				elif (i + 1) % self.num == 0:
					ret[i] = vector[i - self.num] + vector[i + self.num] + vector[i - 1] - 4 * vector[i]
				else:
					ret[i] = vector[i - self.num] + vector[i + self.num] + vector[i - 1] + vector[i + 1] - 4 * vector[i]
		ret = np.reshape(ret, vector.shape)
		assert ret.shape == vector.shape
		return ret / self.h ** 2
			
	def make_error_graph(self):
		iters = self.errors.shape[0]
		plt.yscale("log")
		plt.grid(which = "both")
		plt.plot(np.linspace(1, iters, iters), self.errors)
		plt.scatter(np.linspace(1, iters, iters), self.errors, c = "r", s = 10)
		plt.xlabel("iters")
		plt.ylabel("error")
		plt.savefig("opt_errors.png")
		plt.clf()

	def cg(self):
		max_iter = 10000
		t1 = time.time()
		for i in range(max_iter):
			self.y = self.calc_matrix(self.p)
			self.alpha = np.linalg.norm(self.r) ** 2 / (self.p.T @ self.y)[0, 0]
			self.x = self.x + self.alpha * self.p
			r = self.r.copy()
			self.r = self.r - self.alpha * self.y
			self.beta = (np.linalg.norm(self.r) / np.linalg.norm(r)) ** 2
			self.p = self.r + self.beta * self.p
			self.errors = np.append(self.errors, np.linalg.norm(self.r))
			if np.linalg.norm(self.calc_matrix(self.x) - self.b) / self.b_norm < self.error:
				print("steps : ", i)
				break
		t2 = time.time()
		print("time = ", t2 - t1)

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
		x_range, y_range = np.meshgrid(self.range, self.range) #サンプリング点(x,y)を使ったメッシュ生成
		fig = plt.figure() #プロット領域の作成
		ax = fig.gca(projection='3d') #プロット中の軸の取得。gca は"Get Current Axes" の略。
		ax.plot_wireframe(x_range, y_range, values, color='blue',linewidth=0.3)
		#ax.plot_surface(x_range, y_range, result, rstride=1, cstride=1, cmap='hsv', linewidth=0.3)
		plt.savefig("%s3d.png" %(name))
		plt.clf()
		
	def __call__(self):
		x = np.zeros(self.cells)
		b = np.reshape(self.calc_b(), self.cells)
		print(b)
		
		result = OptCG(self.num, b, self.h).solve() # ここのxは端っこは含まれていない
		#result = CG(A / self.h ** 2, b).correct(0) # ここのxは端っこは含まれていない
		result = np.reshape(result, (self.num, self.num))
		self.plot(result, "optcg_poisson")
		self.plot3d(result, "optcg_poisson")
		print("diff = ", self.diffsum(result, self.calc_u()))
		diff = self.diffmap(result, self.calc_u())
		#self.plot(diff, "diff")
		#self.plot3d(diff, "diff")
		
def f(x, y):
	return 2 * (x * (x - 1) + y * (y - 1))

def u(x, y):
	return x * (x - 1) * y * (y - 1)

if __name__ == "__main__":
	size, num = 1, 51
	result = Poisson(size, num, f, u)()
