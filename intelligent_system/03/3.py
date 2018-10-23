import matplotlib.pyplot as plt
import numpy as np

for i in range(11):
	n = 30000
	cum = np.zeros(n)
	for i in range(i):
		x = np.random.normal(0, 1, n)
		x2 = x**2
		cum += x2

	plt.clf()
	plt.ylim(0, 0.6)
	plt.xlim(0, 25)
	plt.title("histgram of chi-square distribution (freedom : %d)" %(i + 1))
	plt.hist(cum, 80, color="green", normed=True)

	plt.savefig('report3_figures/figure%d.png' %(i + 1))
