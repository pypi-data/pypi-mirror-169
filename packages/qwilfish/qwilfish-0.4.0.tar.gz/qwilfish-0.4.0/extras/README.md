# Extras
Here are some extras that are related the Qwilfish package, one way or another.

## generate\_pcap.sh
A simple script that can be used to convert a textfile with a binary string
into a .pcap file.

## mock\_lldp\_agent
A mock LLDP agent written in C. It uses libpcap to sniff for VLAN tagged frames
or LLDP packets. LLDP packets will be "parsed". Most of the time it does
nothing, but for certain LLDP frames it will deliberately cause a SEGV.
Can be used as a dummy target for Qwilfish.

## quickplot.py
A very basic script for plotting data from a sqlite3 db, such as the ones
created by qwilfish.

## qwilfish-feedback-interface.yang
An attempt at defining the feedback interface using YANG, rather than protobuf.
Might become a feature in the distant future as this would allow for greater
flexibility for the feedback interface (NETCONF, RESTCONF, gNMI) but for now
it's just a relic.

## repo\_logo.png
A logo that can be used for this repo.
