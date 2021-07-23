import os
import urllib.error
import urllib.request
import urllib.response
import sys
from bs4 import BeautifulSoup
def main():
    dataknow()
#数据解析
def dataknow():
    if  not os.path.exists("F:\\pic\\"):
        os.makedirs("F:\\pic\\") 
    else:
        print("文件夹已经存在了，请把原来的文件夹删了，路径：F:\\pic\\，不然用不了")
        sys.exit()

    basicnum=10883
    lobol=0
    while(True):
     url="http://www.gan1994.com/html/article/index"+str(basicnum)+".html"
     sorce=gethtml(url)
     bs=BeautifulSoup(sorce,"html")
     imglist=bs.find_all('img')
     weblist=[]
     for a in imglist:
         web=a.get("src")
         weblist.append(web)
     for b in weblist:
        lobol+=1
        with open("F:\\pic\\"+str(lobol)+".jpg","wb") as imgs:
                print("正在下载第"+str(lobol)+"张图")
                try:
                    lka=urllib.request.urlopen(b)
                    imgs.write(lka.read())
                except:
                    print("ERROR IN"+str(lobol)+"1")
                    imgs.close()
                    os.remove("F:\\pic\\"+str(lobol)+".jpg")
               
                print("下载成功")
     basicnum-=1
     
               
#获取源代码        
def gethtml(url):
    head={"users":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    req=urllib.request.Request(url,headers=head)
    p=""
    try:
        rep=urllib.request.urlopen(req)
        p=rep.read().decode("GBK")
    except:
        print("Error in 2")
    return p
if __name__=="__main__":
    main()
