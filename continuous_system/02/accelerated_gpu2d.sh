#!/bin/bash
#SBATCH -N 1
#SBATCH -t 00:10:00
#SBATCH -J yangbo
#SBATCH -o a_gpu2d_out.txt
#SBATCH -e a_gpu2d_error.txt

./accelerated_gpu2d
