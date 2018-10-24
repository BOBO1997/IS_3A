#include <stdio.h>
#include <omp.h>
#include <sys/time.h>
#include <cuda.h>
#include <cuda_runtime.h>
#include <cuda_runtime_api.h>
#include <driver_types.h>
#include <device_launch_parameters.h>

// device code
__global__
void diffusion(float* u, float r, int size, int iter) {
	
	int i = threadIdx.x / size;
	int j = threadIdx.x % size;
	for (int time = 0; time < iter; time++) {
		if (i != 0 && i != (size - 1) && j != 0 && j != (size - 1)) {
			float upper = u[threadIdx.x - size];
			float lower = u[threadIdx.x + size];
			float left  = u[threadIdx.x - 1];
			float right = u[threadIdx.x + 1];
			__syncthreads();
			u[threadIdx.x] = (1 - 4 * r) * u[threadIdx.x] + r * (upper + lower + left + right);
		}
		__syncthreads();
	}
}

//host code
__host__
int main() {
    struct timeval tv_before, tv_after;
	int size = 30;
	int iter = 100;
	float u[30 * 30] = {0};
	float out[30 * 30] = {0};
	float r = 0.2;
	for (int i = 1; i < size - 1; i++) {
		for (int j = 1; j < size - 1; j++) {
			u[i * size + j] = 1.0;
		}
	}
	float *address;
	const int fsize = size * size * sizeof(float);
	cudaMalloc((void**)&address, fsize);
	cudaMemcpy(address, u, fsize, cudaMemcpyHostToDevice);
	dim3 threadsPerBlock(size * size, 1);
	dim3 numBlocks(1, 1);
	
	gettimeofday(&tv_before, NULL);
	diffusion<<<numBlocks, threadsPerBlock>>>(address, r, size, iter);
	cudaDeviceSynchronize();
	gettimeofday(&tv_after, NULL);

	cudaMemcpy(out, address, fsize, cudaMemcpyDeviceToHost);
	cudaFree(address);
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			int color = (int)(out[i * size + j] * 255);
			printf("\033[48;2;%d;%d;255m  ", color, color);
		}
		printf("\033[0m\n");
	}
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			printf("%.3f ", out[i * size + j]); //数値をdump
		}
		printf("\033[0m\n");
	}
	
	printf("\033[0m\n");
	printf("time : %ld sec + %06lu usec\n", 
			tv_after.tv_sec - tv_before.tv_sec, 
			tv_after.tv_usec - tv_before.tv_usec);
}
