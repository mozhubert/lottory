#!/usr/bin/python
#coding:utf-8

import GetNumber,requests
from bs4 import BeautifulSoup

lottory = GetNumber.Number()

#term = int(raw_input("請輸入起始期數:"))
#period = int(raw_input("請輸入購買期數:"))
#owned = raw_input("請輸入購買獎號:")

# 判斷輸入起始期數是否為九位正整數
while True:
    term = raw_input("請輸入起始期數:")
    if term.isdigit() and len(term)==9:
        break
    else:
        print "請輸入九位數正整數 (ex: 105000088)"
term=int(term)

# 判斷輸入購買期數是否為正整數
while True:
    period = raw_input("請輸入購買期數:")
    if period.isdigit():
        break
period=int(period)

while True:
    inputowned = raw_input("請輸入購買獎號:")
    owned = inputowned.split(',')
    if len(owned) == 6:
        if owned[0].isdigit() and owned[1].isdigit() and owned[2].isdigit() and owned[3].isdigit() and owned[4].isdigit() and owned[5].isdigit():
            break
owned = sorted(owned)

for i in range(0,period):
    #print term+i
    GotLottory = lottory.Get(term+i)

    print ("大樂透第 {} 期開獎號碼：".format(term+i)),
    print GotLottory[0],GotLottory[1],GotLottory[2],GotLottory[3],GotLottory[4],GotLottory[5],
    print "特別號碼：", GotLottory[6]
    lottory.Compare(owned,GotLottory)