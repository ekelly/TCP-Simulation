
set kb kb
set rate $udprate$kb

#Define different colors for data flows (for NAM)
$ns color 1 Blue
$ns color 2 Red
$ns color 3 Green

#Define a 'finish' procedure
proc finish {} {
        global ns nf
        $ns flush-trace
        #Close the NAM trace file
        close $nf
        #Execute NAM on the trace file
        # exec nam out.nam &
        exit 0
}

#Create six nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

#Create links between the nodes
$ns duplex-link $n0 $n1 10Mb 10ms DropTail
$ns duplex-link $n1 $n2 10Mb 10ms DropTail
$ns duplex-link $n2 $n3 10Mb 10ms DropTail
$ns duplex-link $n4 $n1 10Mb 10ms DropTail
$ns duplex-link $n5 $n2 10Mb 10ms DropTail

#Set Queue Size of link (n2-n3) to 10
$ns queue-limit $n2 $n3 10

#Give node position (for NAM)
$ns duplex-link-op $n0 $n1 orient right-down
$ns duplex-link-op $n4 $n1 orient right-up
$ns duplex-link-op $n1 $n2 orient right
$ns duplex-link-op $n2 $n3 orient right-up
$ns duplex-link-op $n2 $n5 orient right-down

#Monitor the queue for link (N2-N3). (for NAM)
$ns duplex-link-op $n2 $n3 queuePos 0.5


################################################
#       Setup a Constant Bit Rate flow         #
################################################

if { $udprate != 0 } {
# Setup N2
set udp0 [new Agent/UDP]
$ns attach-agent $n1 $udp0
# Attach CBR to UDP connection on N2
set cbr0 [new Application/Traffic/CBR]
$cbr0 attach-agent $udp0
$cbr0 set type_ CBR
$cbr0 set packet_size_ 1000
$cbr0 set rate_ $rate
$cbr0 set random_ false

# Setup N3
set null0 [new Agent/Null]
$ns attach-agent $n2 $null0

# Connect N2 to N3
$ns connect $udp0 $null0
$udp0 set fid_ 2
}

################################################
#          Setup the TCP connection            #
################################################

$tcp0 set class_ 2
$ns attach-agent $n0 $tcp0
set sink0 [new Agent/TCPSink]
$ns attach-agent $n3 $sink0
$ns connect $tcp0 $sink0
$tcp0 set fid_ 1
$tcp0 set window_ 10000

#Setup a FTP over TCP connection
set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0
$ftp0 set type_ FTP

################################################
#        Setup the 2nd TCP connection          #
################################################

#Setup a TCP connection
$tcp1 set class_ 2
$ns attach-agent $n4 $tcp1
set sink1 [new Agent/TCPSink]
$ns attach-agent $n5 $sink1
$ns connect $tcp1 $sink1
$tcp1 set fid_ 3
$tcp1 set window_ 10000

#Setup a FTP over TCP connection
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set type_ FTP

################################################
#                 Setup events                 #
################################################

#Schedule events for the CBR and TCP agents
if { $udprate != 0 } {
$ns at 0.0 "$cbr0 start"
}
$ns at 0.0 "$ftp0 start"
$ns at 0.0 "$ftp1 start"

#Detach tcp and sink agents (not really necessary)
# $ns at 5.0 "$ns detach-agent $n0 $tcp0 ; $ns detach-agent $n3 $sink0"

#Call the finish procedure after 5 seconds of simulation time
$ns at 10.0 "finish"

#Print CBR packet size and interval
puts -nonewline "."

#Run the simulation
$ns run

