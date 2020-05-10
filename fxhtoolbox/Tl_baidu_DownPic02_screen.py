# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
from Tl_class_frame import *
# from Tl_baidu_DownPic02 import *
from Tl_baidu_DownPic02  import *
import tkinter.messagebox
import os
import time
from tkinter.filedialog import askopenfilename

class Tl_baidu_DownPic02_screen(object):
    #设计UI 界面
    def setupUI(self):
        v = View(self.root, kind='日', orient=tk.HORIZONTAL)
        v.v1['height'] = 120

        # 设立LabelFrame
        lf1=tk.LabelFrame(v.v1,text='参数')
        lf1.pack(side=tk.LEFT,ipadx=60,ipady=20)

        # #增加Label,用来        
        tk.Label(lf1,text='要下载在内容').pack(anchor=tk.NW)
        self.keyword=tk.StringVar()        
        tk.Entry(lf1,width=50,textvariable=self.keyword).pack(anchor=tk.NW,expand='true',fill='x')

        # lf1_2=tk.LabelFrame(lf1,text='文件夹路径:')
        lf1_2=tk.Frame(lf1)
        lf1_2.pack(anchor=tk.NW,ipadx=60,ipady=10,padx=5)   
        # tk.Label(lf1_2,text='文件夹路径:').pack(side=tk.LEFT)
        tk.Label(lf1_2,text='文件夹路径:').pack(anchor=tk.NW)        
        self.file1=tk.StringVar()        
        tk.Entry(lf1_2,width=40,textvariable=self.file1).pack(anchor=tk.NW)
        vButton = tk.Button(lf1_2, text='...', width=3,command=self.getfile)
        # vButton.pack(side=tk.LEFT)
        vButton.pack(anchor=tk.NW)
        
        tk.Label(lf1,text='所需图片数量:').pack(anchor=tk.NW)        
        self.pic_number=tk.StringVar()  
        self.pic_number.set(10)      
        tk.Entry(lf1,width=10,textvariable=self.pic_number).pack(anchor=tk.NW)

        
        vButton = tk.Button(lf1, text='下载1', width=8,command=self.Call_baidu_Downpic02)
        vButton.pack(side=tk.LEFT)

    def Call_baidu_Downpic02(self):
        # print(self.keyword.get())
        # print(self.file1.get())
        # print(self.pic_number.get())
        if self.keyword.get()=='' or self.file1.get()=='' or self.pic_number.get()=='':
            # print('sssss')
            tkinter.messagebox.showerror(title='操作失败', message='有参数为空,请先检查')
        else:
            try:
                pic_number1=int(self.pic_number.get())
                call_DownPic02_main(self.keyword.get(),self.file1.get(),pic_number1)
                tkinter.messagebox.showinfo(title='操作完成', message='操作完成')
            except:
                import sys
                tuple=sys.exc_info()
                errmsg='导入图片失败'+'错误为:'+str(tuple[1])
                tkinter.messagebox.showerror(title='操作失败', message=errmsg)

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
        # self.root = tk.Tk()   #本界面单独运行时,需要用到本行语句
        self.root = tk.Toplevel()
        self.root.title(string='Baidu 图片下载 管理')
        self.setCenter(self.root, 700, 300)
        self.setupUI()
        self.root.mainloop()

if __name__=='__main__':
    Tl_baidu_DownPic02_screen()

