#!/bin/sh

rm *.txt
rm *.tr
./make_experiments.py -s 1 -e 10 -i 1
./throughput.py tahoe-*.tr > tahoe.txt ; gnuplot < throughput.plot ; mv throughput.png graph.png ; gnome-open graph.png &
