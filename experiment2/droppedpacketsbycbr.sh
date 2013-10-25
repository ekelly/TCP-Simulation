#!/bin/bash

./make_experiments.py
./droppedpacketsbycbr.py Reno-Reno-* > Reno-Reno.txt
./droppedpacketsbycbr.py Reno-Newreno-* > Reno-Newreno.txt
./droppedpacketsbycbr.py Vegas-Vegas-* > Vegas-Vegas.txt
./droppedpacketsbycbr.py Newreno-Vegas-* > Newreno-Vegas.txt
gnuplot -e "filename='Reno-Reno.txt'" droppedpacketsbycbr.plot
gnuplot -e "filename='Reno-Newreno.txt'" droppedpacketsbycbr.plot
gnuplot -e "filename='Vegas-Vegas.txt'" droppedpacketsbycbr.plot
gnuplot -e "filename='Newreno-Vegas.txt'" droppedpacketsbycbr.plot
mv droppedpackets-Reno-Reno.txt.png /var/www/ficklingus/project3/experiment2/
mv droppedpackets-Reno-Newreno.txt.png /var/www/ficklingus/project3/experiment2/
mv droppedpackets-Vegas-Vegas.txt.png /var/www/ficklingus/project3/experiment2/
mv droppedpackets-Newreno-Vegas.txt.png /var/www/ficklingus/project3/experiment2/
rm Reno-Reno.txt
rm Reno-Newreno.txt
rm Vegas-Vegas.txt
rm Newreno-Vegas.txt
rm *.tr
