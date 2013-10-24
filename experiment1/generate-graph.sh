#!/bin/sh

cat $1 | python throughput.py > throughput.txt && gnuplot < throughput.plot && mv throughput.png $1.png && gnome-open $1.png
