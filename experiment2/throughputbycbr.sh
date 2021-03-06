#!/bin/bash

./make_experiments.py
./throughputbycbr.py Reno-Reno-* > Reno-Reno.txt
./throughputbycbr.py Newreno-Newreno-* > NewReno-NewReno.txt
./throughputbycbr.py Reno-Newreno-* > Reno-Newreno.txt
./throughputbycbr.py Vegas-Vegas-* > Vegas-Vegas.txt
./throughputbycbr.py Newreno-Vegas-* > Newreno-Vegas.txt
gnuplot -e "filename='Reno-Reno.txt'" throughputbycbr.plot
gnuplot -e "filename='NewReno-NewReno.txt'" throughputbycbr.plot
gnuplot -e "filename='Reno-Newreno.txt'" throughputbycbr.plot
gnuplot -e "filename='Vegas-Vegas.txt'" throughputbycbr.plot
gnuplot -e "filename='Newreno-Vegas.txt'" throughputbycbr.plot
mv throughput-Reno-Reno.txt.png /var/www/ficklingus/project3/experiment2/
mv throughput-NewReno-NewReno.txt.png /var/www/ficklingus/project3/experiment2/
mv throughput-Reno-Newreno.txt.png /var/www/ficklingus/project3/experiment2/
mv throughput-Vegas-Vegas.txt.png /var/www/ficklingus/project3/experiment2/
mv throughput-Newreno-Vegas.txt.png /var/www/ficklingus/project3/experiment2/
rm *.txt
rm *.tr
