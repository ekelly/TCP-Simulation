set style line 1 default
set terminal png size 1000,400
set output "throughputbycbr.png"
set xlabel "CBR interference (in kb/sec)"
set ylabel "Throughput (in kb/sec)"
#set xtics 1 font ",8"

plot [:] "throughputbycbr.txt" using 1:2 with lines title "NewReno", "throughputbycbr.txt" using 1:3 with lines title "Reno", "throughputbycbr.txt" using 1:4 with lines title "Tahoe", "throughputbycbr.txt" using 1:5 with lines title "Vegas"
