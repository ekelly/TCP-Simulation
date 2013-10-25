#!/bin/bash
#!/bin/bash

./make_experiments.py
./latencybyqueue.py Reno-DropTail.tr > Reno-DropTail.txt
./latencybyqueue.py Reno-RED.tr > Reno-RED.txt
./latencybyqueue.py Sack1-DropTail.tr > Sack1-DropTail.txt
./latencybyqueue.py Sack1-RED.tr > Sack1-RED.txt
gnuplot -e "filename='Reno-DropTail.txt'" latencybyqueue.plot
gnuplot -e "filename='Reno-RED.txt'" latencybyqueue.plot
gnuplot -e "filename='Sack1-DropTail.txt'" latencybyqueue.plot
gnuplot -e "filename='Sack1-RED.txt'" latencybyqueue.plot
mv latency-*.png /var/www/ficklingus/project3/experiment3/
rm *.txt 
rm *.tr
