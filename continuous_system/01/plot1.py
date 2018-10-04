import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot, pylab
import matplotlib.pyplot as plt
import numpy as np

num, time = np.loadtxt("./data1.txt", unpack = True)

# approximate = np.polyfit(num, time, 1)

# def y(x):
# 	x.astype(float)
# 	return (np.log2(x / 128) * x / 128 + 2 * x) * 0.001 + 0.035

# linear = np.poly1d(approximate)(num)

# plt.plot(num, linear, label = 'linear regression')

# plt.plot(num, y(num), label = '((n/128)log(n/128) + 2n) * 0.001 +  0.035')

plt.scatter(num, time, label = 'raw data')
plt.xlabel("input size")
plt.ylabel("time [sec]")
plt.yscale("log")
# plt.xticks(0.0, 100.0, 10.0)
# plt.yticks(0.0, 0.22, 0.02)

plt.title("Culculation Time by Paralell Merge Sort")

plt.legend()

plt.show()

plt.savefig('figure1.png')
