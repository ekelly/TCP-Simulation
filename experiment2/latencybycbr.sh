#!/bin/bash
#!/bin/bash

./make_experiments.py
./latencybycbr.py Reno-Reno-* > Reno-Reno.txt
./latencybycbr.py Reno-Newreno-* > Reno-Newreno.txt
./latencybycbr.py Vegas-Vegas-* > Vegas-Vegas.txt
./latencybycbr.py Newreno-Vegas-* > Newreno-Vegas.txt
gnuplot -e "filename='Reno-Reno.txt'" latencybycbr.plot
gnuplot -e "filename='Reno-Newreno.txt'" latencybycbr.plot
gnuplot -e "filename='Vegas-Vegas.txt'" latencybycbr.plot
gnuplot -e "filename='Newreno-Vegas.txt'" latencybycbr.plot
mv latency-*.png /var/www/ficklingus/project3/experiment2/
rm *.txt 
rm *.tr
