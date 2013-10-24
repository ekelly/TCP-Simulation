#!/usr/bin/python
import sys
import fileinput
from collections import Counter,defaultdict

def main():
    cbrs = defaultdict(Counter)
    for tcp_variant in ['reno', 'tahoe', 'newreno', 'vegas']:
        print tcp_variant
        # read $tcp_variant-*.tr, count number of packets acked / number of seconds
        # 0.0   123
        # 0.1   102
        # ...   ...
        # write to tcp_variant-throughput.txt
        for cbr in range(100,1100,100):
            with open("%s-%s.tr" % (tcp_variant, cbr)) as in_file:
                start_seq = dict()
                end_seq = dict()
                for line in map(lambda line: line.split(" "), in_file):
                    if len(line) and line[0] == '-' and line[4] == 'tcp' and line[2] == '0' and line[3] == '1':
                        start_seq[line[10]] = line[1] 
                        #cbrs[cbr][tcp_variant][line[10]] = line[1]
                    elif len(line) and line[0] == 'r' and line [4] == 'ack' and line[2] == '1' and line[3] == '0':
                        end_seq[line[10]] = line[1]
                running_latency = 0
                num_acks = 0
                for seq in end_seq.keys():
                    latency = float(end_seq[seq]) - float(start_seq[seq])
                    running_latency += latency
                    num_acks += 1 
                cbrs[cbr][tcp_variant] = running_latency / num_acks

    print 'cbr\t'+'\t'.join(sorted(cbrs.values()[0].keys()))
    for cbr,variants in sorted(cbrs.items(), key=lambda item: int(item[0])):
        row = "%s" % cbr
        for variant,count in sorted(variants.items(), key=lambda item: item[0]):
            row += "\t%s" % count
        print row

if __name__ == "__main__":
    main()
