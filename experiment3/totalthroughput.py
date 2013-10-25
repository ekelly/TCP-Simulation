#!/usr/bin/python
import sys
import fileinput
from collections import Counter,defaultdict

def main():
    print "Experiment\tTotal Bytes (Mb/s)"
    for file_name in sys.argv[1:]:
        with open(file_name) as in_file:
            row = file_name
            total_bytes = 0
            for line in map(lambda line: line.split(" "), in_file):
                if len(line) and line[0] == "r" and line[4] == 'tcp':
                    total_bytes += int(line[5])
            print row + "\t%.2f" % (float(total_bytes) / (1024 * 1024))

if __name__ == "__main__":
    main()
