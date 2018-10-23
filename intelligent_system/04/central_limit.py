import matplotlib.pyplot as plt
import numpy as np
import random
import math

def chi2(n, mean, k):
	cum = np.zeros(n)
	for i in range(k):
		x = np.random.randn(n)
		x2 = x ** 2
		cum += x2
	return cum

def diff_from_mean(cum, mu, iterator):
	num_cum = len(cum)
	s_list = []
	for i in range(iterator):
		index = random.randrange(num_cum)
		s_list.append(cum[index])
	mean = np.mean(np.array(s_list))
	return mean - mu

def normalize(cum, mean, disp, iterator, n):
	diff_val = diff_from_mean(cum, mean, iterator)
	z = diff_val / (math.sqrt(disp) * math.sqrt(n))
	return z

iter_n = 15
k = 2
n = 30000
mean = 0
disp = 3
cum = chi2(n, mean, k) # カイ二乗分布
for i in range(iter_n): # 標本平均を取る際に使った標本の数
	z_samples = []
	for j in range(20000):
		#z = normalize(cum, mean, disp, (i + 1), n)
		z = normalize(cum, mean, disp, (i + 1) * 10, n)
		z_samples.append(z)
	plt.clf()
	plt.hist(np.array(z_samples), 100, normed=True)
	#plt.title("histgram : n = %d" %((i + 1)))
	plt.title("histgram : n = %d" %((i + 1) * 10))
	#plt.savefig('report4_figures/central_limit_%d.png' %((i + 1)))
	plt.savefig('report4_figures/central_limit_%d.png' %((i + 1) * 10))
