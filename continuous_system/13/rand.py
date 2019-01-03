import numpy as np

if __name__ == "__main__":
	u = np.random.rand(100000)
	y = u ** 2
	average = np.average(y)
	variance = np.var(y)
	print("average = ", average)
	print("variance = ", variance)
