#!/bin/bash -eux

for name in flower fox rabbit tarsila1 tarsila2 tarsila3; do
  img200="${name}_200.jpg"
  dataset="${name}_200.csv"
  convert -geometry 200 $name.jpg $img200
  python convert.py $img200 > $dataset
  for s in 40000 20000 15000 10000 5000 2000 1000 500 200; do
    dill=$(python learn.py $dataset $s 0.3)
    mem_output=$(python mem.py $dataset $dill)
    k=$(echo $mem_output | sed 's/ .*//')
    python kmeans.py $dataset $k
  done
done
