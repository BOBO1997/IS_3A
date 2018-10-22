import matplotlib.pyplot as plt
import numpy as np
import random

def chi2(n, k):
	cum = np.zeros(n)
	for i in range(k):
		x = np.random.normal(0, 3, n)
		x2 = x ** 2
		cum += x2
	return cum

def large_number(cum, mu, iterator):
	num_cum = len(cum)
	s_list = np.ndarray([])
	for i in range(iterator):
		index = random.randrange(num_cum)
		s_list = np.append(s_list, cum[index])
	mean = np.mean(s_list)
	return mean - mu

n = 30000
cum = chi2(n, 2)
diff = np.ndarray([])
for i in range(2000):
	diff = np.append(diff, large_number(cum, 0, i + 1))

cum = chi2(n, 2)
plt.clf()
#plt.ylim(0, 0.6)
#plt.xlim(0, 25)
plt.plot(diff)
plt.title("difference between average and true average")
plt.savefig('report4_figures/large_number.png')
