#!/bin/bash

#SBATCH --job-name=dla_simulation
#SBATCH --partition=instructional
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --time=01:00:00
#SBATCH --output=dla_sim_%j.log

# Your commands follow
python run2.py

