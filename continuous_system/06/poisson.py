import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class SOR:
	def __init__(self, A, x, b, omega, iters):
		self.A = A # 不変
		self.x = x # 更新値
		self.b = b # 不変
		self.omega = omega # 不変
		self.iters = iters

	def step(self):
		for i in range(self.x.shape[0]):
			if i == 0:
				self.x[i] = self.x[i] + self.omega * (self.b[i] - np.dot(self.A[i, :], self.x[:])) / self.A[i, i]
			else:
				self.x[i] = self.x[i] + self.omega * (self.b[i] - np.dot(self.A[i, :i], self.x[:i]) - np.dot(self.A[i, i:], self.x[i:])) / self.A[i, i]

	def __call__(self):
		for k in range(self.iters):
			self.step()
		return self.x

class Poisson:
	def __init__(self, size, num):
		self.size = size
		self.num = num - 1 # 内部の点の個数
		self.cells = self.num * self.num
		self.h = size / num
		self.range = np.linspace(0, size, self.num)

	def __call__(self):
		I = np.eye(self.num)
		O = np.ones((self.num, self.num))
		U = np.triu(O, k = 1) - np.triu(O, k = 2)
		L = np.triu(O, k = -1) - np.triu(O, k = 0)
		B = U + L
		A = - 4 * np.kron(I, I) + np.kron(B, I) + np.kron(I, B)
		print(self.h)
		print(A)
		print(A.shape)
		x = np.zeros(self.cells)
		print(x)
		print(x.shape)
		b = np.concatenate((np.full(self.cells // 2, -1), np.full(self.cells - self.cells // 2, 1)))
		# b = np.full(self.cells, -1)
		print(b)
		print(b.shape)
		result = SOR(A / self.h ** 2, x, b, 1.95, 100)() # ここのxは端っこは含まれていない
		result = np.reshape(result, (self.num, self.num))

		plt.contourf(self.range, self.range, result)
		plt.colorbar()
		plt.savefig("poisson.png")
		plt.clf()
		fig = plt.figure() #プロット領域の作成
		ax = fig.gca(projection='3d') #プロット中の軸の取得。gca は"Get Current Axes" の略。
		ax.plot_wireframe(self.range, self.range, result, color='blue',linewidth=0.3)
		#ax.plot_surface(x_range, y_range, result, rstride=1, cstride=1, cmap='hsv', linewidth=0.3)
		plt.savefig("poisson3d.png")
		
if __name__ == "__main__":
	size, num = 1, 101
	result = Poisson(size, num)()
