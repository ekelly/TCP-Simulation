#!/usr/bin/python
import sys
import fileinput
from collections import Counter,defaultdict

def main():
    times = defaultdict(dict)
    for file_name in sys.argv[1:]:
        with open(file_name) as in_file:
            tcp_bytes_per_time = dict([(time,0) for time in range(0, 200)])
            cbr_bytes_per_time = dict([(time,0) for time in range(0, 200)])
            for line in map(lambda line: line.split(" "), in_file):
                if len(line) and line[0] == "r" and line[4] == "tcp" and line[2] == "2" and line[3] == "3":
                    tcp_bytes_per_time[int(float(line[1])*10)] += int(line[5])
                if len(line) and line[0] == "r" and line[4] == "cbr" and line[2] == "1" and line[3] == "2":
                    cbr_bytes_per_time[int(float(line[1])*10)] += int(line[5])
            for time,count in tcp_bytes_per_time.items():
                times[time][file_name+"tcp"] = count
            for time,count in cbr_bytes_per_time.items():
                times[time][file_name+"cbr"] = count

    print "Throughput\tRED-TCP\tRED-CBR\tDropTail-TCP\tDropTail-CBR"
    for time,files in sorted(times.items(), key=lambda item: item[0]):
        row = ""
        for file_name,count in reversed(sorted(files.items(), key=lambda item: item[0])):
            row += "\t%s" % int(count / 1024)
        print "%s%s" % (time/10.0, row)

if __name__ == "__main__":
    main()
