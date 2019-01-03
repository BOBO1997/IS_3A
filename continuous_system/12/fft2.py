import math
import time
import matplotlib.pyplot as plt

def fft(val, args, K):
	#print(val, args, K)
	if len(args) == 0:
		return np.array([0])
	elif len(args) == 1:
		#print("ans = ", args)
		return args
	else:
		ans = [0 for i in range(K)]
		q_args = args[::2]
		s_args = args[1::2]
		q_ans = fft(val ** 2, q_args, K // 2)
		s_ans = fft(val ** 2, s_args, K // 2)
		for h in range(K // 2):
			ans[h] = q_ans[h] + val ** h * s_ans[h]
			ans[h + K // 2] = q_ans[h] - val ** h * s_ans[h]
		#print("ans = ", ans)
		return ans

def calc_poly(val, args):
	ans = 0
	power = 0
	for a in args:
		ans += a * val ** power
		power += 1
	return ans

def calc_every_poly(val, args, K):
	ans = []
	for h in range(K):
		ans.append(calc_poly(val ** h, args))
	return ans

if __name__ == "__main__":
	fft_t = []
	naive_t = []
	max_power = 14
	K_val = [2 ** k for k in range(max_power)]
	k_val = [k for k in range(max_power)]
	for k in range(max_power):
		K = 2 ** k
		val = math.cos(2 * math.pi / K) + 1j * math.sin(2 * math.pi / K)
		args = [i + 1 for i in range(K)]
		t1 = time.time()
		fft_ans = fft(val, args, K)
		t2 = time.time()
		#print(fft_ans)
		#print("time by fft: ", t2 - t1)
		t3 = time.time()
		p_ans = calc_every_poly(val, args, K)
		t4 = time.time()
		#print(p_ans)
		#print("time by naive: ", t4 - t3)
		fft_t.append(t2 - t1)
		naive_t.append(t4 - t3)
	plt.plot(K_val, fft_t)
	plt.scatter(K_val, fft_t, s = 10)
	plt.plot(K_val, naive_t)
	plt.scatter(K_val, naive_t, s = 10)
	plt.xlabel("max degree")
	plt.ylabel("time")
	plt.savefig("fft.png")
	plt.clf()

	plt.plot(k_val, fft_t)
	plt.scatter(k_val, fft_t, s = 10)
	plt.plot(k_val, naive_t)
	plt.scatter(k_val, naive_t, s = 10)
	plt.xlabel("max degree")
	plt.ylabel("time")
	plt.savefig("fft_log.png")
	plt.clf()

