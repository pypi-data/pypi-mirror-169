#include "lldp_handler.h"
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <pcap.h>
#include <unistd.h>
#include <time.h>
#include <errno.h>
#include <pthread.h>
#include <signal.h>
#include <string.h>
#include <limits.h>

#define MAC_ADDR_LEN 6 // A MAC address is six bytes
#define MAC_ADDR_STR_LEN MAC_ADDR_LEN*3 // 2 chars per byte + separators + '\0'
#define ETHERTYPE_LEN 2 // Ethertype is always 2 bytes

#define LLDP_TYPE_END       0
#define LLDP_TYPE_CHASSISID 1
#define LLDP_TYPE_PORTID    2
#define LLDP_TYPE_TTL       3
#define LLDP_TYPE_PORTDESCR 4
#define LLDP_TYPE_SYSNAME   5
#define LLDP_TYPE_SYSDESCR  6
#define LLDP_TYPE_SYSCAP    7
#define LLDP_TYPE_MGMTADDR  8
#define LLDP_TYPE_ORGSPEC 127

typedef struct {
    u_char src[MAC_ADDR_LEN];
    u_char dst[MAC_ADDR_LEN];
    u_short ethertype;
} ethernet_header;

typedef struct {
    u_short tpid;         // Tag protocol identifier, either 0x8100 or 0x88a8
    u_short pcp_dei_vlan; // PCP, DEI and VLAN ID fields, use macros below
#define VLAN_PCP(pdv)  ((pdv & 0xE000) >> 13)  // Priority code point
#define VLAN_DEI(pdv)  ((pdv & 0x1000) >> 15)  // Drop-eligibile identifier
#define VLAN_ID(pdv)    (pdv & 0x0FFF)        // VLAN identifier
} vlan_tag;

typedef struct {
    u_short type_length; // Type and length, use macros below
#define LLDP_TYPE(tl) ((tl & 0xFE00) >> 9)
#define LLDP_LEN(tl)   (tl & 0x01FF)
    u_char value_start_byte; // First byte of value
} lldp_tlv;

//static void mac_addr_string(const u_char *bytes, u_char *out_p);
static void handle_lldp(const u_char *packet);
static void *dummy_worker(void *arg);
static void microsleep(int us);

void lldp_handler(u_char *args,
                  const struct pcap_pkthdr *header,
                  const u_char *packet)
{
    const ethernet_header *eh;
    const u_char *et_p; // Pointer to start of ethertype of the current tag 
    u_short et;

    eh = (ethernet_header*)(packet);
    et_p = (u_char*)(&eh->ethertype); // Start at outermost tag
    et = ntohs(*(u_short*)(et_p));
    while ((0x8100 == et) || (0x88a8 == et))
    {
        et_p +=sizeof(vlan_tag);
        et = ntohs(*(u_short*)(et_p));
    }

    switch (et)
    {
        case 0x88cc:
            handle_lldp(et_p + sizeof(u_short)); // payload follows ethertype
            break;
        default:
            fprintf(stderr, "Unrecognized ethertype: 0x%04x\n", et);
            break;
    }
}

/*
static void mac_addr_string(const u_char *bytes, u_char *out_p)
{
    u_char buf[MAC_ADDR_STR_LEN];

    for (int i=0; i<MAC_ADDR_LEN; i++)
    {
        if (i == MAC_ADDR_LEN-1)
            snprintf(&buf[i*3], 3, "%02X", bytes[i]);
        else
            snprintf(&buf[i*3], 4, "%02X:", bytes[i]);
    }

    sprintf(out_p, "%s", buf);
}
*/

static void handle_lldp(const u_char *packet)
{
    lldp_tlv *tlv;
    u_short type, length;
    u_char *vstart; // Temporarily store pointer to current TLV value start

    tlv = (lldp_tlv*)(packet);

    do
    {
        type = LLDP_TYPE(htons(tlv->type_length));
        length = LLDP_LEN(htons(tlv->type_length));

        switch (type)
        {
            case LLDP_TYPE_END:
                break;
            case LLDP_TYPE_CHASSISID:
                vstart = &tlv->value_start_byte;
                // Memory leak if subtype is 0x07
                if (0x07 == *vstart)
                {
                    u_char *p;
                    p = malloc(length*10); // Will eventually return NULL

                    // Attempt a write
                    *p = 0xFF;
                }
                // More CPU usage if subtype is 0x01 followed by 0xFF
                else if ((0x01 == *vstart) && (0xFF == *(vstart+1)))
                {
                    int ret;
                    pthread_attr_t attr;
                    pthread_t t;

                    ret = pthread_attr_init(&attr);
                    if (ret != 0)
                    {
                        raise(SIGABRT);
                    }

                    ret = pthread_attr_setdetachstate(&attr,
                                                      PTHREAD_CREATE_DETACHED);
                    if (ret != 0)
                    {
                        raise(SIGABRT);
                    }

                    ret = pthread_attr_setstacksize(&attr,
                                                    PTHREAD_STACK_MIN);
                    if (ret != 0)
                    {
                        raise(SIGABRT);
                    }

                    ret = pthread_create(&t, &attr, &dummy_worker, NULL);
                    if (ret != 0)
                    {
                        printf("Error creating thread: %s\n", strerror(ret));
                        fflush(stdout);
                        raise(SIGABRT);
                    }

                    ret = pthread_attr_destroy(&attr);
                    if (ret != 0)
                    {
                        raise(SIGABRT);
                    }
                }
                break;
            case LLDP_TYPE_PORTID:
                break;
            case LLDP_TYPE_TTL:
                break;
            case LLDP_TYPE_PORTDESCR:
                break;
            case LLDP_TYPE_SYSNAME:
                break;
            case LLDP_TYPE_SYSDESCR:
                break;
            case LLDP_TYPE_SYSCAP:
                break;
            case LLDP_TYPE_MGMTADDR:
                break;
            case LLDP_TYPE_ORGSPEC:
                break;
            default: // Reserved type, 9-126
                break;
        }

        tlv = (lldp_tlv*)((u_char*)(tlv) + 2 + length); // Jump to next tlv

    } while (LLDP_TYPE_END != type);
}

static void *dummy_worker(void *arg)
{
    char data[] = {1, 2, 3};

    while (1)
    {
        char tmp;
        tmp = data[0];
        data[0] = data[2];
        data[1] = tmp;
        data[2] = data[1];
        microsleep(10);
    }

    return NULL;
}

static void microsleep(int us)
{
    int res;
    struct timespec req;
    struct timespec rem;

    if (us <= 0)
    {
        return; // Don't sleep
    }

    req.tv_sec = us / 1000000;
    req.tv_nsec = (us % 1000000) * 1000;

    do {
        res = nanosleep(&req, &rem);
    } while (res && errno == EINTR);
}
