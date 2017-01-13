#!/usr/bin/python
#coding:utf-8

import requests
from bs4 import BeautifulSoup

class Number:
    def Get(self,term):
        Res =requests.get("http://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx")
        Soup = BeautifulSoup(Res.text,"html.parser")

        # Taiwan Lottory page is using "POST" method, so needs to get viewstate and eventvalidation.
        # Then, combine these with other payload data to communicate.
        viewstate = Soup.findAll(attrs={"name": "__VIEWSTATE"})[0]['value']
        eventvalidation = Soup.findAll(attrs={"name": "__EVENTVALIDATION"})[0]['value']

        # Payload data
        payload = {
        '__VIEWSTATE':viewstate,
		'__VIEWSTATEGENERATOR':'C3E8EA98',
		'__EVENTVALIDATION':eventvalidation,
		'Lotto649Control_history$DropDownList1':'2',
		'Lotto649Control_history$chk':'radNO',
		'Lotto649Control_history$txtNO':term,
		'Lotto649Control_history$btnSubmit':'查詢'
        }

        PostRes = requests.post("http://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx", data = payload)
        PostSoup = BeautifulSoup(PostRes.text, "html.parser")

        # The beginning of lottory number
        #print ("大樂透第 {} 期開獎號碼：".format(term)),

        i = 0
        LottoryList = []

        # List all of general lottory number

        for Black in PostSoup.select('.font_black14b_center'):
            i = i + 1
            if (i > 6 and i <= 12):
                BlackNum = Black.select('span')[0].text
                LottoryList.append(BlackNum)

        RedNum = PostSoup.select('.font_red14b_center , span')[0].text
        LottoryList.append(RedNum)

        return LottoryList


    def Compare(self, Owned, DrawNum):

        BingoRed = 0
        BingoBlack = 0

        for i in range(6):
            if (Owned[i] == DrawNum[6]):
                BingoRed = 1
            for j in range(6):
                if (Owned[i] == DrawNum[j]):
                    BingoBlack +=1

        if BingoBlack == 6:
            print "您中頭獎了啊！見者有份"
        elif BingoBlack == 5 and BingoRed == 1:
            print "您中二獎了啊！"
        elif BingoBlack == 5 and BingoRed == 0:
            print "您中三獎了啊！"
        elif BingoBlack == 4 and BingoRed == 1:
            print "您中四獎了啊！"
        elif BingoBlack == 4 and BingoRed == 0:
            print "您中五獎了啊！"
        elif BingoBlack == 3 and BingoRed == 1:
            print "您中六獎了啊！"
        elif BingoBlack == 2 and BingoRed == 1:
            print "您中七獎了啊！"
        elif BingoBlack == 3:
            print "您中八獎了啊！"
        else:
            print "非常抱歉！再接再厲！"

        print "====================="
        #print BingoBlack,BingoRed