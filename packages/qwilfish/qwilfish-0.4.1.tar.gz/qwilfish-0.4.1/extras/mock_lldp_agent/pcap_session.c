#include <stdio.h>
#include <pcap.h>
#include <signal.h>
#include <stdlib.h>
#include "lldp_handler.h"

#define TIMEOUT_MS 10000 // Ten second timeout if no packets are seen
#define PROMISC 1
#define FILTER_EXP "ether proto 0x88cc || vlan" // LLDP packets

void signal_handler(int sig)
{
    switch (sig) {
        case SIGTERM:
            exit(0);
        default:
            exit(-1);
    }
}

int main(int argc, char *argv[])
{
    char *dev = argv[1]; // CLI argument (hopefully a valid interface)
    char errbuf[PCAP_ERRBUF_SIZE]; // Error string
    pcap_t *handle; // Session handle
    struct bpf_program fp; // The compiled filter
    //struct pcap_pkthdr header; // Header with information by pcap
    //const u_char *packet; // The packet!

    // Register signal handler
    signal(SIGTERM, signal_handler);

    // Start a session (open the device)
    handle = pcap_open_live(dev, BUFSIZ, PROMISC, TIMEOUT_MS, errbuf);
    if (NULL == handle)
    {
        fprintf(stderr, "Couldn't open device %s: %s\n", dev, errbuf);
        return(2);
    }
    // Make sure that it is an Ethernet device
    if (pcap_datalink(handle) != DLT_EN10MB)
    {
        fprintf(stderr, "Device %s doesn't provide Ethernet headers!\n", dev);
        return(2);
    }
    // Compile and install the filter
    if (pcap_compile(handle, &fp, FILTER_EXP, 0, PCAP_NETMASK_UNKNOWN) == -1)
    {
        fprintf(stderr,
                "Couldn't compile filter %s: %s\n",
                FILTER_EXP,
                pcap_geterr(handle));
        return(2);
    }
    if (pcap_setfilter(handle, &fp) == -1)
    {
        fprintf(stderr,
                "Couldn't install filter %s: %s\n",
                FILTER_EXP,
                pcap_geterr(handle));
        return(2);
    }

    // Capture a packet!
    printf("Entering pcap_loop...\n");
    (void) pcap_loop(handle, -1, lldp_handler, NULL);

    // Close session
    pcap_close(handle);

    return(0);
}
