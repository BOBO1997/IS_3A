ICC = icc
CFLAGS = -Wall -O2
MKL_FLAGS = -mkl
CBLAS_DGEMM = cblas_dgemm.c
LOCAL_DGEMM = local_dgemm.c
SVD = svd.c

.PHONY: all clean

all: cblas_dgemm local_dgemm svd

cblas_dgemm: $(CBLAS_DGEMM)
	$(ICC) $(CFLAGS) $(MKL_FLAGS) $^ -o $@

local_dgemm: $(LOCAL_DGEMM)
	$(CC) $(CFLAGS) $^ -o $@

svd: $(SVD)
	$(ICC) $(CFLAGS) $(MKL_FLAGS) $^ -o $@

clean:
	-rm -f cblas_dgemm local_dgemm svd
