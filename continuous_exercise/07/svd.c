#include <stdlib.h>
#include <stdio.h>

/* DGESVD prototype */
extern void dgesvd( char* jobu, char* jobvt, int* m, int* n, double* a,
		int* lda, double* s, double* u, int* ldu, double* vt, int* ldvt,
		double* work, int* lwork, int* info );
/* Auxiliary routines prototypes */
extern void print_matrix( char* desc, int m, int n, double* a, int lda );
//extern void print_matrix( int m, int n, double* a );

/* Parameters */
#define M 6
#define N 5
#define LDA M
#define LDU M
#define LDVT N

/* Main program */
int main() {
	/* Locals */
	int m = M, n = N, lda = LDA, ldu = LDU, ldvt = LDVT, info, lwork;
	double wkopt;
	double* work;
	/* Local arrays */
	double s[N], u[LDU*M], vt[LDVT*N];
		/*
	double a[LDA*N] = {
	    1,  2,	3,	4,	5,	6,
	    1,	3,	5,	7,	9,	11,
			12,	10,	8,	6,	4,	2,
			5,	4,	6,	3,	7,	2,
			5,	6,	4,	7,	3,	8,
			6,	5,	4,	3,	2,	1
	};
		*/
	double a[LDA*N] = {
	    8.79,  6.11, -9.15,  9.57, -3.49,  9.84,
	    9.93,  6.91, -7.93,  1.64,  4.02,  0.15,
	    9.83,  5.04,  4.86,  8.83,  9.80, -8.99,
	    5.45, -0.27,  4.85,  0.74, 10.00, -6.02,
	    3.16,  7.98,  3.01,  5.80,  4.27, -5.31
	};
	/* Executable statements */
	printf( " DGESVD Example Program Results\n" );
	/* Query and allocate the optimal workspace */
	lwork = -1;
	dgesvd( "All", "All", &m, &n, a, &lda, s, u, &ldu, vt, &ldvt, &wkopt, &lwork,
	 &info );
	lwork = (int)wkopt;
	work = (double*)malloc( lwork*sizeof(double) );
	/* Compute SVD */
	dgesvd( "All", "All", &m, &n, a, &lda, s, u, &ldu, vt, &ldvt, work, &lwork,
	 &info );
	/* Check for convergence */
	if( info > 0 ) {
		printf( "The algorithm computing SVD failed to converge.\n" );
		exit( 1 );
	}
	/* Print singular values */
	print_matrix( "Singular values", 1, n, s, 1 );
	/* Print left singular vectors */
	print_matrix( "Left singular vectors (stored columnwise)", m, m, u, ldu );
	/* Print right singular vectors */
	print_matrix( "Right singular vectors (stored rowwise)", n, n, vt, ldvt );
	//double S[M * N] = {0};
	//double C[M * N] = {0};
	//double Ans[M * N] = {0};
	/*
	double *U, *S, *VT, *C, *Ans;
	U   = (double *)mkl_malloc( M*M*sizeof( double ), 64 );
	S   = (double *)mkl_malloc( M*N*sizeof( double ), 64 );
	VT  = (double *)mkl_malloc( N*N*sizeof( double ), 64 );
	C   = (double *)mkl_malloc( M*N*sizeof( double ), 64 );
	Ans = (double *)mkl_malloc( M*N*sizeof( double ), 64 );
	for (int i = 0; i < )
	for (int i = 0; i < N; i++) S[i + i * N] = s[i];
	cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, 
				m, n, m, 1, u, m, S, n, 0, C, n);
	cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, 
				m, n, n, 1, C, n, vt, n, 0, Ans, n);

	printf("singular values : \n");
	print_matrix(1, n, s);
	printf("u : \n");
	print_matrix(m, n, u);
	printf("V.T: \n");
	print_matrix(n, n, vt);
	*/
	/* Free workspace */

	free( (void*)work );
	exit( 0 );
} /* End of DGESVD Example */

/* Auxiliary routine: printing a matrix */
void print_matrix( char* desc, int m, int n, double* a, int lda ) {
	int i, j;
	printf( "\n %s\n", desc );
	for( i = 0; i < m; i++ ) {
		for( j = 0; j < n; j++ ) printf( " %6.10f", a[i+j*lda] );
		printf( "\n" );
	}
}
/*
void print_matrix(int m, int n, double* A) {
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			printf("%12.0f", A[j + i * n]);
		}
		printf("\n");
	}
}
*/
