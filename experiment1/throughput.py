#!/usr/bin/python
import fileinput
from collections import Counter

def main():
    packets_per_time = Counter()
    for line in map(lambda line: line.split(" "), fileinput.input()):
        if len(line) and line[0] == "r" and line[4] == 'tcp':
            packets_per_time[int(float(line[1])*10)] += 1
    for time,count in packets_per_time.items():
        print "%s\t%s" % (float(time)/10,count)


if __name__ == "__main__":
    main()
