import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
	scblas = np.array([50,100,500,1000,2000,3000,4000,5000])
	tcblas = np.array([70312 - 57372,
					   810496 - 783555,
					   40486 - 25806,
					   52994 - 33527,
					   1074960 - 614228,
					   4153828 - 3248550,
					   3325513 - 2071552,
					   #1323322 - 551516,
					   1630461 - 157054])
	slocal = np.array([50, 100, 500, 700, 1000])
	tlocal = np.array([334 - 212,
					   7832 - 6981,
					   525018 - 388726,
					   694709 - 322535,
					   8190307 - 6673303])
	somp = np.array([50,100,500,1000,2000])
	tomp = np.array([624545 - 595461,
					 83756 - 43039,
					 6024728 - 5998793,
					 759742 - 459776,
					 5667636 - 4243704])
	tcblas = tcblas / 1000000
	tlocal = tlocal / 1000000
	tomp = tomp / 1000000
	plt.xlabel("size")
	plt.ylabel("time(s)")
	plt.plot(scblas, tcblas)
	plt.plot(slocal, tlocal)
	plt.plot(somp, tomp)
	plt.savefig("mat_time.png")
	plt.clf()
