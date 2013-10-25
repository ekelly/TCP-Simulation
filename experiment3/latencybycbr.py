#!/usr/bin/python
import sys
import fileinput
from collections import Counter,defaultdict

# run with ./latencybyqueue.py Reno-*
#       or ./latencybyqueue.py Sack1-*, etc

def main():
    rtts = defaultdict(Counter)
    for in_name in sys.argv[1:]:
        with open(in_name) as in_file:
            qtype = in_name.split('-')[1].split('.')[0]
            seq_map = defaultdict(lambda: defaultdict(dict))
            sum_latency = defaultdict(lambda: defaultdict(float))
            num_acks = defaultdict(Counter)
            for line in map(lambda line: line.split(" "), in_file):
                t = int(float(line[1])*10)
                if len(line) and line[0] == '-' and line[4] == 'tcp' and line[2] == '0' and line[3] == '1':
                    seq_map[t][qtype][line[10]] = float(line[1])
                    print seq_map[t][qtype][line[10]]
                elif len(line) and line[0] == 'r' and line[4] == 'ack' and line[2] == '1' and line[3] == '0':
                    if not line[10] in seq_map[t][qtype]:
                        import pdb; pdb.set_trace()
                    sum_latency[t][qtype] += float(line[1]) - seq_map[t][qtype][line[10]]
                    num_acks[t][qtype] += 1
            rtts[t][qtype] = (sum_latency[t][qtype] / num_acks[t][qtype])

    print 'Time\t'+'\t'.join(sorted(rtts.values()[0].keys()))
    for time,qtypes in sorted(rtts.items(), key=lambda item: int(item[0])):
        row = "%s" % time
        for times,count in sorted(qtypes.items(), key=lambda item: item[0]):
            row += "\t%.2f" % float(count*1000)
        print row

if __name__ == "__main__":
    main()
