from os import remove
from PIL import Image
for i in range(1,22568):
    urlf="D:\\oprea\\"+str(i)+".jpg"
    print(urlf)
    try:
        img = Image.open(urlf)
        w = img.width       #图片的宽
        h=img.height
        img.close()
        if w==720:
            remove(urlf)
        elif w==469 and h==740:
             remove(urlf)
        elif w==458 and h==750:
            remove(urlf)
        elif w==480 and h==660:
            remove(urlf)
        elif w==500 and h==689:
            remove(urlf)
        elif w==480 and h==660:
            remove(urlf)
        elif w==445 and h==447:
            remove(urlf)
    except:
        print("no this file")
    
