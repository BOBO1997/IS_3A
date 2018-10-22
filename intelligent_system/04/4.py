import matplotlib.pyplot as plt
import numpy as np

n = 30000
cum = np.zeros(n)
for i in range(2):
	x = np.random.normal(0, 1, n)
	x2 = x**2
	cum += x2

plt.clf()
plt.ylim(0, 0.6)
plt.xlim(0, 25)
plt.title("histgram of chi-square distribution (freedom : 2)")
plt.hist(cum, 80, color="green", normed=True)

plt.savefig('report4_figures/chi2.png')
