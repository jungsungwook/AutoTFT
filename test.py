import cv2
import time
import keyboard
import pickle
import dill
#import mmap
#import numpy as np
#import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
#from PyQt5.QtCore import Qt
from tkinter import *
import threading
import pyautogui
from PIL import ImageGrab
import ctypes
#import matplotlib
template = cv2.imread('cost_1/ahep.png', 0)
w, h = template.shape[::-1]


varList = []
# template 이미지의 가로/세로

chmList = [['xmxk',1], ['ahep',1], ['slekffl',1], ['qpdls',1], ['vldhfk',1], ['rkfps',1], ['dnjdnlr',1], ['dpffltm',1], ['zktkels',1], ['rmqm',1], ['zkwlrtm',1],
           ['ekfl',1]]
selectList = []
sharedMem_selectList = mp.Array('i', range(len(chmList)))
sharedMem_chk=mp.Value('i',0)
# Template Match Method
def resetArr(arr):
    for l in range(len(arr)):
        arr[l] = 0
##def all_loopStop(chk):
##    #print("[def]all_loopStop:::ready")
##    while True:
##        if chk.value==0:
##            if keyboard.is_pressed('q'):
##                print("::stop loop::")
##                chk.value=1


def screencapture(shrMem,chk):
    #print("[def]screencapture:::ready")
    while True:
        if chk.value==0:
            #if (testarr[0] == 1):
            #    break
            imageGrab = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
            imageGrab.save('capture.png')
            loadimageGrab=cv2.imread('capture.png', 0)
            #printScreen = np.array(image)
            #cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
            precessed_2(shrMem,loadimageGrab,chk)


def ui_init(shrMem,chk):
    self=Tk()
    # 체크버튼 변수들
    self.ahep_var = StringVar()
    self.slekffl_var = StringVar()
    self.qpdls_var = StringVar()
    self.xmxk_var = StringVar()
    self.dnjdnlr_var = StringVar()
    self.zkwlrtm_var = StringVar()
    self.ekfl_var = StringVar()
    self.vldhfk_var = StringVar()
    self.dpffltm_var = StringVar()
    self.zktkels_var = StringVar()
    self.rmqm_var = StringVar()
    self.rkfps_var = StringVar()


    # 타이틀선언
    self.title("AutoTFT v0.1")
    # 체크버튼 객체들
    self.ahepChk = Checkbutton(self, text='모데카이저', variable=self.ahep_var, onvalue='ahepON', offvalue='ahepOFF',
                               command=lambda:checkBOX(shrMem))
    self.slekfflChk = Checkbutton(self, text='니달리', variable=self.slekffl_var, onvalue='slekfflON',
                                  offvalue='slekfflOFF', command=lambda:checkBOX(shrMem))
    self.qpdlsChk = Checkbutton(self, text='베인', variable=self.qpdls_var, onvalue='qpdlsON', offvalue='qpdlsOFF',
                                command=lambda:checkBOX(shrMem))
    self.xmxkChk = Checkbutton(self, text='트리스타', variable=self.xmxk_var, onvalue='xmxkON', offvalue='xmxkOFF',
                               command=lambda:checkBOX(shrMem))
    self.rkfpsChk = Checkbutton(self, text='가렌', variable=self.rkfps_var, onvalue='rkfpsON', offvalue='rkfpsOFF',
                                command=lambda:checkBOX(shrMem))
    self.dnjdnlrChk = Checkbutton(self, text='워윅', variable=self.dnjdnlr_var, onvalue='dnjdnlrON',
                                  offvalue='dnjdnlrOFF', command=lambda:checkBOX(shrMem))
    self.zkwlrtmChk = Checkbutton(self, text='카직스', variable=self.zkwlrtm_var, onvalue='zkwlrtmON',
                                  offvalue='zkwlrtmOFF', command=lambda:checkBOX(shrMem))
    self.ekflChk = Checkbutton(self, text='다리우스', variable=self.ekfl_var, onvalue='ekflON', offvalue='ekflOFF',
                               command=lambda:checkBOX(shrMem))
    self.vldhfkChk = Checkbutton(self, text='피오라', variable=self.vldhfk_var, onvalue='vldhfkON', offvalue='vldhfkOFF',
                                 command=lambda:checkBOX(shrMem))
    self.dpffltmChk = Checkbutton(self, text='엘리스', variable=self.dpffltm_var, onvalue='dpffltmON',
                                  offvalue='dpffltmOFF', command=lambda:checkBOX(shrMem))
    self.zktkelsChk = Checkbutton(self, text='카사딘', variable=self.zktkels_var, onvalue='zktkelsON',
                                  offvalue='zktkelsOFF', command=lambda:checkBOX(shrMem))
    self.rmqmChk = Checkbutton(self, text='그레이브즈', variable=self.rmqm_var, onvalue='rmqmON', offvalue='rmqmOFF',
                               command=lambda:checkBOX(shrMem))
    # 체크버튼 설정값
    self.ahepChk.deselect()
    self.slekfflChk.deselect()
    self.qpdlsChk.deselect()
    self.xmxkChk.deselect()
    self.rkfpsChk.deselect()
    self.dnjdnlrChk.deselect()
    self.zkwlrtmChk.deselect()
    self.ekflChk.deselect()
    self.vldhfkChk.deselect()
    self.dpffltmChk.deselect()
    self.zktkelsChk.deselect()
    self.rmqmChk.deselect()
    # 체크버튼 패키징
    self.ahepChk.pack(side=TOP)
    self.slekfflChk.pack(side=TOP)
    self.qpdlsChk.pack(side=TOP)
    self.xmxkChk.pack(side=TOP)
    self.rkfpsChk.pack(side=TOP)
    self.dnjdnlrChk.pack(side=TOP)
    self.zkwlrtmChk.pack(side=TOP)
    self.ekflChk.pack(side=TOP)
    self.vldhfkChk.pack(side=TOP)
    self.dpffltmChk.pack(side=TOP)
    self.zktkelsChk.pack(side=TOP)
    self.rmqmChk.pack(side=TOP)
    #
    varList.append(self.ahep_var)
    varList.append(self.slekffl_var)
    varList.append(self.qpdls_var)
    varList.append(self.xmxk_var)
    varList.append(self.rkfps_var)
    varList.append(self.dnjdnlr_var)
    varList.append(self.zkwlrtm_var)
    varList.append(self.ekfl_var)
    varList.append(self.vldhfk_var)
    varList.append(self.dpffltm_var)
    varList.append(self.zktkels_var)
    varList.append(self.rmqm_var)
    #
    strtbtn = Button(self, text="Start", command= lambda: startBtn(chk))
    strtbtn.pack()
    async_box_process = mp.Process(target=async_box(self))
    async_box_process.start()
    self.title('autoTFT v1.0')
    self.geometry('200x500+200+200')
    self.mainloop()

def async_box(self):
    if sharedMem_chk==0:
        label=Label(self,text="작동중",width=10, height=5, fg="red", relief="solid")
        label.pack()

def startBtn(chk):
    print("Click::StartBtn")
    print(chk.value)
    if(chk.value==1):
        print("launch")
        chk.value=0

def checkBOX(shrMem):
    for var in varList:
        for i in chmList:
            if (var.get() == i[0] + "ON"):
                if not (i in selectList):
                    selectList.append(i)
                    print(selectList)
            elif (var.get() == i[0] + "OFF"):
                if (i in selectList):
                    selectList.remove(i)
                    print(selectList)
    tmplist = []
    resetArr(shrMem)
    for t in selectList:
        tmplist.append(chmList.index(t))
    for k in tmplist:
        shrMem[k] = 1

def precessed_2(shrMem,captureImg,chk):
    #print("[def]precessed_2:::ready\n=========================")
    for i in range(len(shrMem)):
        if(shrMem[i] and chk.value==0):
            targetName=chmList[i]
            print("[SEARCHING] : ", targetName)
            template = cv2.imread('cost_1/' + targetName[0] + '.png', 0)
            img = captureImg
            method = eval('cv2.TM_SQDIFF_NORMED')
            res = cv2.matchTemplate(img, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            print(min_val, "::", max_val, "::", min_loc, "::", max_loc)
            if(min_val<=0.3):
                pyautogui.moveTo((min_loc[0] + 100), (min_loc[1] + 70))
                pyautogui.mouseDown((min_loc[0] + 100), (min_loc[1] + 70))
                time.sleep(0.5)
                pyautogui.mouseUp((min_loc[0]-100), (min_loc[1]-100))



def processed(shrMem,captureImg):
    testName=""
    for chk in range(len(shrMem)):
        if(shrMem[chk]):
            testName=chmList[chk]
            print(testName)
    if not(testName==""):
        template = cv2.imread('cost_1/'+testName+'.png', 0)
        img = captureImg
        method = eval('cv2.TM_SQDIFF_NORMED')
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        pyautogui.moveTo((min_loc[0]+100),(min_loc[1]+70))
        print(min_val,"::",max_val,"::",min_loc,"::",max_loc)
        #top_left = min_loc
        #bottom_right = (top_left[0] + w, top_left[1] + h)
        #cv2.rectangle(img, top_left, bottom_right, 255, 5)

        #plt.subplot(121), plt.title('cv2.TM_SQDIFF'), plt.imshow(res, cmap='gray'), plt.yticks([]), plt.xticks([])
        #plt.subplot(122), plt.imshow(img, cmap='gray')
        #plt.show()

def __init__():
    resetArr(sharedMem_selectList)
##    test1 = mp.Process(target=all_loopStop, args=(sharedMem_chk,))
##    test1.start()
    test3 = mp.Process(target=screencapture, args=(sharedMem_selectList,sharedMem_chk))
    test3.start()
    test2 = mp.Process(target=ui_init,args=(sharedMem_selectList,sharedMem_chk))
    test2.start()

if __name__ == '__main__':
    __init__()
