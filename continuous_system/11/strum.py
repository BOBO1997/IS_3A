import numpy as np
np.set_printoptions(precision = 3)

def f(k, l, A):
	T = A[:(k+1), :(k+1)] - l * np.eye(k+1)
	#print(T)
	#print(np.linalg.det(T))
	return np.linalg.det(T)

if __name__ == "__main__":
	size = 10
	A = np.triu(np.ones(size), k = 1) - np.triu(np.ones(size), k = 2) + np.triu(np.ones(size), k = -1) - np.triu(np.ones(size), k = 0) 
	for i in range(size):
		A[i, i] = i + 1
	print(A)
	for j in range(size):
		l = j + 1
		#nums = []
		num = 0
		prev = f(0, l, A)
		for i in range(size):
			det = f(i, l, A)
			#print(prev, det)
			p = -1 if prev <= 0 else 1
			d = -1 if det <= 0 else 1
			#print(p, d)
			if p * d < 0:
				num += 1
			prev = det
			#nums.append(det)
		print(l, "	未満の固有値の個数:	", num + 1)
		#ispos = [True if v > 0 else False for v in nums]
		#print(ispos)
	W, V = np.linalg.eig(A)
	print(W)
