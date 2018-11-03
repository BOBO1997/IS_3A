import numpy as np
import random
import math
import matplotlib.pyplot as plt

def f(x, y):
	return 3 * x ** 2 + 2 * y ** 2

def diff(x, y):
	return 6 * x, 4 * y

def gradf(x, y):
	return 6 * x, 4 * y

def vec_abs(v):
	v1, v2 = v
	return v1 ** 2 + v2 ** 2

def barrier(f, diff, a, b, x, y, threshold, max_iter):
	x_list = [x]
	y_list = [y]
	e = 1.0
	for _ in range(max_iter):
		d = diff(x, y)
		dx, dy = d
		# ステップ幅の更新(バックトラック法)
		for _ in range(max_iter):
			if f(x - e * dx, y - e * dy) - f(x, y) > - a * e * vec_abs(d):
				e = b * e
		x = x - e * dx
		y = y - e * dy
		x_list.append(x)
		y_list.append(y)
		if x < threshold and y < threshold / 10:
			break
	return x_list, y_list

if __name__ == '__main__':
	a = 0.5
	b = 0.8
	threshold = 0.01
	max_iter = 10000
	
	# 等高線の実装
	levels = []
	for i in range(20):
		levels.append(1 * (i + 1))
	x = np.linspace(-5, 5, 100)
	y = np.linspace(-5, 5, 100)
	X, Y = np.meshgrid(x, y)
	Z = np.sqrt(3 * X ** 2 + 2 * Y ** 2)
	plt.contour(X, Y, Z, levels = levels)

	x_init, y_init = 4, 4
	x_list, y_list = barrier(f, diff, a, b, x_init, y_init, threshold, max_iter)
	plt.scatter(x_list, y_list, s = 2, c = 'orange', zorder = 3)
	plt.plot(x_list, y_list, zorder = 2)
	
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("Backtracking Line Search")
	plt.gca().set_aspect('equal')
	plt.savefig("backtracking.png")
