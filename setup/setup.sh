#!/bin/bash

conda env create -f setup/environment.yml
eval "$(conda shell.bash hook)"
conda activate myenv