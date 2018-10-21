#!/bin/bash
#SBATCH -N 1
#SBATCH -t 00:10:00
#SBATCH -J yangbo
#SBATCH -o cpu_out.txt
#SBATCH -e cpu_error.txt

./simulate_cpu
