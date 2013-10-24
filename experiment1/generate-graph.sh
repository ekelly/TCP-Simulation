#!/bin/sh

cat $1 | python throughput.py > throughput.txt && gnuplot < throughput.plot && gnome-open throughput.png
