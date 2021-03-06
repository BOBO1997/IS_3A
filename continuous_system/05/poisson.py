import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class SOR:
	def __init__(self, A, x, b, omega, error, iters):
		self.A = A # 不変
		self.x = x # 更新値
		self.b = b # 不変
		self.omega = omega # 不変
		self.error = error
		self.iters = iters

	def step(self):
		for i in range(self.x.shape[0]):
			if i == 0:
				self.x[i] = self.x[i] + self.omega * (self.b[i] - self.A[i, :] @ self.x[:]) / self.A[i, i]
			else:
				self.x[i] = self.x[i] + self.omega * (self.b[i] - self.A[i, :i] @ self.x[:i] - self.A[i, i:] @ self.x[i:]) / self.A[i, i]

	def calc_relative_error(self):
		error = np.linalg.norm(self.b - self.A @ self.x) / np.linalg.norm(self.b)
		print(error)
		return error

	def __call__(self):
		for k in range(self.iters):
			if self.calc_relative_error() >= self.error:
				self.step()
			else:
				break
			print(k)
		return self.x

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
		print(self.h)
		print(A.shape)
		x = np.zeros(self.cells)
		print(x.shape)
		b = np.reshape(self.calc_b(), self.cells)
		print(b.shape)
		result = SOR(A / self.h ** 2, x, b, 1.95, 0.00000000001, 1000)() # ここのxは端っこは含まれていない
		result = np.reshape(result, (self.num, self.num))
		print("diff = ", self.diffsum(result, self.calc_u()))
		diff = self.diffmap(result, self.calc_u())
		
		self.plot(result, "poisson")
		self.plot(diff, "diff")
		self.plot3d(result, "poisson")
		self.plot3d(diff, "diff")
		
def f(x, y):
	return 2 * (x * (x - 1) + y * (y - 1))

def u(x, y):
	return x * (x - 1) * y * (y - 1)

if __name__ == "__main__":
	size, num = 1, 101
	result = Poisson(size, num, f, u)()
