#define min(x, y) (((x) < (y)) ? (x) : (y))

#include <stdio.h>
#include <stdlib.h>

void dgemm(	int m, int n, int k, 
			double alpha, double* A, double* B,
			double beta, double* C,
			double* AB) {
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			double ab = 0;
			for (int l = 0; l < k; l++) {
				printf("%lf\n", A[l + i * k]);
				printf("%lf\n", B[j * k + l]);
				ab += alpha * A[l + i * k] * B[j * k + l];
			}
			printf("\n");
			AB[j + i * n] = ab;
		}
	}
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			C[i + j * n] = AB[i + j * n] + beta * C[i + j * n];
		}
	}
}

int main(){
	double *A, *B, *C, *AB;
	int m, n, k;
	double alpha, beta;

	m = 2, k = 3, n = 2;

	int min_size = 10;
	alpha = 1.0; beta = 1.0;

	A = (double *)malloc(m * k * sizeof(double));
	B = (double *)malloc(k * n * sizeof(double));
	C = (double *)malloc(m * n * sizeof(double));
	AB = (double *)malloc(m * n * sizeof(double));

	if (A == NULL || B == NULL || C == NULL) {
		printf("cannnot alloc memory for matrixes.\n");
		return 1;
	}
	for (int i = 0; i < m * k; i++) A[i] = (double)(i + 1);
	for (int i = 0; i < k * n; i++) B[i] = (double)(-i - 1);
	for (int i = 0; i < m * n; i++) C[i] = 0.0;
	for (int i = 0; i < m * n; i++) AB[i] = 0.0;

	dgemm(m, n, k, alpha, A, B, beta, C, AB);
	
	printf("\nA = \n");
	for (int i = 0; i < min(m, min_size); i++) {
		for (int j = 0; j < min(k, min_size); j++) {
			printf("%12.0f", A[j + i * k]);
		}
		printf("\n");
	}
	printf("\nB = \n");
	for (int i = 0; i < min(k, min_size); i++) {
		for (int j = 0; j < min(n, min_size); j++) {
			printf("%12.0f", B[j + i * n]);
		}
		printf("\n");
	}
	printf("\nC = \n");
	for (int i = 0; i < min(m, min_size); i++) {
		for (int j = 0; j < min(n, min_size); j++) {
			printf("%12.0f", C[j + i * n]);
		}
		printf("\n");
	}
	free(A);
	free(B);
	free(C);
	free(AB);
}
