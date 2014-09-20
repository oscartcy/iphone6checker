#!/bin/bash
echo 'Start Running'
curl https://reserve.cdn-apple.com/HK/en_HK/reserve/iPhone/availability.json | grep 'true'
while [ $? -ne 0 ];
do
curl https://reserve.cdn-apple.com/HK/en_HK/reserve/iPhone/availability.json | grep 'true'
done

echo 'Available!!!!!'
