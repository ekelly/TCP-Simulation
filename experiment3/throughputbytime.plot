set style line 1 default
set terminal png size 1000,400
set output filename.".png"
set xlabel "Time (seconds)
set ylabel "Throughput (in kb/sec)"
set style line 1 lt 1 lc rgb "red" lw 1
set style line 2 lt 3 lc rgb "red" lw 1
set style line 3 lt 1 lc rgb "blue" lw 1
set style line 4 lt 3 lc rgb "blue" lw 1
#set xtics 1 font ",8"

plot filename using 1:2 ls 1 title column(2) with lines, '' using 1:3 ls 2 title column(3) with lines, '' using 1:4 ls 3 title column(4) with lines, '' using 1:5 ls 4 title column(5) with lines
