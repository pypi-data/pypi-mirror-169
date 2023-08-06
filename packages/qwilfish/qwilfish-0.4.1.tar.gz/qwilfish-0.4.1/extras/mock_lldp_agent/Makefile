CROSS_TOOL =
CFLAGS = --coverage -Wall -Werror -g
CC_C = $(CROSS_TOOL)gcc
NO_LINK = -c
LINK_PCAP_SESSION = -lpcap -pthread
LINK_BUGGY_LLDP_PM = -lcap

all: buggy_lldp_pm pcap_session

buggy_lldp_pm: buggy_lldp_pm.c
	$(CC_C) $(CFLAGS) buggy_lldp_pm.c -o buggy_lldp_pm $(LINK_BUGGY_LLDP_PM)

pcap_session: pcap_session.o lldp_handler.o
	$(CC_C) $(CFLAGS) pcap_session.o lldp_handler.o -o pcap_session $(LINK_PCAP_SESSION)

pcap_session.o: pcap_session.c
	$(CC_C) $(CFLAGS) $(NO_LINK) pcap_session.c

lldp_handler.o: lldp_handler.c lldp_handler.h
	$(CC_C) $(CFLAGS) $(NO_LINK) lldp_handler.c

setcap: buggy_lldp_pm
	sudo setcap cap_net_raw=p buggy_lldp_pm # Must permit in parent's file
	sudo setcap cap_net_raw=ei pcap_session # Can inherit and is effective

clean:
	-rm buggy_lldp_pm pcap_session *.o
