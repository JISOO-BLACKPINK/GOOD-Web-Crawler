import re
import urllib.error
import urllib.request
import urllib.response
from bs4 import BeautifulSoup
def main():
    sa=0
    while True:
        a=input("请输入要爬取的网页个数：1-3100\n")
        sa=int(a)
        if sa>3100:
            print("数值过大，请重新输入")
        elif sa<1:
            print("数值过小！请重新输入")
        else:
            break
    dataknow(sa)
#数据解析
def dataknow(asdas):
    jak=0
    a=0
    lax=[]
    for i in range(0,asdas):
        a+=1
        num=10900-a
        strn=str(num)
        turl="http://20a5.com/html/article/index"+strn+".html"
        print(turl)
        au=gethtml(turl)
        bs=BeautifulSoup(au,"html.parser")
        lists=bs.find_all("img")
        for k in lists:
            lax.append(k.get("src"))
        for dw in lax:
            jak+=1
            with open("D:\\oprea\\"+str(jak)+".jpg","wb") as imgs:
                lka=urllib.request.urlopen(dw)
                print("正在下载第"+str(jak)+"张色图")
                imgs.write(lka.read())
                print("下载成功")
#获取源代码        
def gethtml(url):
    head={"users":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    req=urllib.request.Request(url,headers=head)
    p=""
    try:
        rep=urllib.request.urlopen(req)
        p=rep.read().decode("GBK")
    except urllib.error.URLError as b:
        print("ERROR!")
        print(b)
    return p
if __name__=="__main__":
    main()