/* C source code is found in dgemm_example.c */

#define min(x,y) (((x) < (y)) ? (x) : (y))

#include <stdio.h>
#include <stdlib.h>
#include "mkl.h"
#include <sys/time.h>

void print_matrix(int m, int n, double* A) {
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			printf("%12.0f", A[j + i * n]);
		}
		printf("\n");
	}
}

int main()
{
	double *A, *B, *C;
	int m, n, k, i, j;
	double alpha, beta;
	/*
	printf ("\n This example computes real matrix C=alpha*A*B+beta*C using \n"
			" Intel(R) MKL function dgemm, where A, B, and	C are matrices and \n"
			" alpha and beta are double precision scalars\n\n");
	*/
	
	struct timeval tv1, tv2;
	
	m = 1000, k = 1000, n = 1000;
	printf("size of A = (%d, %d)\n", m, k);
	printf("size of B = (%d, %d)\n", k, n);
	printf("size of C = (%d, %d)\n", m, n);
	// m = 2000, k = 200, n = 1000;
	int min_size = 100; // bobo custom
	/*
	printf (" Initializing data for matrix multiplication C=A*B for matrix \n"
			" A(%ix%i) and matrix B(%ix%i)\n\n", m, k, k, n);
	*/
	alpha = 1.0; beta = 0.0;
	/*
	printf (" Allocating memory for matrices aligned on 64-byte boundary for better \n"
			" performance \n\n");
	*/
	A = (double *)mkl_malloc( m*k*sizeof( double ), 64 );
	B = (double *)mkl_malloc( k*n*sizeof( double ), 64 );
	C = (double *)mkl_malloc( m*n*sizeof( double ), 64 );
	if (A == NULL || B == NULL || C == NULL) {
		//printf( "\n ERROR: Can't allocate memory for matrices. Aborting... \n\n");
		mkl_free(A);
		mkl_free(B);
		mkl_free(C);
		return 1;
	}

	// 配列値の初期化
	//printf (" Intializing matrix data \n\n");
	for (i = 0; i < (m*k); i++) {
		A[i] = (double)(i+1);
	}
	for (i = 0; i < (k*n); i++) {
		B[i] = (double)(-i-1);
	}
	for (i = 0; i < (m*n); i++) {
		C[i] = 0.0;
	}

	// 本処理
	//printf (" Computing matrix product using Intel(R) MKL dgemm function via CBLAS interface \n\n");
	gettimeofday(&tv1, NULL);
	cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, 
				m, n, k, alpha, A, k, B, n, beta, C, n);
	gettimeofday(&tv2, NULL);
	printf("%ld %06lu\n", tv1.tv_sec, tv1.tv_usec);
	printf("%ld %06lu\n", tv2.tv_sec, tv2.tv_usec);
	//printf ("\n Computations completed.\n\n");
	/*
	// 結果を表示
	printf (" Top left corner of matrix A: \n");
	print_matrix(m, k, A);
	printf ("\n Top left corner of matrix B: \n");
	print_matrix(k, n, B);
	printf ("\n Top left corner of matrix C: \n");
	print_matrix(m, n, C);
	*/
	//printf ("\n Deallocating memory \n\n");
	mkl_free(A);
	mkl_free(B);
	mkl_free(C);

	//printf (" Example completed. \n\n");
	return 0;
}
