import matplotlib.pyplot as plt
import numpy as np
import random

n = 30000
def chi2(n, k):
	cum = np.zeros(n)
	for i in range(k):
		x = np.random.normal(0, 1, n)
		x2 = x ** 2
		cum += x2
	return cum

def large_number(cum, mu, iterator):
	num_cum = len(cum)
	s_list = np.ndarray([])
	for i in range(iterator):
		index = random.randrange(num_cum)
		np.append(s_list, cum[index])
	mean = np.mean(s_list)
	return mean - mu

cum = chi2(n, 2)
plt.clf()
plt.ylim(0, 0.6)
plt.xlim(0, 25)
plt.title("histgram of chi-square distribution (freedom : 2)")
plt.hist(cum, bins=80, color="green", normed=True)

plt.savefig('report4_figures/chi2.png')

print(type(cum))

diff = np.ndarray([])
for i in range(100):
	np.append(diff, large_number(cum, 1, i + 1))

plt.plot(diff)
plt.savefig('report4_figures/large_number.png')
