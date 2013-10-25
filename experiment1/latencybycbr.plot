set style line 1 default
set terminal png size 1000,400
set output "latencybycbr.png"
set xlabel "CBR interference (in kb/sec)"
set ylabel "Latency (average RTT in ms)"
#set xtics 1 font ",8"

plot [:] "latencybycbr.txt" using 1:2 with lines title "NewReno", "latencybycbr.txt" using 1:3 with lines title "Reno", "latencybycbr.txt" using 1:4 with lines title "Tahoe", "latencybycbr.txt" using 1:5 with lines title "Vegas"
