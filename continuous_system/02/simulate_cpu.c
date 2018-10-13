#include <stdio.h>
#include <omp.h>

int main() {
	float u[2][100][100] = {0};
	float r = 0.2;
	for (int i = 1; i < 99; i++) {
		for (int j = 1; j < 99; j++) {
			u[0][i][j] = 1.0;
		}
	}
	for (int time = 1; time <= 1500; time++) {
		//#pragma omp parallel
		if (time % 2 == 0) {
			#pragma omp parallel for collapse(2)
			for (int i = 1; i < 99; i++) {
				for (int j = 1; j < 99; j++) {
					u[0][i][j] = (1 - 4 * r) * u[1][i][j] + r * (u[1][i + 1][j] + u[1][i - 1][j] + u[1][i][j + 1] + u[1][i][j - 1]);
				}
			}
		}
		else {
			#pragma omp parallel for collapse(2)
			for (int i = 1; i < 99; i++) {
				for (int j = 1; j < 99; j++) {
					u[1][i][j] = (1 - 4 * r) * u[0][i][j] + r * (u[0][i + 1][j] + u[0][i - 1][j] + u[0][i][j + 1] + u[0][i][j - 1]);
				}
			}
		}
	}
	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++) {
			int color = (int)(u[0][i][j] * 250);
			printf("\033[48;2;%d;%d;255m  ", color, color);
			//printf("%.3f ", u[0][i][j]);
		}
		printf("\n");
	}
	printf("\033[0m\n");
}
