# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
from Tl_class_frame import *
import os
import time
from tkinter.filedialog import askopenfilename

class PiMain(object):
    #设计UI 界面
    def setupUI(self):
        v = View(self.root, kind='日', orient=tk.VERTICAL)
        v.v1['width'] = 120

        # #增加按钮,用来 OS
        vButton = tk.Button(v.v1,text='待扩展1',width=11)
        vButton.place(anchor=tk.W,relx=0.1,rely=0.2)

        vButton = tk.Button(v.v1, text='待扩展2', width=11)
        vButton.place(anchor=tk.W, relx=0.1, rely=0.3)

        vButton = tk.Button(v.v1, text='待扩展3', width=11)
        vButton.place(anchor=tk.W, relx=0.1, rely=0.4)

        v_right = View(v.v2, bg='blue',kind='日', orient=tk.HORIZONTAL)
        v_right.v1['height'] = 100

        # #增加Label,用来
        tk.Label(v_right.v1,text='文件夹路径:').pack(side=tk.LEFT)
        self.file1=tk.StringVar()        
        tk.Entry(v_right.v1,width=50,textvariable=self.file1).pack(side=tk.LEFT)
        vButton = tk.Button(v_right.v1, text='...', width=3,command=self.getfile)
        vButton.pack(side=tk.LEFT)
        vButton = tk.Button(v_right.v1, text='重命名', width=8,command=self.renamefile)
        vButton.pack(side=tk.LEFT)

        v_right2 = View(v_right.v2, bg='blue',kind='日', orient=tk.HORIZONTAL)
        v_right2.v1['height'] = 100

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
        

    def handler(self, event, top, tv):
        content = self.tv.set(self.tv.selection(), column='ColB')
        # print(content)
        if content=="":
            pass
        else:
            self.show_vip11_data(content)

    def handler_adaptor(self, fun, **kwds):
        # 事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

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
        self.root.title(string='VIP 管理')
        self.setCenter(self.root, 700, 300)
        self.setupUI()
        self.root.mainloop()

if __name__=='__main__':
    PiMain()
