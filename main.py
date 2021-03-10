import cv2
import time
import keyboard
import mmap
import numpy as np
from matplotlib import pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt
from tkinter import *
import threading
import multiprocessing as mp
import pyautogui
from PIL import ImageGrab
import ctypes
import threading
template = cv2.imread('cost_1/ahep.png', 0)
w, h = template.shape[::-1]


varList = []
# template 이미지의 가로/세로
self = Tk()
chmList = ['xmxk', 'ahep', 'slekffl', 'qpdls', 'vldhfk', 'rkfps', 'dnjdnlr', 'dpffltm', 'zktkels', 'rmqm', 'zkwlrtm',
           'ekfl']
selectList = []
global sharedMem_selectList
sharedMem_selectList = ['i' for i in range(len(chmList))]
global chk
chk = True

# Template Match Method
def resetArr(arr):
    for i in range(len(arr)):
        arr[i] = 0
        
def all_loopStop():
    global chk
    print("[def]all_loopStop:::ready")
    while(chk==False):
        if keyboard.is_pressed('q'):
            print("::stop loop::")
            chk=True
    print("[def]all_loopStop:::exit")

def __init__(self):
    resetArr(sharedMem_selectList)
    test2 = threading.Thread(target=ui_init(self))
    test2.start()



def screencapture():
    global sharedMem_selectList
    global chk
    print("[def]screencapture:::ready")
    while (chk==False):
        #if (testarr[0] == 1):
        #    break
        imageGrab = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
        imageGrab.save('capture.png')
        loadimageGrab=cv2.imread('capture.png', 0)
        #printScreen = np.array(image)
        #cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
        precessed_2(sharedMem_selectList,loadimageGrab)
    print("[def]screencapture:::exit")


def ui_init(self):
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
                               command=checkBOX)
    self.slekfflChk = Checkbutton(self, text='니달리', variable=self.slekffl_var, onvalue='slekfflON',
                                  offvalue='slekfflOFF', command=checkBOX)
    self.qpdlsChk = Checkbutton(self, text='베인', variable=self.qpdls_var, onvalue='qpdlsON', offvalue='qpdlsOFF',
                                command=checkBOX)
    self.xmxkChk = Checkbutton(self, text='트리스타', variable=self.xmxk_var, onvalue='xmxkON', offvalue='xmxkOFF',
                               command=checkBOX)
    self.rkfpsChk = Checkbutton(self, text='가렌', variable=self.rkfps_var, onvalue='rkfpsON', offvalue='rkfpsOFF',
                                command=checkBOX)
    self.dnjdnlrChk = Checkbutton(self, text='워윅', variable=self.dnjdnlr_var, onvalue='dnjdnlrON',
                                  offvalue='dnjdnlrOFF', command=checkBOX)
    self.zkwlrtmChk = Checkbutton(self, text='카직스', variable=self.zkwlrtm_var, onvalue='zkwlrtmON',
                                  offvalue='zkwlrtmOFF', command=checkBOX)
    self.ekflChk = Checkbutton(self, text='다리우스', variable=self.ekfl_var, onvalue='ekflON', offvalue='ekflOFF',
                               command=checkBOX)
    self.vldhfkChk = Checkbutton(self, text='피오라', variable=self.vldhfk_var, onvalue='vldhfkON', offvalue='vldhfkOFF',
                                 command=checkBOX)
    self.dpffltmChk = Checkbutton(self, text='엘리스', variable=self.dpffltm_var, onvalue='dpffltmON',
                                  offvalue='dpffltmOFF', command=checkBOX)
    self.zktkelsChk = Checkbutton(self, text='카사딘', variable=self.zktkels_var, onvalue='zktkelsON',
                                  offvalue='zktkelsOFF', command=checkBOX)
    self.rmqmChk = Checkbutton(self, text='그레이브즈', variable=self.rmqm_var, onvalue='rmqmON', offvalue='rmqmOFF',
                               command=checkBOX)
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
    strtbtn = Button(self, text="Start", command=startBtn)
    strtbtn.pack()
    self.title('autoTFT v1.0')
    self.geometry('200x500+200+200')
    self.mainloop()
def startBtn():
    global chk
    print("Click::StartBtn")
    print(chk)
    if(chk):
        print("launch")
        test1 = threading.Thread(target=all_loopStop)
        test1.start()
        test3 = threading.Thread(target=screencapture)
        test3.start()
        chk=False;

def checkBOX():
    for var in varList:
        for i in chmList:
            if (var.get() == i + "ON"):
                if not (i in selectList):
                    selectList.append(i)
                    print(selectList)
            elif (var.get() == i + "OFF"):
                if (i in selectList):
                    selectList.remove(i)
                    print(selectList)
    tmplist = []
    resetArr(sharedMem_selectList)
    for t in selectList:
        tmplist.append(chmList.index(t))
    for k in tmplist:
        sharedMem_selectList[k] = 1

def precessed_2(shrMem,captureImg):
    print("[def]precessed_2:::ready")
    for i in range(len(shrMem)):
        if(shrMem[i]):
            targetName=chmList[i]
            template = cv2.imread('cost_1/' + targetName + '.png', 0)
            img = captureImg
            method = eval('cv2.TM_SQDIFF_NORMED')
            res = cv2.matchTemplate(img, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if(min_val>=1.0):
                print("=검출되지 않음=")
                return
            pyautogui.moveTo((min_loc[0] + 100), (min_loc[1] + 70))
            pyautogui.mouseDown((min_loc[0] + 100), (min_loc[1] + 70))
            time.sleep(0.5)
            #pyautogui.mouseUp((min_loc[0]-100), (min_loc[1]-100))
            pyautogui.mouseUp((min_loc[0] + 100), (min_loc[1] + 70))
            print(min_val, "::", max_val, "::", min_loc, "::", max_loc)


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


if __name__ == '__main__':
    __init__(self)
