#!/bin/bash
#SBATCH -N 8
#SBATCH -B 2:10
#SBATCH -t 00:10:00
#SBATCH -J BOBO
#SBATCH -o output.txt
#SBATCH -e error.txt

./openmp_dgemm
