#!/usr/bin/python

from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("-s", "--start", dest="start", type="int",
                          help="start at this mb/s for the UDP stream")
parser.add_option("-e", "--end", dest="end", type="int",
                          help="end at this mb/s for the UDP stream")
parser.add_option("-i", "--increment", dest="inc", type="int",
                          help="how fast do we increment the mb/s")

(options, args) = parser.parse_args()

settings = """
set udprate %(mb)smb

#Open the NAM trace file
set nf [open out-%(mb)s.nam w]

"""

experiments = []

if options.start and options.end and options.inc:
    for i in range(options.start, options.end + options.inc, options.inc):
        with open("experiment%s.tcl" % i, "a+") as experiment:
            experiment.write(settings % {"mb": i})
            with open("template.tcl") as template:
                for line in template:
                    experiment.write(line)
                experiment.close()
                template.close()
            experiments.append("experiment%s.tcl" % i)
else:
    parser.print_help()

for experiment in experiments:
    os.system("/course/cs4700f12/ns-allinone-2.35/bin/ns %s" % experiment)
    os.remove(experiment)
