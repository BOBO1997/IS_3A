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

if __name__ == "__main__":
	n = 1000
	p_data, n_data = generate_data(n)
	px, py = p_data
	nx, ny = n_data
	plt.scatter(px, py, s = 3, c = "r")
	plt.scatter(nx, ny, s = 3, c = "b")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.savefig("svm.png")
