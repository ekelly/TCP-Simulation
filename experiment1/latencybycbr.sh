#!/bin/bash

./make_experiments.py
./latencybycbr.py *.tr > latencybycbr.txt 
gnuplot -e "filename='latencybycbr.txt'" latencybycbr.plot
mv latencybycbr.png /var/www/ficklingus/project3/experiment1/
rm latencybycbr.txt
rm *.tr
