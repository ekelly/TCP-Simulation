set style line 1 default
set terminal png size 480,320
set output "throughput-".filename.".png"
set xlabel "CBR interference (in kb/sec)"
set ylabel "Throughput (in kb/sec)"
set xtics 2000 font ",10"

plot filename using 1:2 with lines title column(2), '' using 1:3 with lines title column(3)
