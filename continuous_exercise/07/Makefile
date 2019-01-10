ICC = icc
CFLAGS = -Wall
MKL_FLAGS = -mkl
CBLAS_DGEMM = cblas_dgemm.c
LOCAL_DGEMM = local_dgemm.c

.PHONY: all clean

all: cblas_dgemm local_dgemm

cblas_dgemm: $(CBLAS_DGEMM)
	$(ICC) $(CFLAGS) $(MKL_FLAGS) $^ -o $@

local_dgemm: $(LOCAL_DGEMM)
	$(CC) $(CFLAGS) $^ -o $@

clean:
	-rm -f cblas_dgemm local_dgemm
