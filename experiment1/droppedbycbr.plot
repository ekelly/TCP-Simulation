set style line 1 default
set terminal png size 1000,400
set output "droppedbycbr.png"
set xlabel "CBR interference (in kb/sec)"
set ylabel "Dropped packets (%)"
#set xtics 1 font ",8"

plot [:] "droppedbycbr.txt" using 1:2 with lines title "NewReno", "droppedbycbr.txt" using 1:3 with lines title "Reno", "droppedbycbr.txt" using 1:4 with lines title "Tahoe", "droppedbycbr.txt" using 1:5 with lines title "Vegas"
