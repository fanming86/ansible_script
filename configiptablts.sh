#!/bin/bash

iptables -F
iptables -t nat -F PREROUTING
iptables -I FORWARD -o private -d  192.168.100.10 -j ACCEPT
iptables -t nat -I PREROUTING -p tcp --dport 24210 -j DNAT --to 192.168.100.10:22
iptables -t nat -I PREROUTING -p tcp --dport 24220 -j DNAT --to 192.168.100.20:22

