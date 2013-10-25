#!/usr/bin/python

import os

settings = """
set udprate %(cbr)i

#Open the NAM trace file
set nf [open %(tcp1)s-%(tcp2)s-%(cbr)i.tr w]

#Create a simulator object
set ns [new Simulator]
$ns trace-all $nf

#Setup a TCP connection
set tcp0 [new Agent/TCP/%(tcp1)s]
set tcp1 [new Agent/TCP/%(tcp2)s]

"""

matches = [("Reno", "Reno"), ("Reno", "Newreno"), 
            ("Newreno", "Newreno"),
           ("Vegas", "Vegas"), ("Newreno", "Vegas")]
experiments = []

for match in matches:
    for cbr in range(0, 10500, 500):
        type1 = match[0].lower()
        type2 = match[1].lower()
        filename = "experiment.%s-%s.%i.tcl" % (type1, type2, cbr)
        with open(filename, "a+") as experiment:
            experiment.write(settings % {"tcp1": match[0], "tcp2": match[1], "cbr": cbr})
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
