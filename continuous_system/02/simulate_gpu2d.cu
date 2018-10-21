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
void diffusion(float* u, size_t pitch, float r, int size, int iter) {
	
	int i = blockIdx.x * blockDim.x + threadIdx.x;
	int j = blockIdx.y * blockDim.y + threadIdx.y;

	for (int time = 0; time < iter; time++) {
		if (i != 0 && i != (size - 1) && j != 0 && j != (size - 1)) {
			float upper, lower, left, right;
			float* row = (float*)((char*)u + j * pitch);
			float* upper_row = (float*)((char*)u + (j - 1) * pitch);
			float* lower_row = (float*)((char*)u + (j + 1) * pitch);
			upper = upper_row[i];
			lower = lower_row[i];
			left  = row[i - 1];
			right = row[i + 1];
			__syncthreads();
			row[i] = (1 - 4 * r) * row[i] + r * (upper + lower + left + right);
		}
		__syncthreads();
	}
}

//host code
__host__
int main() {
    struct timeval tv_before, tv_after;
	int size = 512;
	int iter = 100;
	int thread_width = 32;
	float u[512][512] = {0};
	float out[512][512] = {0};
	float r = 0.225;
	for (int i = 1; i < size - 1; i++) {
		for (int j = 1; j < size - 1; j++) {
			u[i][j] = 1.0;
		}
	}
	//float **address;
	float *address;
	size_t pitch;
	size_t host_pitch = size * sizeof(float);

	cudaMallocPitch(&address, &pitch, size * sizeof(float), size);
	printf("host_pitch = %d, device_pitch = %d\n", (int)host_pitch, (int)pitch);
	cudaMemcpy2D(address, pitch, u, host_pitch, size * sizeof(float), size, cudaMemcpyHostToDevice);
	
	dim3 threadsPerBlock(thread_width, thread_width);
	dim3 numBlocks(size / thread_width, size / thread_width);
	
	gettimeofday(&tv_before, NULL);
	diffusion<<<numBlocks, threadsPerBlock>>>(address, pitch, r, size, iter);
	cudaDeviceSynchronize();
	gettimeofday(&tv_after, NULL);
	
	cudaMemcpy2D(out, host_pitch, address, pitch, size * sizeof(float), size, cudaMemcpyDeviceToHost);
	cudaFree(address);
	
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			int color = (int)(out[i][j] * 255);
			printf("\033[48;2;%d;%d;255m ", color, color);
		}
		printf("\033[0m\n");
	}
	/*
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			printf("%.3f ", out[i][j]);
		}
		printf("\033[0m\n");
	}
	*/
	printf("\033[0m\n");
	printf("time : %06ld sec + %lu usec\n", 
			tv_after.tv_sec - tv_before.tv_sec, 
			tv_after.tv_usec - tv_before.tv_usec);
}
