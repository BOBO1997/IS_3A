import matplotlib.pyplot as plt
import numpy as np
import random

def chi2(n, k):
	cum = np.zeros(n)
	for i in range(k):
		x = np.random.randn(n)
		x2 = x ** 2
		cum += x2
	return cum

def large_number(cum, mu, iterator):
	num_cum = len(cum)
	s_list = []
	for i in range(iterator):
		index = random.randrange(num_cum)
		s_list.append(cum[index])
	mean = np.mean(np.array(s_list))
	return mean - mu

n = 30000
cum = chi2(n, 2)
diff = []
for i in range(10000):
	diff.append(large_number(cum, 0, i + 1))

plt.clf()
plt.plot(np.array(diff))
plt.title("difference between average and true average")
plt.savefig('report4_figures/large_number.png')
