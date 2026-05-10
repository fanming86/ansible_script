#!/bin/bash

ipaddress=`ip -4 a s ens192 | grep inet | awk '{print $2}' | awk -F / '{print $1}'`
cd /opt/MicroserviceMall/portal-service/
grep -r '172.31.20.200'  ./  | awk -F : '{print $1}' | while read i; do echo $i; sed -i "s/172.31.20.200/$ipaddress/g" $i ; done


cd /opt/MicroserviceMall/portal-service/target/

jar xf portal-service.jar

grep -r '172.31.20.200'  ./  | awk -F : '{print $1}' | while read i; do echo $i; sed -i "s/172.31.20.200/$ipaddress/g" $i ; done


jar uf portal-service.jar  BOOT-INF/classes/static/js/productList.js BOOT-INF/classes/static/js/orderList.js
