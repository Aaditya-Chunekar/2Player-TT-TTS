from gtts import gTTS as gt
import pyautogui as pag
import time
import random
import os
print("\033[33mIMP : The program should only be running with one tab of command prompt\033[0m")
def ps(text):
    language = 'en'
    myobj = gt(text=text, lang=language, slow=False)
    myobj.save("temp.mp3")
    os.system("start temp.mp3")
   
po=input("Enter player one name : ")
pt=input("Enter player two name : ")
#deuce-less two player one match system
ps("Toss for serve")
time.sleep(3)
ch=int(input(str(po)+" selects choice, either 0 or 1, winner serves	"))
if (random.randint(0,1)==ch):
	se=po
	nse=pt
else:
	se=pt
	nse=po
ps("Enter 1 to increment point of "+str(po)+" and 2 to increment point of "+str(pt)+" after match begins")
time.sleep(5)
ps("Match begins in 3")
time.sleep(1.5)
ps("2")
time.sleep(1.5)
ps("1")
time.sleep(1.5)
spo=0
spt=0
#add deuce logic by 
#adding win variable which on being 0 means player one has won, 1 means two and 2 means none
while (spo != 11 and spt != 11):
	if((spo+spt)%4==0 or (spo+spt)%4==1):
		ps(str(se)+" serves")
		time.sleep(1.5)
	else:
		ps(str(nse)+" serves")
		time.sleep(1.5)
	ptm=int(input("Enter 1 or 2 : "))
	if(ptm==1):
		spo+=1;
	elif(ptm==2):
		spt+=1;
	ps("Score\n"+str(po)+" "+str(spo)+"\n"+str(pt)+str(spt))
	time.sleep(5)
if(spo==11):
	ps(str(po)+" Wins !")
else:
	ps(str(pt)+" Wins !")


