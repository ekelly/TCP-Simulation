set style line 1 default
set terminal png size 1000,400
set output "throughput.png"
set xlabel "Time (seconds)"
set ylabel "Packets per 1/10 second"
set xtics 1 font ",8"

plot [:] "reno-throughput-6000.txt" using 1:2 with lines title "1mb cbr"
