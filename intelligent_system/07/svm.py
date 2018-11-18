import math
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_data(n):
	p_data, n_data = np.array([[], []]), np.array([[], []])
	for i in range(n):
		a = 4 * (float(i) / float(n - 1))
		px1 = a * math.cos(a) + np.random.rand()
		px2 = a * math.sin(a) + np.random.rand()
		nx1 = (a + math.pi) * math.cos(a) + np.random.rand()
		nx2 = (a + math.pi) * math.sin(a) + np.random.rand()
		p_data = np.append(p_data, [[px1], [px2]], axis = 1)
		n_data = np.append(n_data, [[nx1], [nx2]], axis = 1)
	return p_data, n_data

def kernel(xi, xj, h = 0.3):
    return np.exp(- np.sum((xi - xj) ** 2) / (2 * h ** 2))

def create_k_matrix(n, data):
	K = np.zeros((n, n), dtype = float)
	for i in range(n):
		for j in range(n):
			K[i, j] = kernel(data[:, i], data[:, j])
	return K

def culc_theta_kernel(x, theta, data):
	sum_theta_kernel = 0
	for i in range(len(data)):
		sum_theta_kernel += theta[i] * kernel(x, data[:, i])
	return sum_theta_kernel

def svm(n, max_iters, e, b, c, threshold, p_data, n_data):
	px1, px2 = p_data
	print(p_data.shape)
	nx1, nx2 = n_data
	data = np.concatenate((p_data, n_data), axis = 1)
	print(data.shape)
	label = np.concatenate((np.ones(n // 2), np.full(n // 2, -1)))
	theta = np.zeros(n)
	K = create_k_matrix(n, data)
	for iters in range(max_iters):
		for i in range(n):
			d = np.zeros(n)
			if 1 - culc_theta_kernel(n, theta, data) * label[i] > 0:
				for j in range(n):
					d[j] += - label[i] * kernel(data[:, i], data[:, j])
		theta = theta - e * (e * d + 2 * np.dot(K, theta))
		e *= b
		print("theta = \n{}".format(theta))
		print("iter %d finished" %(iters))
	
	values = np.array([])
	plot = np.zeros((2, 0))
	axis_range = np.linspace(-6, 6, 100)
	for i in axis_range:
		for j in axis_range:
			value = abs(culc_theta_kernel(np.array([i, j]), theta, data))
			print(i, j, value)
			values = np.append(values, value)
			if value < threshold:
				plot = np.concatenate((plot, np.array([[i], [j]])), axis = 1)
		print("iter %d finished" %(i))
	print(plot.shape)
	values = np.reshape(values, (100, 100))
	# 等高線の実装
	levels = []
	for i in range(20):
		levels.append(1 * (i + 1))
	'''
	x = np.linspace(-6, 6, 100)
	y = np.linspace(-6, 6, 100)
	X, Y = np.meshgrid(x, y)
	print(X.shape)
	print(type(X))
	print(X)
	Z = culc_theta_kernel(np.array([X, Y]), theta, data)
	#Z = X ** 2 + Y ** 2
	#print(Z.shape)
	'''
	plt.contour(axis_range, axis_range, values, levels = levels)
	
	return plot

if __name__ == "__main__":
	n = 100
	max_iters = 100
	e = 0.5
	b = 0.8
	c = 1
	threshold = 0.01
	p_data, n_data = generate_data(n)
	x1_plot, x2_plot = svm(n * 2, max_iters, e, b, c, threshold, p_data, n_data)
	px1, px2 = p_data
	nx1, nx2 = n_data
	plt.scatter(px1, px2, s = 3, c = "r")
	plt.scatter(nx1, nx2, s = 3, c = "b")
	#plt.scatter(x1_plot, x2_plot, s = 3, c = "g")
	#plt.plot(x1_plot, x2_plot, color = "g", linewidth = 0.5)
	plt.title("svm")
	plt.xlim(-7, 5)
	plt.ylim(-6, 6)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.savefig("svm.png")
