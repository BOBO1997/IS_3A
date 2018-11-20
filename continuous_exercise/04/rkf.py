import math
import numpy as np
import matplotlib.pyplot as plt

class ORG:
	def __init__(self, num, r):
		self.num = num
		self.range = r

	def f(self, x):
		return - math.exp(- x) / 2 + 2 * math.exp(- 2 * x) / 5 + 3 * math.sin(x) / 10 + math.cos(x) / 10

	def __call__(self):
		x_list = np.linspace(0, self.range, self.num)
		y_list = []
		for x in x_list:
			y = self.f(x)
			y_list.append(y)
		return x_list, y_list

class RKF:
	def __init__(self, alpha, error, h, max_iter, x, y1, y2):
		self.h = h
		self.max_iter = max_iter
		self.x = x
		self.y1 = y1
		self.y2 = y2
		self.alpha = alpha
		self.error = error

	def fy1(self, y2):
		return y2

	def fy2(self, x, y1, y2):
		return - 3 * y2 - 2 * y1 + math.cos(x)

	def rkf_test(self, h):
		a1 = self.fy1(self.y2)
		a2 = self.fy2(self.x, self.y1, self.y2)

		b1 = self.fy1(self.y2 + a2 / 4)
		b2 = self.fy2(self.x + h / 4, 
					  self.y1 + a1 / 4, 
					  self.y2 + a2 / 4)

		c1 = self.fy1(self.y2 + 3 * a2 / 32 + 9 * a2 / 32)
		c2 = self.fy2(self.x + 3 * h / 8,
					  self.y1 + 3 * a1 / 32 + 9 * a1 / 32,
					  self.y2 + 3 * a2 / 32 + 9 * a2 / 32)

		d1 = self.fy1(self.y2 + 1932 * a2 / 2197 - 7200 * b2 / 2197 + 7296 * c2 / 2197)
		d2 = self.fy2(self.x + 12 * h / 13,
					  self.y1 + 1932 * a1 / 2197 - 7200 * b1 / 2197 + 7296 * c1 / 2197,
					  self.y2 + 1932 * a2 / 2197 - 7200 * b2 / 2197 + 7296 * c2 / 2197)

		e1 = self.fy1(self.y2 + 439 * a2 / 216 - 8 * b2 + 3680 * c2 / 513 - 845 * d2 / 4104)
		e2 = self.fy2(self.x + h,
					  self.y1 + 439 * a1 / 216 - 8 * b1 + 3680 * c1 / 513 - 845 * d1 / 4104,
					  self.y2 + 439 * a2 / 216 - 8 * b2 + 3680 * c2 / 513 - 845 * d2 / 4104)

		f1 = self.fy1(self.y2 - 8 * a1 / 27 + 2 * b2 - 3544 * c2 / 2565 + 1859 * d2 / 4104 - 11 * e2 / 40)
		f2 = self.fy2(self.x + h / 2,
					  self.y2 - 8 * a1 / 27 + 2 * b1 - 3544 * c1 / 2565 + 1859 * d1 / 4104 - 11 * e1 / 40,
					  self.y2 - 8 * a2 / 27 + 2 * b2 - 3544 * c2 / 2565 + 1859 * d2 / 4104 - 11 * e2 / 40)
		rkf4y1 = self.y1 + h * (25 * a1 / 216 + 1408 * c1 / 2565 + 2197 * d1 / 4104 - e1 / 5)
		rkf5y1 = self.y1 + h * (16 * a1 / 135 + 6656 * c1 / 12825 + 28561 * d1 / 56430 - 9 * e1 / 50 - 2 * f1 / 55)
		rkf4y2 = self.y2 + h * (25 * a2 / 216 + 1408 * c2 / 2565 + 2197 * d2 / 4104 - e2 / 5)
		rkf5y2 = self.y2 + h * (16 * a2 / 135 + 6656 * c2 / 12825 + 28561 * d2 / 56430 - 9 * e2 / 50 - 2 * f2 / 55)
		return rkf4y1, rkf5y1, rkf4y2, rkf5y2

	def rkf_step(self):
		R = 1
		h = self.h
		pre_h = h
		iters = 0
		while R >= self.error:
			y1, rkf5y1, y2, rkf5y2 = self.rkf_test(h)
			R1 = abs(rkf5y1 - y1)
			R2 = abs(rkf5y2 - y2)
			R = max(R1, R2)
			pre_h = h
			h = self.alpha * h * math.pow(self.error / R, 1.0 / 4.0)
			iters += 1
			if iters > self.max_iter:
				break
		self.x = self.x + pre_h
		self.y1 = y1
		self.y2 = y2
		return pre_h, self.x, self.y1

	def __call__(self):
		h_list = []
		x_list = []
		y_list = []
		for i in range(self.max_iter):
			h, x, y = self.rkf_step()
			h_list.append(h)
			x_list.append(x)
			y_list.append(y)
		return h_list, x_list, y_list

if __name__ == "__main__":
	h_list, x_list, y_list = RKF(0.8, 0.0001, 0.1, 10000, 0, 0, 0)()
	x_org, y_org = ORG(10000, 40)()
	plt.plot(x_list, y_list)
	plt.plot(x_org, y_org)
	plt.title("Runge-Kutta-Fehlberg Method")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.savefig("rkf.png")
	plt.clf()
	plt.title("Runge-Kutta-Fehlberg Method")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.plot(h_list)
	plt.savefig("h.png")
