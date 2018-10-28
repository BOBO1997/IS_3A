#!/bin/bash
#SBATCH -N 1
#SBATCH -t 00:10:00
#SBATCH -J yangbo
#SBATCH -o correct_gpu2d_out.txt
#SBATCH -e correct_gpu2d_error.txt

./correct_gpu2d
