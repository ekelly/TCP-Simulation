#!/usr/bin/python

import os

settings = """

#Open the NAM trace file
set nf [open %(ttype)s-%(qtype)s.tr w]

#Create a simulator object
set ns [new Simulator]
$ns trace-all $nf

#Setup a TCP connection
set tcp0 [new Agent/TCP/%(ttype)s]

"""

experiments = []

for tcptype in ["Reno", "Sack1"]:
    for queue_type in ["DropTail", "RED"]:
        filename = "experiment-%s-%s.tcl" % (tcptype, queue_type)
        with open(filename, "a+") as experiment:
            experiment.write(settings % {"ttype": tcptype, "qtype": queue_type})
            with open("template.tcl") as template:
                for line in template:
                    experiment.write(line)
                experiment.close()
                template.close()
            experiments.append(filename)

for experiment in experiments:
    os.system("ns %s" % experiment)
    os.remove(experiment)

print ""
