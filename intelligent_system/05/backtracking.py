import numpy as np
import random
import math
import matplotlib.pyplot as plt

def f(x, y):
	return 10 * x ** 2 + y ** 2

def diff(x, y):
	return 20 * x, 2 * y

def vec_abs(v):
	v1, v2 = v
	return v1 ** 2 + v2 ** 2

def backtracking(f, diff, a, b, x, y, threshold, max_iter):
	x_list = [x]
	y_list = [y]
	for _ in range(max_iter):
		e = 1.0
		d = diff(x, y)
		dx, dy = d
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
	levels = []
	for i in range(20):
		levels.append(1 * (i + 1))
	a = 0.5
	b = 0.8
	threshold = 0.01
	max_iter = 10000
	x_init = random.uniform(-5.0, 5.0)
	y_init = random.uniform(-5.0, 5.0)
	# x_init, y_init = 4, 2
	x_list, y_list = backtracking(f, diff, a, b, x_init, y_init, threshold, max_iter)
	x = np.linspace(-5, 5, 100)
	y = np.linspace(-5, 5, 100)
	X, Y = np.meshgrid(x, y)
	plt.scatter(x_list, y_list, s = 5, c = 'orange')
	Z = np.sqrt(10 * X ** 2 + Y ** 2)
	plt.plot(x_list, y_list)
	plt.contour(X, Y, Z, levels = levels)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("Backtracking Line Search")
	plt.gca().set_aspect('equal')
	plt.savefig("backtracking.png")
