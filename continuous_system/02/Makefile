CPUOBJS = simulate_cpu.c
GPUOBJS = simulate_gpu.cu

CC = gcc
CFLAGS = -Wall -fopenmp
NVCC = nvcc

.PHONY: all
all: simulate_cpu simulate_gpu

simulate_cpu: $(CPUOBJS)
	$(CC) $(CFLAGS) -o $@ $(CPUOBJS)

simulate_gpu: $(GPUOBJS)
	$(NVCC) -o $@ $(GPUOBJS)

.PHONY: clean
clean:
	rm simulate_cpu simulate_gpu simulate_gpu2 
