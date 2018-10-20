#include <stdio.h>
#include <cuda.h>
#include <cuda_runtime.h>
#include <cuda_runtime_api.h>

// Kernel definition
/*
__global__ void MatAdd(int N, float A[N][N], float B[N][N],
float C[N][N])
{
	int i = blockIdx.x * blockDim.x + threadIdx.x;
	int j = blockIdx.y * blockDim.y + threadIdx.y;
	if (i < N && j < N)
		C[i][j] = A[i][j] + B[i][j];
}
*/

__host__
int main()
{
	int N = 16;
	int A[16][16], B[16][16], C[16][16];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			A[i][j] = i + j;
			B[i][j] = i - j;
			C[i][j] = i * j;
		}
	}
	cudaMallocPitch(());
	
	// Kernel invocation
	dim3 threadsPerBlock(16, 16);
	dim3 numBlocks(N / threadsPerBlock.x, N / threadsPerBlock.y);
	MatAdd<<<numBlocks, threadsPerBlock>>>(N, A, B, C);
}
