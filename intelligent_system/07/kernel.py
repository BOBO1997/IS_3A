import math
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_data(n):
	x_data, y_data = [], []
	for i in range(n):
		x = 6 * ((float(i + 1) / float(n - 1)) - 0.5)
		x_data.append(x)
		y_data.append( math.sin(math.pi * x) / (math.pi * x) + 0.1 * x + random.normalvariate(0, 0.2 ** 2))
	return x_data, y_data

if __name__ == "__main__":
	n = 1000
	x_data, y_data = generate_data(n)
	plt.scatter(x_data, y_data, s = 3)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.savefig("kernel.png")
