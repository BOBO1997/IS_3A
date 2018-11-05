import math

def f(x, r, c):
	return - math.sqrt(r ** 2 - (c - x) ** 2) - math.cos(x)

def diff(x, r, c):
	return (x - c) / math.sqrt(r ** 2 - (c - x) ** 2) + math.sin(x)

def divide(a, b):
	w = (3 - math.sqrt(5)) / 2
	return a * w + b * (1 - w)

def collision(f, diff, center, r, threshold, max_iter):
	a, b, x = 0, 0, 0
	if diff(center, r, center) < 0:
		a = center
		b = center + math.pi
		if a < center - r:
			a = center - r
		if b > center + r:
			b = center + r
		c = divide(b, a)
		d = divide(a, b)
	else:
		a = center - math.pi
		b = center
		if a < center - r:
			a = center - r
		if b > center + r:
			b = center + r
		c = divide(b, a) # aより
		d = divide(a, b) # bより
	for _ in range(max_iter):
		if f(c, r, center) < f(d, r, center):
			b = d
			c = divide(b, a)
			d = divide(a, b)
		else:
			a = c
			c = divide(b, a)
			d = divide(a, b)
		if abs(c - d) < threshold:
			break
	return - f(c, r, center)

def time(h):
	return math.sqrt(2 * h / 9.8)

if __name__ == '__main__':
	x = 3
	y = 4
	z = 100
	r = 2
	c = math.sqrt(x ** 2 + y ** 2)
	threshold = 0.0000001
	max_iter = 1000
	
	h = z - collision(f, diff, c, r, threshold, max_iter)
	print(h)
	t = time(h)
	print(t)
