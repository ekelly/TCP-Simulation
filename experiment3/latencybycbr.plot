set style line 1 default
set terminal png size 1000,400
set output "latency-".filename.".png"
set xlabel "Time (s)"
set ylabel "Latency (average RTT in ms)"
#set xtics 1 font ",8"

plot filename using 1:2 with lines title column(2), '' using 1:3 with lines title column(3)
