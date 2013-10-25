#!/usr/bin/python
import sys
import fileinput
from collections import Counter,defaultdict

# run with ./throughputbycbr.py Reno-Reno*
#       or ./throughputbycbr.py Vegas-Vegas*, etc

def main():
    cbrs = defaultdict(Counter)
    for in_name in sys.argv[1:]:
        with open(in_name) as in_file:
            cbr = int(in_name.split('-')[2].split('.')[0])
            first_var = in_name.split('-')[0] + "-1"
            second_var = in_name.split('-')[1] + "-2"
            for line in map(lambda line: line.split(" "), in_file):
                if len(line) and line[0] == 'r' and line[4] == 'tcp' and line[2] == '2':
                    if line[3] == '3':
                        cbrs[cbr][first_var] += int(line[5])
                    elif line[3] == '5':
                        cbrs[cbr][second_var] += int(line[5])

    print 'cbr\t'+'\t'.join(sorted(cbrs.values()[0].keys()))
    for cbr,variants in sorted(cbrs.items(), key=lambda item: int(item[0])):
        row = "%s" % cbr
        for variant,count in sorted(variants.items(), key=lambda item: item[0]):
            row += "\t%s" % str(count/1000)
        print row

if __name__ == "__main__":
    main()
