import math

def f(x, r, c):
	return - math.sqrt(r ** 2 - (c - x) ** 2) - math.cos(x)

def diff(x, r, c):
	return (x - c) / math.sqrt(r ** 2 - (c - x) ** 2) + math.sin(x)

def divide(a, b):
	w = (3 - math.sqrt(5)) / 2
	return a * w + b * (1 - w)

def collision(f, diff, center, y, r, threshold, max_iter):
	a, b, x = 0, 0, 0
	if diff(center, r, center) < 0:
		a = center
		b = center + math.pi
		c = divide(b, a)
		d = divide(a, b)
	else:
		a = center - math.pi
		b = center
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
	c = 10
	y = 100
	r = 10

	threshold = 0.0000001
	max_iter = 1000
	
	h = y - collision(f, diff, c, y, r, threshold, max_iter)
	t = time(h)
	print(t)