import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation

# G = 6.67 * 10 ** (-11)
G = 1

def f(v):
	return v

def g(r, m1, m2):
	return (- G * (m1 + m2) / (np.linalg.norm(r) ** 3)) * r

def rungekutta(m1, m2, r1, r2, v1, v2, iters, h):
	r = r1 - r2
	v = v1 - v2
	orbitr = r
	orbit1 = r * (m2 / (m1 + m2))# np.array([])
	orbit2 = r * (- m1 / (m1 + m2)) # np.array([])
	for i in range(iters - 1):
		ar = f(v)
		av = g(r, m1, m2)

		br = f(v + av * h / 2)
		bv = g(r + ar * h / 2, m1, m2)
		
		cr = f(v + bv * h / 2)
		cv = g(r + br * h / 2, m1, m2) 
		
		dr = f(v + cv * h)
		dv = g(r + cr * h, m1, m2)
		
		r = r + h * (ar + 2 * br + 2 * cr + dr) / 6
		v = v + h * (av + 2 * bv + 2 * cv + dv) / 6
		orbit1 = np.append(orbit1, r * ( m2 / (m1 + m2)))
		orbit2 = np.append(orbit2, - r * ( m1 / (m1 + m2)))
		orbitr = np.append(orbitr, r)
	return np.reshape(orbit1, (iters, 2)), np.reshape(orbit2, (iters, 2)), np.reshape(orbitr, (iters, 2))

if __name__ == '__main__':
	iters = 10000
	h = 0.01
	m1 = 1
	m2 = 1
	r1 = np.array([0, 0])
	r2 = np.array([1, 0])
	v1 = np.array([0, -0.6])
	v2 = np.array([0, 0.6])
	orbit1, orbit2, orbitr = rungekutta(m1, m2, r1, r2, v1, v2, iters, h)
	print(orbit1.shape)
	t = np.linspace(0, 1, iters)
	x1, y1 = orbit1.T
	x2, y2 = orbit2.T
	xr, yr = orbitr.T
	
	'''
	fig = plt.figure()
	ims = []
	for i in range(100):
		im = plt.plot(xr[i], yr[i])
		
		im = plt.scatter(np.array([xr[i]]), np.array([yr[i]]),
						c=t,#色と時系列の対応
						cmap=cm.jet,#カラーマップの種類
						marker='.',lw=0)
		
		ims.append(im)
	ani = animation.ArtistAnimation(fig, ims, interval = 100)
	plt.show()
	'''
	plt.scatter(x1,y1,
				c=t,#色と時系列の対応
				cmap=cm.jet,#カラーマップの種類
				marker='.',lw=0)
	plt.scatter(x2,y2,
				c=t,#色と時系列の対応
				cmap=cm.jet,#カラーマップの種類
				marker='.',lw=0)
	'''
	plt.scatter(xr, yr,
				c=t,#色と時系列の対応
				cmap=cm.jet,#カラーマップの種類
				marker='.',lw=0)
	'''
	plt.xlabel("x")
	plt.ylabel("y")
	ax=plt.colorbar()#カラーマップの凡例
	ax.set_label('time [10 ^ (-5) * sec]')#カラーバーのラベルネーム
	#plt.plot(xr, yr)
	#plt.plot(x1, y1)
	#plt.plot(x2, y2)
	plt.savefig("orbit.png")
