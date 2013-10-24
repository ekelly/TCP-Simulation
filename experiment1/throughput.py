#!/usr/bin/python
import sys
import fileinput
from collections import Counter,defaultdict

def main():
    times = defaultdict(dict)
    for file_name in sys.argv[1:]:
        with open(file_name) as in_file:
            packets_per_time = dict([(time,0) for time in range(0, 100)])
            for line in map(lambda line: line.split(" "), in_file):
                if len(line) and line[0] == "r" and line[4] == 'tcp':
                    packets_per_time[int(float(line[1])*10)] += 1
            for time,count in packets_per_time.items():
                times[time][file_name] = count

    for time,files in sorted(times.items(), key=lambda item: item[0]):
        row = ""
        for file_name,count in sorted(files.items(), key=lambda item: item[0]):
            row += "\t%s" % count
        print "%s%s" % (time/10.0, row)

if __name__ == "__main__":
    main()
