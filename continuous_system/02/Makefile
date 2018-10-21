CPUOBJS = simulate_cpu.c
CPUOPENMP = simulate_openmp.c
GPUOBJS = simulate_gpu.cu
GPU2D   = simulate_gpu2d.cu

CC = gcc
CFLAGS = -Wall 
MPFLAG = -fopenmp
NVCC = nvcc

.PHONY: all
all: simulate_cpu simulate_openmp simulate_gpu simulate_gpu2d

simulate_cpu: $(CPUOBJS)
	$(CC) $(CFLAGS) -o $@ $(CPUOBJS)

simulate_openmp: $(CPUOPENMP)
	$(CC) $(CFLAGS) $(MPFLAG) -o $@ $(CPUOPENMP)

simulate_gpu: $(GPUOBJS)
	$(NVCC) -o $@ $(GPUOBJS)

simulate_gpu2d: $(GPU2D)
	$(NVCC) -o $@ $(GPU2D)

.PHONY: clean
clean:
	-rm simulate_cpu simulate_openmp simulate_gpu simulate_gpu2d
