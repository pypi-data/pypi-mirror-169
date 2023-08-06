#! /bin/bash

TXTFILE="${1}.bin"
PCAPFILE="${1}.pcap"

cat $1 | tr -d '\n' | perl -lpe '$_=pack"B*",$_' > $TXTFILE
od -Ax -tx1 -v $TXTFILE | text2pcap - $PCAPFILE

rm ${TXTFILE}
