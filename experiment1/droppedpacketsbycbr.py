#!/usr/bin/python
import sys
import fileinput
from collections import Counter,defaultdict

def main():
    cbrs = defaultdict(lambda: dict([('reno',0),('tahoe',0),('newreno',0),('vegas',0)]))
    sent = defaultdict(lambda: dict([('reno',0),('tahoe',0),('newreno',0),('vegas',0)]))
    for tcp_variant in ['reno', 'tahoe', 'newreno', 'vegas']:
        # print tcp_variant
        # read $tcp_variant-*.tr, count number of packets acked / number of seconds
        # 0.0   123
        # 0.1   102
        # ...   ...
        # write to tcp_variant-throughput.txt
        for cbr in range(0,10500,500):
            with open("%s-%s.tr" % (tcp_variant, cbr)) as in_file:
                for line in map(lambda line: line.split(" "), in_file):
                    if len(line) and line[0] == 'd' and line[4] == 'tcp':
                        cbrs[cbr][tcp_variant] += 1
                    elif len(line) and line[4] == 'tcp' and line[2] == '0' and line[3] == '1' and line[0] == '-':
                        sent[cbr][tcp_variant] += 1

    print 'cbr\t'+'\t'.join(sorted(cbrs.values()[0].keys()))
    for cbr,variants in sorted(cbrs.items(), key=lambda item: int(item[0])):
        row = "%s" % cbr
        for variant,count in sorted(variants.items(), key=lambda item: item[0]):
            percent = (100.0 * (float(count) / float(sent[cbr][variant])))
            row += "\t%.4f" % percent
        print row

if __name__ == "__main__":
    main()
