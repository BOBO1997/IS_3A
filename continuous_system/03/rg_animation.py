import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation

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
	r1 = np.array([1, 0])
	r2 = np.array([0, 0])
	v1 = np.array([0, 0.34])
	v2 = np.array([0, 0])
	orbit1, orbit2, orbitr = rungekutta(m1, m2, r1, r2, v1, v2, iters, h)
	print(orbit1.shape)
	t = np.linspace(0, 1, iters)
	x1, y1 = orbit1.T
	x2, y2 = orbit2.T
	xr, yr = orbitr.T
	#plt.plot(x1, y1)
	#plt.plot(x2, y2)
	
	fig = plt.figure()
	#fig2 = plt.figure()
	ims = []
	#ims2 = []
	for i in range(1000):
		x1_array = np.array([x1[i]])
		y1_array = np.array([y1[i]])
		x2_array = np.array([x2[i]])
		y2_array = np.array([y2[i]])
		im1 = plt.plot(x1_array, y1_array, "r", marker = "o")
		im2 = plt.plot(x2_array, y2_array, "b", marker = "o")
		im3 = plt.plot(x1, y1)
		im4 = plt.plot(x2, y2)
		ims.append(im1 + im2 + im3 + im4)
		#ims2.append([im2])
		print(i)
	ani = animation.ArtistAnimation(fig, ims, interval = 100)
	#ani2 = animation.ArtistAnimation(fig2, ims2, interval = 100)
	plt.show()

	plt.xlabel("x")
	plt.ylabel("y")
	#ax=plt.colorbar()#カラーマップの凡例
	#ax.set_label('time [10 ^ (-5) * sec]')#カラーバーのラベルネーム
	#plt.plot(xr, yr)
	#plt.plot(x1, y1)
	#plt.plot(x2, y2)
	#plt.savefig("orbit.html")
	#ani.save("output.html", writer="imagemagick")
