#!/bin/bash

./make_experiments.py
./droppedpacketsbycbr.py *.tr > droppedpacketsbycbr.txt 
gnuplot -e "filename='droppedpacketsbycbr.txt'" droppedpacketsbycbr.plot
mv droppedpacketsbycbr.png /var/www/ficklingus/project3/experiment1/
rm droppedpacketsbycbr.txt
rm *.tr
