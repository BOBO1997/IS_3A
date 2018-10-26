import os
import random
import math as m
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def f(x):
	return m.exp(x ** 4) - m.pi

def diff(x):
	return m.exp(x ** 4) * 4 * (x ** 3)
	
def newton(f, diff, init_value, threshold, max_iter, file_name):
	iter_list = []
	val = init_value
	val_list = []
	for i in range(max_iter):
		val = val - f(val) / diff(val)
		err = f(val)
		if abs(err) > threshold:
			iter_list.append(i)
			val_list.append(val)
		else:
			break
	plt.plot(iter_list, val_list)
	plt.xlabel("iteration")
	plt.ylabel("value")
	plt.title("Using Newton's Method")
	plt.savefig(file_name)

def slow_newton(f, diff, init_value, weight, param, threshold, max_iter, file_name):
	iter_list = []
	val = init_value
	val_list = []
	for i in range(max_iter):
		limit = 0
		try:
			l = abs(f(val - weight ** limit * (f(val) / diff(val))))
		except OverflowError:
			l = float('inf')
			pass
		r = (1 - param * (weight ** limit)) * abs(f(val))
		while l >= r or l == float('inf'):
			if (limit > -100):
				limit -= 1
			else:
				break
			try:
				l = abs(f(val - weight ** limit * f(val) / diff(val)))
			except OverflowError:
				l = float('inf')
				pass
			r = (1 - param * (weight ** limit)) * abs(f(val))
		print(val)
		val = val - (weight ** limit) * (f(val) / diff(val))
		err = f(val)
		if abs(err) > threshold:
			iter_list.append(i)
			val_list.append(val)
		else:
			break
	plt.plot(iter_list, val_list)
	plt.xlabel("iteration")
	plt.ylabel("value")
	plt.title("Using Slow Convergence for Newton's Method")
	plt.savefig(file_name)

if __name__ == '__main__':
	init_value = random.uniform(-2.0, 2.0)
	init_value = 0.3
	try:
		newton(f, diff, init_value, 0.0000000001, 100, 'newton.png')
	except OverflowError:
		print("f(x) became too big number")
		pass
	#try:
	slow_newton(f, diff, init_value, 20, 0.9, 0.0000000001, 10000, 'slow_newton.png')
	#except OverflowError:
		#print("f(x) became too big number")
		# pass
