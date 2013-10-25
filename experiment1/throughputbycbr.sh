#!/bin/bash

./make_experiments.py
./throughputbycbr.py *tr > throughputbycbr.txt
gnuplot < throughputbycbr.plot
mv throughputbycbr.png /var/www/ficklingus/project3/experiment1/
rm throughputbycbr.txt
rm *.tr
