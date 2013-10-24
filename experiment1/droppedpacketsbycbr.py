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
                for line in map(lambda line: line.split(" "), in_file):
                    if len(line) and line[0] == 'd' and line[4] == 'tcp':
                        cbrs[cbr][tcp_variant] += 1

    print 'cbr\t'+'\t'.join(sorted(cbrs.values()[0].keys()))
    for cbr,variants in sorted(cbrs.items(), key=lambda item: int(item[0])):
        row = "%s" % cbr
        for variant,count in sorted(variants.items(), key=lambda item: item[0]):
            row += "\t%s" % count
        print row

if __name__ == "__main__":
    main()
