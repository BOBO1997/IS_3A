import math
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_data(n):
	p_data, n_data = np.array([[], []]), np.array([[], []])
	for i in range(n):
		a = 4 * math.pi * (float(i) / float(n - 1))
		px1 = a * math.cos(a) + np.random.rand()
		px2 = a * math.sin(a) + np.random.rand()
		nx1 = (a + math.pi) * math.cos(a) + np.random.rand()
		nx2 = (a + math.pi) * math.sin(a) + np.random.rand()
		p_data = np.append(p_data, [[px1], [px2]], axis = 1)
		n_data = np.append(n_data, [[nx1], [nx2]], axis = 1)
	return p_data, n_dat

def kernel(xi, xj, h = 0.5): # 2 * h ** 2 = 1
    return np.exp(- np.sum((xi - xj) ** 2) / (2 * h ** 2))

def create_k_matrix(n, data):
	K = np.zeros((n, n), dtype = float)
	for i in range(n):
		for j in range(n):
			K[i, j] = kernel(data[:, i], data[:, j])
	return K

def culc_theta_kernel(x, theta, data):
	sum_theta_kernel = 0
	for i in range(len(theta)):
		sum_theta_kernel += theta[i] * kernel(x, data[:, i])
	return sum_theta_kernel

def svm(n, max_iters, e, b, c, p_data, n_data):
	print(p_data.shape)
	print(p_data)
	print(n_data)
	data = np.concatenate((p_data, n_data), axis = 1)
	print(data)
	print(data.shape)
	label = np.concatenate((np.ones(n // 2), np.full(n // 2, -1)))
	theta = np.ones(n)
	K = create_k_matrix(n, data)
	for iters in range(max_iters):
		d = np.zeros(n)
		for i in range(n):
			if 1 - culc_theta_kernel(data[:, i], theta, data) * label[i] > 0:
				for j in range(n):
					d[j] += - label[i] * kernel(data[:, i], data[:, j])
		theta = theta - e * (c * d + 2 * theta @ K)
		e *= b
		print("theta = \n{}".format(theta))
		print("iter %d finished" %(iters))
	
	values = np.array([])
	x_range = np.linspace(-16, 16, 100)
	y_range = np.linspace(-16, 16, 100)
	for i in x_range:
		for j in y_range:
			value = culc_theta_kernel(np.array([i, j]), theta, data)
			values = np.append(values, value)
		print("iter %d finished" %(i))
	values = np.reshape(values, (100, 100)).T
	for i in range(n // 2):
		for j in range(n // 2):
			values[i, j] = 1 if values[i, j] > 0 else -1
	plt.contourf(y_range, x_range, values)
	plt.colorbar()

if __name__ == "__main__":
	n = 100
	max_iters = 50
	e = 0.05
	b = 1
	c = 1
	p_data, n_data = generate_data(n)
	px1, px2 = p_data
	nx1, nx2 = n_data
	svm(n * 2, max_iters, e, b, c, p_data, n_data)
	plt.scatter(px1, px2, s = 3, c = "r")
	plt.scatter(nx1, nx2, s = 3, c = "w")
	plt.title("svm")
	plt.xlim(-16, 16)
	plt.ylim(-16, 16)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.savefig("svm.png")
