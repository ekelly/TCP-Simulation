#!/usr/bin/python
import sys
import fileinput
from collections import Counter,defaultdict

# run with ./latencybyqueue.py Reno-Reno*
#       or ./latencybyqueue.py Vegas-Vegas*, etc

def main():
    rtts = defaultdict(Counter)
    for in_name in sys.argv[1:]:
        with open(in_name) as in_file:
            cbr = int(in_name.split('-')[2].split('.')[0])
            variant1 = in_name.split('-')[0].split('.')[0]
            variant2 = in_name.split('-')[1].split('.')[0]
            if variant1 == variant2:
                variant1 += "-1"
                variant2 += "-2"
            seq_map = defaultdict(Counter)
            sum_latency = dict([(variant1, 0), (variant2, 0)])
            num_acks = dict([(variant1, 0), (variant2, 0)])
            for line in map(lambda line: line.split(" "), in_file):
                if len(line) and line[0] == '-' and line[4] == 'tcp':
                    if line[7] == '1' and line[2] == '0' and line[3] == '1':
                        seq_map[variant1][line[10]] = float(line[1])
                    elif line[7] == '3' and line[2] == '4' and line[3] == '1':
                        seq_map[variant2][line[10]] = float(line[1])
                elif len(line) and line[0] == 'r' and line[4] == 'ack':
                    if line[7] == '1' and line[2] == '1' and line[3] == '0':
                        sum_latency[variant1] += float(line[1]) - float(seq_map[variant1][line[10]])
                        num_acks[variant1] += 1
                    elif line[7] == '3' and line[2] == '1' and line[3] == '4':
                        sum_latency[variant2] += float(line[1]) - float(seq_map[variant2][line[10]])
                        num_acks[variant2] += 1
            rtts[cbr][variant1] = (sum_latency[variant1] / num_acks[variant1])
            rtts[cbr][variant2] = (sum_latency[variant2] / num_acks[variant2])

    print 'cbr\t'+'\t'.join(sorted(rtts.values()[0].keys()))
    for cbr,variants in sorted(rtts.items(), key=lambda item: int(item[0])):
        row = "%s" % cbr
        for variant,count in sorted(variants.items(), key=lambda item: item[0]):
            row += "\t%.2f" % float(count*1000)
        print row

if __name__ == "__main__":
    main()
