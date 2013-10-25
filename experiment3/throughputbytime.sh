#!/bin/bash

./make_experiments.py
./throughputbytime.py Reno-*.tr > throughput-Reno.txt
./throughputbytime.py Sack1-*.tr > throughput-Sack1.txt
gnuplot -e "filename='throughput-Reno.txt'" throughputbytime.plot
gnuplot -e "filename='throughput-Sack1.txt'" throughputbytime.plot
mv throughput-*.png /var/www/ficklingus/project3/experiment3/
rm *.txt
rm *.tr
