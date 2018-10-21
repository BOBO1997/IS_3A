#!/bin/bash
#SBATCH -N 1
#SBATCH -t 00:10:00
#SBATCH -J yangbo
#SBATCH -o omp_out.txt
#SBATCH -e omp_error.txt

./simulate_openmp

