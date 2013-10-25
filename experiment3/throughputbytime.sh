#!/bin/bash

./make_experiments.py
./throughputbytime.py Reno-RED.tr > Reno-RED.txt
./throughputbytime.py Reno-DropTail.tr > Reno-DropTail.txt
./throughputbytime.py Sack1-RED.tr > Sack1-RED.txt
./throughputbytime.py Sack1-DropTail.tr > Sack1-DropTail.txt
gnuplot -e "filename='Reno-RED.txt'" throughputbytime.plot
gnuplot -e "filename='Reno-DropTail.txt'" throughputbytime.plot
gnuplot -e "filename='Sack1-RED.txt'" throughputbytime.plot
gnuplot -e "filename='Sack1-DropTail.txt'" throughputbytime.plot
mv throughput-*.png /var/www/ficklingus/project3/experiment3/
rm *-RED.txt
rm *-DropTail.txt
rm *.tr
