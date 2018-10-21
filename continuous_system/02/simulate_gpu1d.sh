#!/bin/bash
#SBATCH -N 1
#SBATCH -t 00:10:00
#SBATCH -J bobo
#SBATCH -o gpu1d_out.txt
#SBATCH -e gpu1d_error.txt

./simulate_gpu1d
