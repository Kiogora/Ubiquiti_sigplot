#!/bin/bash

dB=`fab --password=ubnt host_type | grep dBm | sed -e 's/[^0-9]/ /g' \
-e 's/^ *//g' \
-e 's/ *$//g' \
| tr -s ' ' \
| sed 's/ /\n/g' \
| sed -n '7p'`

time_now=`date | sed -e 's/[^0-9]/ /g' \
-e 's/^ *//g' \
-e 's/ *$//g' \
| tr -s ' ' \
| sed 's/ /,/g'`

delimiter=','
csv=$dB$delimiter$time_now

echo $csv >> signal.csv
