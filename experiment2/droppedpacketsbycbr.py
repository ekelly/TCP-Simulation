#!/usr/bin/python
import sys
import fileinput
from collections import Counter,defaultdict

def f_to_name(flowid, match):
    return match[0 if flowid == 1 else 1]

def main():
    # variant names
    variant1 = ""
    variant2 = ""

    #drpd = defaultdict(lambda: dict([('1',0),('3',0)]))
    drpd = defaultdict(Counter)
    sent = defaultdict(Counter)
    for in_name in sys.argv[1:]:
        with open(in_name) as in_file:
            cbr = int(in_name.split('-')[2].split('.')[0])
            variant1 = in_name.split('-')[0].split('.')[0]
            variant2 = in_name.split('-')[1].split('.')[0]
            if variant1 == variant2:
                variant1 += "-1"
                variant2 += "-2"
            drpd[cbr]['1'] = 0
            drpd[cbr]['3'] = 0
            for line in map(lambda line: line.split(" "), in_file):
                if len(line) and line[0] == 'd' and line[4] == 'tcp':
                    drpd[cbr][line[7]] += 1
                elif len(line) and line[4] == 'tcp' and (line[2] == '0' or line[2] == '4') and line[3] == '1' and line[0] == '-':
                    sent[cbr][line[7]] += 1

    print "cbr\t%s\t%s" % (variant1, variant2)
    for cbr,flows in sorted(sent.items(), key=lambda item: int(item[0])):
        row = "%s" % cbr
        for flow,count in flows.items():
            dropped = float(drpd[cbr][flow])
            percent = (99.0 * (dropped / count))
            row += "\t%.3f" % percent
        print row

if __name__ == "__main__":
    main()
