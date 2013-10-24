set style line 1 default
set terminal png size 1000,400
set output "throughput.png"
set xlabel "Time (seconds)"
set ylabel "Packets per 1/10 second"
set xtics 1 font ",8"

plot [:] "tahoe.txt" using 1:2 with lines title "1mb cbr", "tahoe.txt" using 1:6 with lines title "4mb cbr", "tahoe.txt" using 1:9 with lines title "7mb cbr", "tahoe.txt" using 1:3 with lines title "10mb cbr"
