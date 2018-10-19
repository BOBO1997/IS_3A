#include <stdio.h>
#include <omp.h>
#include <sys/time.h>
#include <cuda.h>
#include <cuda_runtime.h>

int main() {
    struct timeval tv_before, tv_after;
	int size = 1000;
	int iter = 100;
	float u[2][1000][1000] = {0};
	float r = 0.2;
	for (int i = 1; i < size - 1; i++) {
		for (int j = 1; j < size - 1; j++) {
			u[0][i][j] = 1.0;
		}
	}
	gettimeofday(&tv_before, NULL);
	for (int time = 1; time <= iter; time++) {
		//#pragma omp parallel
		if (time % 2 == 0) {
			#pragma omp parallel for collapse(2)
			for (int i = 1; i < size - 1; i++) {
				for (int j = 1; j < size - 1; j++) {
					u[0][i][j] = (1 - 4 * r) * u[1][i][j] + r * (u[1][i + 1][j] + u[1][i - 1][j] + u[1][i][j + 1] + u[1][i][j - 1]);
				}
			}
		}
		else {
			#pragma omp parallel for collapse(2)
			for (int i = 1; i < size - 1; i++) {
				for (int j = 1; j < size - 1; j++) {
					u[1][i][j] = (1 - 4 * r) * u[0][i][j] + r * (u[0][i + 1][j] + u[0][i - 1][j] + u[0][i][j + 1] + u[0][i][j - 1]);
				}
			}
		}
	}
	gettimeofday(&tv_after, NULL);
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			int color = (int)(u[0][i][j] * 255);
			printf("\033[48;2;%d;%d;255m  ", color, color);
			//printf("%.3f ", u[0][i][j]); //数値をdump
		}
		printf("\n");
	}
	printf("\033[0m\n");
	printf("time : %ld sec + %06lu usec\n", tv_after.tv_sec - tv_before.tv_sec, tv_after.tv_usec - tv_before.tv_usec);
}
