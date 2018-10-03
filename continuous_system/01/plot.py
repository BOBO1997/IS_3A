import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

num, time = np.loadtxt("./data.txt", unpack = True)

approximate = np.polyfit(num, time, 1)

linear = np.poly1d(approximate)(num)

plt.plot(num, linear, label = 'linear regression')
plt.scatter(num, time, label = 'raw data')
plt.xlabel("input size")
plt.ylabel("time")
# plt.xticks(0.0, 100.0, 10.0)
# plt.yticks(0.0, 0.22, 0.02)

plt.title("Culculation Time by Paralell Merge Sort")

plt.legend()

plt.show()

plt.savefig('figure.png')
