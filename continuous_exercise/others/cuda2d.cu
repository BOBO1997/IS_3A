#include<stdio.h>
#include<cuda.h>
#define height 50
#define width 50

// Device code
__global__ void kernel(float* devPtr, int pitch)
{
    for (int r = 0; r < height; ++r) {
        float* row = (float*)((char*)devPtr + r * pitch);
        for (int c = 0; c < width; ++c) {
             float element = row[c];
        }
    }
}

//Host Code
int main()
{
	float* devPtr;
	size_t pitch;
	cudaMallocPitch((void**)&devPtr, &pitch, width * sizeof(float), height);
	printf("%d\n", (int)pitch);
	kernel<<<100, 512>>>(devPtr, pitch);
	return 0;
}
