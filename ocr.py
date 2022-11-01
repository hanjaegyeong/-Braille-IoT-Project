import easyocr 
import cv2
import hbcvt
import bluetooth

socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
socket.connect(("B8:D6:1A:82:4D:92", 1))
print("bluetooth connected!")

reader = easyocr.Reader(['ko','en'])

img_path = r'/home/oseer/Downloads/image.jpg'
img = cv2.imread(img_path)


result = reader.readtext(img_path)
percentage = 0.1  

txtlist = []
with open(r"/home/oseer/Downloads/txtimage.txt", "w", encoding="utf8") as f:
      f.write("")
for bbox,text,conf, in result:
  if conf> percentage:
    

    a = text.replace(" ", "")
    
    with open(r"/home/oseer/Downloads/txtimage.txt", "a", encoding="utf8") as f:
      f.write(str(a))
    


    b = hbcvt.h2b.text(a)
    print(a)
    print("---------------------")
    print(b)



    print("---------------------")

    for i in range(len(a)):   ## 텍스트 공백없앤 길이만큼 반복 
        for j in range(len(b[i][1])):
            for k in range(len(b[i][1][j][1])):
                 c = b[i][1][j][1][k]  ### 점자로 변환한 정수 리스트로 반한
                 d = [str(i) for i in c]
                 m = "".join(d)
                 msg = ""
                 print(m)
                 for idx in range(len(m)):
                     if m[idx] == "1":
                         print(idx)
                         msg += str(idx)
                 msg = msg.replace("0", "a")
                 msg = msg.replace("1", "b")
                 msg = msg.replace("2", "c")
                 msg = msg.replace("3", "d")
                 msg = msg.replace("4", "e")
                 msg = msg.replace("5", "f")
                 print(msg)
                 socket.send(msg)
                 print(" " .join(d))

socket.close()
