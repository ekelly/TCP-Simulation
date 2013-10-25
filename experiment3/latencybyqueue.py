#!/usr/bin/python
import sys
import fileinput
from collections import Counter,defaultdict

# run with ./latencybyqueue.py Reno-*
#       or ./latencybyqueue.py Sack1-*, etc

def main():
    sent_map = defaultdict(dict)
    latency_map = defaultdict(dict)
    for in_name in sys.argv[1:]:
        with open(in_name) as in_file:
            qtype = in_name.split('-')[1].split('.')[0]
            for line in map(lambda line: line.split(" "), in_file):
                if (len(line) and
                        line[0] == '-' and
                        line[4] == 'tcp' and
                        line[2] == '0' and
                        line[3] == '1'):
                    sent_map[qtype][line[10]] = float(line[1])
                elif (len(line) and
                        line[0] == 'r' and
                        line[4] == 'ack' and
                        line[2] == '1' and
                        line[3] == '0'):
                    latency_map[qtype][line[10]] = (int(sent_map[qtype][line[10]]*10),
                                                float(line[1]) - sent_map[qtype][line[10]])

    
    period_latency = defaultdict(lambda: defaultdict(float))
    period_total = defaultdict(Counter)
    for qtype,packets in latency_map.items():
        for seq_no,(start_time,latency) in packets.items():
            period_latency[start_time][qtype] += latency
            period_total[start_time][qtype] += 1

    print "Time\tRED\tDropTail"
    for start_time,latencies in sorted(period_latency.items(), key=lambda per: per[0]):
        row = "%s\t" % (start_time/10.0)
        for qtype in ['RED', 'DropTail']:
            if qtype in latencies:
                row += "%s\t" % (1000*latencies[qtype] / period_total[start_time][qtype])
            else:
                row += "?\t"
        print row

# seq# -> (nearest 1/10 second, RTT)
# want dict from time in 1/10 second to latency for packets sent

if __name__ == "__main__":
    main()
