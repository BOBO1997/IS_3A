#!/bin/bash
#SBATCH -N 1
#SBATCH -t 00:10:00
#SBATCH -J yangbo
#SBATCH -o gpu2d_out.txt
#SBATCH -e gpu2d_error.txt

./simulate_gpu2d
