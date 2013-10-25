#!/bin/bash
#!/bin/bash

./make_experiments.py
./latencybyqueue.py Reno-*.tr > latency-Reno.txt
./latencybyqueue.py Sack1-*.tr > latency-Sack1.txt
gnuplot -e "filename='latency-Reno.txt'" latencybyqueue.plot
gnuplot -e "filename='latency-Sack1.txt'" latencybyqueue.plot
mv latency-*.png /var/www/ficklingus/project3/experiment3/
rm *.txt 
rm *.tr
