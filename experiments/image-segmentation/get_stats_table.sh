#!/bin/bash -eux

for dataset in flower tarsila3 tarsila2; do
  for s in 20000 15000 10000 5000 2000 500 200; do
    python view_spn_stats.py ${dataset}_200_${s}_0.300000.dill
    python analyze_recolored.py mem_recolored_${dataset}_200_${s}_0.300000.csv
  done
done
