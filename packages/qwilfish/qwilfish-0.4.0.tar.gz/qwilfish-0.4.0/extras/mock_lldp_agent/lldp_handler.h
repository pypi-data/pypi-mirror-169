#ifndef __LLDP_HANDLER__
#define __LLDP_HANDLER__
#include <pcap.h>

void lldp_handler(u_char *args,
                  const struct pcap_pkthdr *header,
                  const u_char *packet);

#endif
