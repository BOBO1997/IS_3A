import os
import random
import math as m
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	try:
		e = m.exp(x ** 4)
	except:
		e = float('inf')
	return e - m.pi

def diff(x):
	try:
		e = m.exp(x ** 4)
	except:
		e = float('inf')
	return e * 4 * (x ** 3)
	
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

def slow_newton(f, diff, init_value, weight, param, threshold, max_iter,file_name):
	iter_list = []
	val = init_value
	val_list = []
	for i in range(max_iter):
		weight_power = 0
		l = abs(f(val - weight ** weight_power * (f(val) / diff(val))))
		r = (1 - param * (weight ** weight_power)) * abs(f(val))
		while l >= r or l == float('inf'):
			if (weight_power > - max_iter):
				weight_power -= 1
			else:
				break
			l = abs(f(val - weight ** weight_power * f(val) / diff(val)))
			r = (1 - param * (weight ** weight_power)) * abs(f(val))
		val = val - (weight ** weight_power) * (f(val) / diff(val))
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
	init_value = 0.1
	slow_newton(f, diff, init_value, 20, 0.9, 0.0000000001, 10000, 'slow_newton.png')
	newton(f, diff, init_value, 0.0000000001, 10000, 'newton.png')
