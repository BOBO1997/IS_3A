#include <stdio.h>
#include <math.h>

typedef struct x {
	double x;
	double y;
} X;

typedef struct v {
	double x;
	double y;
} V;

typedef struct l {
	double a;
	double b;
	double c;
} L;

double dot(V v1, V v2) {
	return v1.x * v2.x + v1.y * v2.y;
}

double vabs(V v) {
	return sqrt(v.x * v.x + v.y * v.y);
}

double dist(X x1, X x2) {
	double x = x1.x - x2.x;
	double y = x1.y - x2.y;
	return sqrt(x * x + y * y);
}

X intersect(L l1, L l2) {
	X x;
	x.x = (l1.b * l2.c - l2.b * l1.c) / (l1.a * l2.b - l2.a * l1.b);
	x.y = (l2.a * l1.c - l1.a * l2.c) / (l1.a * l2.b - l2.a * l1.b);
	return x;
}

double calctime(double r, X x1, X x2, V v1, V v2) {
	double vabs1 = vabs(v1);
	double vabs2 = vabs(v2);
	double rawcos = dot(v1, v2) / (vabs1 * vabs2);
	if (rawcos == -1) {
		return (dist(x1, x2) - 2 * r) / (vabs1 + vabs2);
	}
	else if (rawcos == 1) {
		printf("%f, %f\n", vabs1, vabs2);
		return (dist(x1, x2) - 2 * r) / fabs(vabs1 - vabs2);
	}
	else {
		double cos = fabs(rawcos);
		L l1, l2;
		l1.a = - v1.y; l1.b = v1.x; l1.c = - v1.x * x1.y + v1.y * x1.x;
		l2.a = - v2.y; l2.b = v2.x; l2.c = - v2.x * x2.y + v2.y * x2.x;
		X x = intersect(l1, l2);
		printf("(x, y) = (%f, %f)\n", x.x, x.y);
		double l = dist(x1, x);
		return (l - r * sqrt(2 / (1 - cos))) / vabs1;
	}
}

int main() {
	double r = 1;
	X x1, x2;
	V v1, v2;
	v1.x = 1; v1.y = 0;
	v2.x = 5; v2.y = 0;
	x1.x = 3; x1.y = 0;
	x2.x = 1; x2.y = 0;

	double t = calctime(r, x1, x2, v1, v2);
	printf("%f\n", t);
}
