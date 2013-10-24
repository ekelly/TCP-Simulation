set style line 1 default
set terminal png size 1000,400
set output "throughput.png"
set xlabel "Time (seconds)"
set ylabel "Packets per 1/10 second"
set xtics 5 font ",8"

plot [:] "throughput.txt" using 1:2 with lines
