set style line 1 default
set terminal png size 400,400
set output "droppedpacketsbycbr.png"
set xlabel "CBR interference (in kb/sec)"
set ylabel "% packets dropped"
#set xtics 1 font ",8"

plot [:] "droppedpacketsbycbr.txt" using 1:2 with lines title "NewReno", "droppedpacketsbycbr.txt" using 1:3 with lines title "Reno", "droppedpacketsbycbr.txt" using 1:4 with lines title "Tahoe", "droppedpacketsbycbr.txt" using 1:5 with lines title "Vegas"
