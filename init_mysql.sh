#!/bin/bash

p=`grep 'password is generated for root@localhost' /var/log/mysqld.log | cut -d ' ' -f 13`  # mysql8
mysqladmin -uroot -p"$p" password 'Admin@123'
