#!/bin/bash
echo 'Start Running'
curl https://reserve.cdn-apple.com/HK/en_HK/reserve/iPhone/availability.json | grep -i 'true'
while [ $? -ne 0 ];
do
curl https://reserve.cdn-apple.com/HK/en_HK/reserve/iPhone/availability.json | grep -i 'true'
done

echo 'Available!!!!!'
echo -e "\007"
