#!/bin/bash
echo 'Start Running'
x=''
while [ "$x" != '1' ];
do
    x=$(curl -o - 'https://reserve.cdn-apple.com/HK/zh_HK/reserve/iPhone/availability.json' -o -  | iconv -f windows-1251 | tr -dc '[:print:]'| python parse.py)
    echo ${x}
done

echo 'Available!!!!!'
echo -e "\007"
