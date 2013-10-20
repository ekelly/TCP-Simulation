#!/usr/bin/python

import os

settings = """

#Open the NAM trace file
set nf [open %(tcp1)s-%(tcp2)s.nam w]

#Create a simulator object
set ns [new Simulator]
$ns namtrace-all $nf

#Setup a TCP connection
set tcp0 [new Agent/TCP/%(tcp1)s]
set tcp1 [new Agent/TCP/%(tcp2)s]

"""

matches = [("Reno", "Reno"), ("Reno", "Newreno"), 
           ("Vegas", "Vegas"), ("Newreno", "Vegas")]
experiments = []

for match in matches:
    type1 = match[0].lower()
    type2 = match[1].lower()
    filename = "experiment.%s-%s.tcl" % (type1, type2)
    with open(filename, "a+") as experiment:
        experiment.write(settings % {"tcp1": match[0], "tcp2": match[1]})
        with open("template.tcl") as template:
            for line in template:
                experiment.write(line)
            experiment.close()
            template.close()
        experiments.append(filename)

for experiment in experiments:
    os.system("/course/cs4700f12/ns-allinone-2.35/bin/ns %s" % experiment)
    os.remove(experiment)
