import math
import random
import sklearn
import sklearn.metrics
import numpy as np
import matplotlib.pyplot as plt

def kernel(xi, xj, h = 0.3):
    return np.exp(- np.sum((xi - xj) ** 2) / (2 * h ** 2))

def create_k_matrix(n, h, x_data):
	K = np.zeros((n, n), dtype = float)
	for i in range(n):
		for j in range(n):
			K[i, j] = kernel(x_data[i], x_data[j], h)
	return K

def culc_theta(n, h, K, lam, y_data):
	return np.dot(np.dot(np.linalg.inv(np.dot(K, K) + lam * np.eye(n)), K), y_data)

def culc_theta_kernel(x, h, theta, x_data):
	sum_theta_kernel = 0
	for i in range(len(x_data)):
		sum_theta_kernel += theta[i] * kernel(x, x_data[i], h)
	return sum_theta_kernel

def generate_data(n):
	x_data, y_data, x_org, y_org = [], [], [], []
	for i in range(n):
		x = 6 * ((float(i + 1) / float(n - 1)) - 0.5)
		x_data.append(x)
		x_org.append(x)
		y_data.append( math.sin(math.pi * x) / (math.pi * x) + 0.1 * x + random.normalvariate(0, 0.2 ** 2) )
		y_org.append( math.sin(math.pi * x) / (math.pi * x) + 0.1 * x )
	return x_data, y_data, x_org, y_org

def predict_plot(n, h, lam, x_data, y_data):
	K = create_k_matrix(n, h, x_data)
	theta = culc_theta(n, h, K, lam, y_data)
	x_plot = np.arange(-3, 3, 0.01)
	y_plot = np.zeros(len(x_plot))
	for i in range(len(x_plot)):
		y_plot[i] = culc_theta_kernel(x_plot[i], h, theta, x_data)
	return x_plot, y_plot, theta

def cross_validation(n, k, h, lam, x_data, y_data):
	size = n // k
	N = n - size
	n_plot = 600
	x_plot_mat = np.zeros((0 , n_plot))
	y_plot_mat = np.zeros((0 , n_plot))
	mse_list = []
	for i in range(k):
		if i == 0:
			train_x_data = x_data[size:]
			train_y_data = y_data[size:]
			test_x_data = x_data[:size]
			test_y_data = y_data[:size]
		elif i == k - 1:
			train_x_data = x_data[:-size]
			train_y_data = y_data[:-size]
			test_x_data = x_data[i * size:]
			test_y_data = y_data[i * size:]
		else:
			train_x_data = np.concatenate((x_data[:size * i], x_data[size * i + size:]))
			train_y_data = np.concatenate((y_data[:size * i], y_data[size * i + size:]))
			test_x_data = x_data[i * size:i * size + size]
			test_y_data = y_data[i * size:i * size + size]
		train_x_plot, train_y_plot, theta = predict_plot(N, h, lam, train_x_data, train_y_data)
		x_plot_mat = np.concatenate((x_plot_mat, np.reshape(train_x_plot, (1, n_plot))))
		y_plot_mat = np.concatenate((y_plot_mat, np.reshape(train_y_plot, (1, n_plot))))
		test_f_data = []
		for j in range(size):
			test_f_data.append( culc_theta_kernel(test_x_data[j], h, theta, train_x_data) )
		mse_list.append( sklearn.metrics.mean_squared_error(test_f_data, test_y_data) )

	ave_x_plot = np.average(x_plot_mat, axis = 0)
	ave_y_plot = np.average(y_plot_mat, axis = 0)
	return ave_x_plot, ave_y_plot, mse_list

if __name__ == "__main__":
	n = 1000
	k = 10
	h_list = [0.1, 0.5, 1]
	lam_list = [0.1, 0.5, 1]

	x_data, y_data, x_org, y_org = generate_data(n)
	sklearn.utils.shuffle(x_data, y_data)
	
	for i in range(len(h_list)):
		for j in range(len(lam_list)):
			h = h_list[i]
			lam = lam_list[j]

			plt.scatter(x_data, y_data, s = 1)
			plt.plot(x_org, y_org, color = "g", label = "original", linewidth = 0.5)
			
			x_plot, y_plot, mse_list = cross_validation(n, k, h, lam, x_data, y_data)
			print(mse_list)
			error = np.average(mse_list)
			plt.plot(x_plot, y_plot, color = "r", label = "predicted\n(h = {0}, lambda = {1}, error = {2})".format(h, lam, error), linewidth = 0.5)

			plt.xlim(-3, 3)
			plt.ylim(-0.6, 1.2)
			plt.title("gaussian kernel model")
			plt.legend(fontsize = 'x-small')
			plt.xlabel("x")
			plt.ylabel("y")
			plt.savefig("kernel_h%dl%d.png" %(int(h * 10), int(lam * 10)))
			plt.clf()
			print("finished case : %f %f" %(h, lam))
