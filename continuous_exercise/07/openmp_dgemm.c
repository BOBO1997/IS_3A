#define min(x, y) (((x) < (y)) ? (x) : (y))

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <omp.h>

void dgemm(	int m, int n, int k, 
			double alpha, double* A, double* B,
			double beta, double* C,
			double* AB) {
	#pragma omp parallel for collapse(2)
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			double ab = 0;
			for (int l = 0; l < k; l++) {
				ab += alpha * A[l + i * k] * B[j + l * n];
			}
			AB[j + i * n] = ab;
		}
	}
	#pragma omp parallel for collapse(2)
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			C[i + j * n] = AB[i + j * n] + beta * C[i + j * n];
		}
	}
}

void print_matrix(int m, int n, double* A) {
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			printf("%12.0f", A[j + i * n]);
		}
		printf("\n");
	}
}

int main(){
	double *A, *B, *C, *AB;
	int m, n, k;
	double alpha, beta;

	struct timeval tv1, tv2;
	int temp = 700;
	m = temp, k = temp, n = temp;

	printf("size of A = (%d, %d)\n", m, k);
	printf("size of B = (%d, %d)\n", k, n);
	printf("size of C = (%d, %d)\n", m, n);

	//int min_size = 100;
	alpha = 1.0; beta = 0.0;
	
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
	
	gettimeofday(&tv1, NULL);
	dgemm(m, n, k, alpha, A, B, beta, C, AB);
	gettimeofday(&tv2, NULL);

	printf("%ld %06lu\n", tv2.tv_sec, tv2.tv_usec);
	printf("%ld %06lu\n", tv1.tv_sec, tv1.tv_usec);
	/*
	printf("\nA = \n");
	print_matrix(m, k, A)
	printf("\nB = \n");
	print_matrix(k, n, B)
	printf("\nC = \n");
	print_matrix(m, n, C)
	*/
	free(A);
	free(B);
	free(C);
	free(AB);
}
