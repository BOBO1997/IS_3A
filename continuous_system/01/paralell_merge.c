#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

void merge(int* b, int* c, int* d, int bsize, int csize) {
    int i = 0, j = 0, k = 0;
    while (i < bsize && j < csize) {
        if (b[i] < c[j]) { d[k] = b[i]; i++; k++; }
        else { d[k] = c[j]; j++; k++; }
    }
    if (j >= csize) for (int l = k; l < bsize + csize; l++, i++) d[l] = b[i];
    else if (i >= bsize) for (int l = k; l < bsize + csize; l++, j++) d[l] = c[j];
}

void mergeSort(int* d, int dsize) {
    int bsize = dsize / 2;
    int csize = dsize - bsize;
    int* b = calloc(bsize, sizeof(int));
    int* c = calloc(csize, sizeof(int));
    for (int i = 0; i < bsize; i++) b[i] = d[i];
    for (int i = 0; i < csize; i++) c[i] = d[i + bsize];
    if (bsize == 0 || csize == 0) return;
    if (bsize > 1) mergeSort(b, bsize);
    if (csize > 1) mergeSort(c, csize);
    merge(b, c, d, bsize, csize);
}

int main(int argc, char **argv) {

    struct timeval tv_before, tv_after;

    int myid, numproc;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numproc);
    MPI_Comm_rank(MPI_COMM_WORLD, &myid);

    int N = ((0x1)<<23), p = 128;
    int k = N / p;
    int* b = NULL;
    if ((b = (int*)malloc(k * sizeof(int))) == NULL) { perror("calloc failed"); exit(1); }

    if (myid == 0) {
        printf("sort %d items, using %d processes\n", N, p);
        int* a = NULL;
        if ((a = (int*)malloc(N * sizeof(int))) == NULL) { perror("calloc failed"); exit(1); }
        // 代表プロセスで乱数を生成
        for (int i = 0; i < N; i++) { a[i] = rand() % N + 1; }

        // 乱数をそれぞれのプロセスに送る
        for (int i = 1; i < p; i++) MPI_Send(a + i * k, k, MPI_INT, i, 0, MPI_COMM_WORLD);
        for (int i = 0; i < k; i++) b[i] = a[i];
    } else {
        MPI_Recv(b, k, MPI_INT, 0, 0, MPI_COMM_WORLD, NULL);
    }
    MPI_Barrier(MPI_COMM_WORLD);
    if (myid == 0) {
        gettimeofday(&tv_before, NULL);
        printf("before : %ld %06lu\n", tv_before.tv_sec, tv_before.tv_usec);
    }
    //それぞれのプロセスでmergesortをかける
    mergeSort(b, k);

    MPI_Barrier(MPI_COMM_WORLD);
    int i = 1, j = 2, send_flag = 0;
    if (myid == 0) send_flag = 1;

    while (j <= p) {
        if (myid % j != 0) {
            if (send_flag == 0) {
                MPI_Send(b, k * i, MPI_INT, myid - i, 0, MPI_COMM_WORLD);
                free(b); send_flag = 1;
            }
        } else {
            int* c = NULL; if ((c = (int*)malloc(k * i * sizeof(int))) == NULL) { perror("calloc failed"); exit(1); }
            int* d = NULL; if ((d = (int*)malloc(k * j * sizeof(int))) == NULL) { perror("calloc failed"); exit(1); }
            MPI_Recv(c, k * i, MPI_INT, myid + i, 0, MPI_COMM_WORLD, NULL);
            merge(b, c, d, k * i, k * i);
            free(b); free(c); c = NULL; b = d;
        }
        i = i * 2; j = j * 2;
    }
    if (myid == 0) {
        gettimeofday(&tv_after, NULL);
        printf("after  : %ld %06lu\n", tv_after.tv_sec, tv_after.tv_usec);
        printf("sorted array   = ");
        printf("sorting time : %ld sec + %06lu usec\n", tv_after.tv_sec - tv_before.tv_sec, tv_after.tv_usec - tv_before.tv_usec);
    }
    MPI_Finalize();
    return 0;
}
