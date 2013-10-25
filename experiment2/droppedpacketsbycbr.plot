set style line 1 default
set terminal png size 1000,400
set output "droppedpackets-".filename.".png"
set xlabel "CBR interference (in kb/sec)"
set ylabel "Dropped packets (%)"
#set xtics 1 font ",8"

plot filename using 1:2 with lines title column(2), '' using 1:3 with lines title column(3)
