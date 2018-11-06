import numpy as np
import random
import math
import matplotlib.pyplot as plt

def f(x, y):
	return 3 * x ** 2 + 2 * y ** 2

def grad_f(x, y):
	return np.array([6 * x, 4 * y])

def h(x, y):
	return 1 - (x + y)

def phi(x, y):
	return math.log(- h(x, y))

def grad_phi(x, y):
	return np.array([1 / (- h(x, y)), 1 / (- h(x, y))])

def vec_abs_2(v):
	v1, v2 = v
	return v1 ** 2 + v2 ** 2

def target_f(c, x, y):
	return f(x, y) - c * phi(x, y)

def is_in_h(x, y):
	if h(x, y) <= 0:
		return True
	else:
		return False

def barrier(x, y, threshold, max_iter):
	x_list = [x]
	y_list = [y]
	# バックトラック法のパラメタ
	a = 0.5
	b = 0.8
	c = 5.0
	# 内点法
	for _ in range(max_iter):
		# cの値で勾配法
		pre_x, pre_y = x, y
		for _ in range(max_iter):
			prex, prey = x, y
			e = 1.0
			grad = grad_f(x, y) - c * grad_phi(x, y)
			dx, dy = grad
			# ステップ幅の更新(バックトラック法)
			for _ in range(max_iter):
				if (not is_in_h(x - e * dx, y - e * dy)) or target_f(c, x - e * dx, y - e * dy) - target_f(c, x, y) > - a * e * vec_abs_2(grad):
					e = b * e
			x = x - e * dx
			y = y - e * dy
			print("after =", x, y)
			if abs(x - prex) < threshold and abs(y - prey) < threshold:
				break
		x_list.append(x)
		y_list.append(y)
		c /= 2
		if abs(x - pre_x) < threshold and abs(y - pre_y) < threshold:
			break
	return x_list, y_list

if __name__ == '__main__':
	threshold = 0.001
	max_iter = 100
	
	# 等高線の実装
	levels = []
	for i in range(20):
		levels.append(1 * (i + 1))
	x = np.linspace(-5, 5, 100)
	y = np.linspace(-5, 5, 100)
	X, Y = np.meshgrid(x, y)
	Z = np.sqrt(3 * X ** 2 + 2 * Y ** 2)
	plt.contour(X, Y, Z, levels = levels)

	lin_x = np.linspace(-4,5,5)
	lin_y = 1 - lin_x
	plt.plot(lin_x, lin_y, "-r", linewidth = 0.5)

	# 初期値
	x_init, y_init = 4, 3
	x_list, y_list = barrier(x_init, y_init, threshold, max_iter)
	plt.scatter(x_list, y_list, s = 0.5, c = 'orange', zorder = 3)
	plt.plot(x_list, y_list, zorder = 2, linewidth = 0.5)
	
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("Barrier Method")
	plt.gca().set_aspect('equal')
	plt.savefig("barrier.png")
