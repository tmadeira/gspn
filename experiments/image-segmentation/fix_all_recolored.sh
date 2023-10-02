#!/bin/bash -eux

for name in flower fox rabbit tarsila1 tarsila2 tarsila3; do
  dataset="${name}_200.csv"
  for s in 40000 20000 15000 10000 5000 2000 1000 500 200; do
    python fix_recolored.py $dataset mem_recolored_${name}_200_${s}_0.300000.csv
  done
done
