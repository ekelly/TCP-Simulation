#!/usr/bin/python

from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("-s", "--start", dest="start", type="int", default=1,
                          help="start at this mb/s for the UDP stream")
parser.add_option("-e", "--end", dest="end", type="int", default=10,
                          help="end at this mb/s for the UDP stream")
parser.add_option("-i", "--increment", dest="inc", type="int", default=1,
                          help="how fast do we increment the mb/s")

(options, args) = parser.parse_args()

settings = """
set udprate %(kb)skb

#Open the NAM trace file
set nf [open %(ttype)s-%(kb)s.tr w]

#Create a simulator object
set ns [new Simulator]
$ns trace-all $nf

#Setup a TCP connection
set tcp0 [new Agent/%(tcp)s]

"""

experiments = []

if options.start and options.end and options.inc:
    for i in range(options.start, options.end + options.inc, options.inc):
        i = i*100
        for tcptype in ["TCP", "TCP/Reno", "TCP/Newreno", "TCP/Vegas"]:
            ttype = "tahoe" if tcptype.find("/") == -1 else tcptype.split("/")[1].lower()
            with open("experiment%s-%s.tcl" % (i, ttype), "a+") as experiment:
                experiment.write(settings % {"kb": i, "tcp": tcptype, "ttype": ttype})
                with open("template.tcl") as template:
                    for line in template:
                        experiment.write(line)
                    experiment.close()
                    template.close()
                experiments.append("experiment%s-%s.tcl" % (i, ttype))
else:
    parser.print_help()

for experiment in experiments:
    os.system("ns %s" % experiment)
    os.remove(experiment)

print ""
