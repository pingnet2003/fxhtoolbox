# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
from Tl_class_frame import *
from Tl_baidu_DownPic02 import *
import os
import time
from tkinter.filedialog import askopenfilename

class PiMain(object):
    #设计UI 界面
    def setupUI(self):
        v = View(self.root, kind='日', orient=tk.HORIZONTAL)
        v.v1['height'] = 120

        # 设立LabelFrame
        lf1=tk.LabelFrame(v.v1,text='参数')
        lf1.pack(side=tk.LEFT,ipadx=60,ipady=20)

        # #增加Label,用来        
        tk.Label(lf1,text='要下载在内容').pack(anchor=tk.NW)
        self.file1=tk.StringVar()        
        tk.Entry(lf1,width=50,textvariable=self.file1).pack(anchor=tk.NW,expand='true',fill='x')

        # tk.Label(lf1,text='文件夹路径:').pack(side=tk.LEFT)
        tk.Label(lf1,text='文件夹路径:').pack(anchor=tk.NW)        
        self.file1=tk.StringVar()        
        tk.Entry(lf1,width=40,textvariable=self.file1).pack(anchor=tk.NW)
        
        tk.Label(lf1,text='所需图片数量:').pack(anchor=tk.NW)        
        self.pic_number=tk.StringVar()        
        tk.Entry(lf1,width=10,textvariable=self.pic_number).pack(anchor=tk.NW)

        vButton = tk.Button(lf1, text='...', width=3,command=self.getfile)
        vButton.pack(side=tk.LEFT)
        vButton = tk.Button(lf1, text='下载1', width=8,command=self.Call_baidu_Downpic02)
        vButton.pack(side=tk.LEFT)

    def renamefile(self):
        direct1=self.file1.get()
        # print(direct1)
        direct2=self.get_sysdate2()
        bak_direct1=os.path.join(direct1,direct2)
        # print(bak_direct1)        
        files = os.listdir(direct1)
        print(files)
        files2=sorted(files)
        print(files2)
        # for i in files:
        #     if os.path.isfile(os.path.join(direct1,i)):
        #         print(os.path.join(direct1,i))

    def Call_baidu_Downpic02(self):
        call_DownPic02_main('Raspberry',5)

    def getfile(self):
        xx = tk.filedialog.askdirectory()
        self.file1.set(xx)

    # 设立函数，来取得当前时间，作为文件名的一部分，以免文件名重复
    def get_sysdate2(self):
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        # print(now)
        return now

    def setCenter(self,root, w, h):
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = int((ws / 2) - (w / 2))
        y = int((hs / 2) - (h / 2))
        root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

    #类的运行主体
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(string='Baidu 图片下载 管理')
        self.setCenter(self.root, 700, 300)
        self.setupUI()
        self.root.mainloop()

if __name__=='__main__':
    PiMain()

