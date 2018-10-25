CPUOBJS = simulate_cpu.c
CPUOMP 	= simulate_omp.c
GPUOBJS = simulate_gpu1d.cu
GPU2D   = simulate_gpu2d.cu
A_GPU2D = accelerated_gpu2d.cu
CORRECT = correct_gpu2d.cu

CC = gcc
CFLAGS = -Wall 
OMPFLAG = -fopenmp
NVCC = nvcc

.PHONY: all
all: simulate_cpu simulate_omp simulate_gpu1d simulate_gpu2d accelerated_gpu2d correct_gpu2d

simulate_cpu: $(CPUOBJS)
	$(CC) $(CFLAGS) -o $@ $(CPUOBJS)

simulate_omp: $(CPUOMP)
	$(CC) $(CFLAGS) $(OMPFLAG) -o $@ $(CPUOMP)

simulate_gpu1d: $(GPUOBJS)
	$(NVCC) -o $@ $(GPUOBJS)

simulate_gpu2d: $(GPU2D)
	$(NVCC) -o $@ $(GPU2D)

accelerated_gpu2d: $(A_GPU2D)
	$(NVCC) -o $@ $(A_GPU2D)

correct_gpu2d: $(CORRECT)
	$(NVCC) -o $@ $(CORRECT)

.PHONY: clean
clean:
	-rm simulate_cpu simulate_omp simulate_gpu1d simulate_gpu2d accelerated_gpu2d correct_gpu2d
