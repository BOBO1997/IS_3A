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
void diffusion(float** u, float r, int size, int iter) {
	
	int i = blockIdx.x * blockDim.x + threadIdx.x;
	int j = blockIdx.y * blockDim.y + threadIdx.y;
	for (int time = 0; time < iter; time++) {
		float upper, lower, left, right;
		if (i != 0 && i != (size - 1) && j != 0 && j != (size - 1)) {
			upper = u[i - 1][j];
			lower = u[i + 1][j];
			left  = u[i][j - 1];
			right = u[i][j + 1];
			__syncthreads();
			u[i][j] = (1 - 4 * r) * u[i][j] + r * (upper + lower + left + right);
		}
		__syncthreads();
	}
}

//host code
__host__
int main() {
    struct timeval tv_before, tv_after;
	int size = 100;
	int iter = 100;
	float u[100][100] = {0};
	float out[100][100] = {0};
	float r = 0.2;
	for (int i = 1; i < size - 1; i++) {
		for (int j = 1; j < size - 1; j++) {
			u[i][j] = 1.0;
			out[i][j] = 0.5;
		}
	}
	float **address;
	size_t pitch;
	size_t host_pitch = size * sizeof(float);

	cudaMallocPitch((void**)&address, &pitch, size * sizeof(float), size);
	printf("%d, %d\n", (int)pitch, (int)host_pitch);
	//cudaMemcpy2D(address, host_pitch, u, pitch, size * sizeof(float), size, cudaMemcpyHostToDevice);
	cudaMemcpy2D(address, pitch, u, host_pitch, size * sizeof(float), size, cudaMemcpyHostToDevice);
	
	dim3 threadsPerBlock(size, size);
	dim3 numBlocks(2, 2);
	
	gettimeofday(&tv_before, NULL);
	diffusion<<<numBlocks, threadsPerBlock>>>(address, r, size, iter);
	gettimeofday(&tv_after, NULL);
	
	//cudaMemcpy2D(u, pitch, address, host_pitch, size * sizeof(float), size, cudaMemcpyDeviceToHost);
	cudaMemcpy2D(out, host_pitch, address, pitch, size * sizeof(float), size, cudaMemcpyDeviceToHost);
	cudaFree(address);
	
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			int color = (int)(out[i][j] * 255);
			printf("\033[48;2;%d;%d;255m  ", color, color);
		}
		printf("\033[0m\n");
	}
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			printf("%.3f ", out[i][j]);
		}
		printf("\033[0m\n");
	}

	printf("\033[0m\n");
	printf("time : %ld sec + %06lu usec\n", 
			tv_after.tv_sec - tv_before.tv_sec, 
			tv_after.tv_usec - tv_before.tv_usec);
}
