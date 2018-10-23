import matplotlib.pyplot as plt
import numpy as np
import random
import math

def normal_gauss(n):
	return np.random.randn(n)

def chi2(n, mean, disp, k):
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
	diff_val = diff_from_mean(cum, mean, iterator) # X_iterator - mean
	z = diff_val / (math.sqrt(disp) * math.sqrt(n))
	return z # Z_iterator

def t_dist(n, cum, k):
	gaussian = normal_gauss(n)
	t_sample = []
	for i in range(n):
		t_sample.append(gaussian[i] / math.sqrt(cum[i] / 2))
	return np.array(t_sample)

iter_n = 10
k = 2
n = 30000
mean = 0
disp = 1
cum = chi2(n, mean, disp, k) # カイ二乗分布
t_samples = t_dist(n, cum, k) # t分布
for i in range(iter_n): # 標本平均を取る際に使った標本の数
	z_samples = []
	for j in range(5000):
		z = normalize(t_samples, mean, disp, (i + 1) * 10, n)
		z_samples.append(z)
	plt.clf()
	plt.hist(np.array(z_samples), 100, normed=True)
	plt.title("histgram : n = %d" %((i + 1) * 10))
	plt.savefig('report4_figures/t_central_limit_%d.png' %((i + 1) * 10))
