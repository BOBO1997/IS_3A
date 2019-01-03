import numpy as np
import math

class FFT:
	def __init__(self, p, K):
		self.p = p
		self.K = K
		self.answers = np.zeros(self.K)
		
	def calc_poly(self, x, a_list):
		ans = 0
		power = 0
		for a in a_list:
			ans += a * x ** power
			power += 1
		return ans

	def fft(self, omg, p, K, h):
		if len(p) > 1:
			q = p[::2]
			s = p[1::2]
			print(q)
			print(s)
			pval = fft(omg ** 2, q, k // 2 - 1)
			sval = fft(omg ** 2, s, k // 2 - 1)
			self.answers[h] = 114514
			return pval + qval + omg * sval
		else:
			ans = 0
			power = 0
			for a in p:
				ans += a * omg ** power
				power += 1
			return ans 
	

if __name__ == "__main__":
	p = np.array([1,2,3,4,5,6,7,8])
	k = 3
	K = 2 ** k
	omg = math.sqrt(0.5) * (1 + 1j)
	fft = FFT(p, K)
	answers = fft.fft(omg, p, K, 1)
	print(answers)
