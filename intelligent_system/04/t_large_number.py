import matplotlib.pyplot as plt
import numpy as np
import random
import math

def normal_gauss(n):
	return np.random.randn(n)

def chi2(n, mean, disp, k):
	cum = np.zeros(n)
	for i in range(k):
		x = np.random.normal(mean, disp, n)
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

def t_dist(n, cum, k):
	gaussian = normal_gauss(n)
	t_sample = []
	for i in range(n):
		t_sample.append(gaussian[i] / math.sqrt(cum[i] / 2))
	return np.array(t_sample)

iter_n = 1000
k = 2
n = 1000
mean = 0
disp = 3
cum = chi2(n, mean, disp, k) # カイ二乗分布
t_samples = t_dist(n, cum, k)
diff_samples = []
for i in range(iter_n):
	z_samples = []
	for j in range(100):
		z = normalize(t_samples, mean, disp, i + 1, n) # Z_iterator
		z_samples.append(z)
	diff = diff_from_mean(z_samples, mean, i + 1)
	diff_samples.append(z)

plt.clf()
plt.plot(np.array(diff_samples))
plt.title("diff from mean")
plt.savefig('report4_figures/t_large_number.png')
