import math
import numpy as np
import matplotlib.pyplot as plt

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
				self.x[i] = self.x[i] + self.omega * (self.b[i] - np.sum(self.A[i, :] * self.x[:])) / self.A[i, i]
			else:
				self.x[i] = self.x[i] + self.omega * (self.b[i] - np.sum(self.A[i, :(i - 1)] * self.x[:(i - 1)]) - np.sum(self.A[i, i:] * self.x[i:])) / self.A[i, i]

	def __call__(self):
		for k in range(self.iters):
			self.step()
		return self.x

class Poisson(SOR):
	def __init__(self, size, num):
		self.size = size
		self.num = num - 1 # 内部の点の個数
		self.h = size / num

	def __call__(self):
		I = np.eye(self.num)
		O = np.ones((self.num, self.num))
		U = np.triu(O, k = 1) - np.triu(O, k = 2)
		L = np.triu(O, k = -1) - np.triu(O, k = 0)
		B = U + L
		A = - 4 * np.kron(I, I) + np.kron(B, I) + np.kron(I, B)
		x = np.zeros(self.num * self.num)
		b = np.concatenate((np.full(-0.5, self.num), np.full(0.5, self.num)))
		result = SOR(A, x, b, 1.95, 3)() # ここのxは端っこは含まれていない
		return np.reshape(result, (self.num, self.num))
		
if __name__ == "__main__":
	size = 1
	num = 100
	result = Poisson(size, num)()
	x_range = np.linspace(0, size, num)
	y_range = np.linspace(0, size, num)
	plt.contourf(y_range, x_range, result)
	plt.colorbar()
