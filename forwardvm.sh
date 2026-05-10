#!/bin/bash

serverbip=`virsh net-dhcp-leases  default | grep serverb  | awk '{print $5}' | awk -F'/' '{print $1}'`
iptables -I FORWARD -o private -d  $serverbip  -j ACCEPT
iptables -t nat -I PREROUTING -p tcp --dport 24220 -j DNAT --to $serverbip:22
