# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
from Tl_class_frame import *
import os
import time
from tkinter.filedialog import askopenfilename
from shutil import copy
import re
 
class Tl_Rename_Screen(object):
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
 
        v_right2 = View(v_right.v2, bg='blue',kind='日', orient=tk.VERTICAL)
        # v_right2.v1['height'] = 100
 
        lf1=tk.LabelFrame(v_right2.v1,text="原来文件列表")
        lf1.pack()
        self.lb1=tk.Listbox(lf1,height=30,width=50)
        self.lb1.insert('end','xxxxxxx')
        self.lb1.pack()
        lf2=tk.LabelFrame(v_right2.v2,text="重命名后的文件列表")
        lf2.pack()
        self.lb2=tk.Listbox(lf2,height=30,width=50)
        self.lb2.insert('end','yyyyyy')
        self.lb2.pack()
        
 
    def renamefile(self):
        direct1=self.file1.get()    #获得 要处理的文件夹 路径
        direct2=self.get_sysdate2()   #获得 备份文件夹 名字        
        parent_path = os.path.dirname(direct1) #获得 要处理的文件夹 所在的目录,即 父级目录          
        bak_direct1=os.path.join(parent_path,direct2)    #得到 备份文件夹 的完整路径        
        file_lists=[]     
        file_list2s=[]    
        if not os.path.exists(bak_direct1):      #判断 备份文件夹 是否已存在
            os.makedirs(bak_direct1)             # 不存在则重新创建
        for root,sub_dirs,files in os.walk(direct1):     # 遍历  要处理的文件夹
            for file in files:
                if file.endswith('mp3'):   #检查 扩展名为MP3的文件
                    print(file)
                    file_lists.append(file)
                    dest_file=os.path.join(bak_direct1,file)   #要备份的 目标文件名
                    copy(os.path.join(root,file),dest_file)    #Copy 到目标处
                    vir_file=os.path.splitext(file)[0]         #除去 扩展名
                    vir_file_ext=os.path.splitext(file)[1]         #  扩展名
                    num_file=re.findall(r"\d+",vir_file)           # 用正则提取 文件名中的数字
                    if num_file:                                    #非空,则判断是否 小于10，是则在前面加0
                        if int(num_file[0])<10 and len(num_file[0])<2 :
                            pre_name='0'+(num_file[0])
                        else:
                            pre_name=num_file[0]                        
                        new_file_name=pre_name+file            #在原有文件名前加上 前缀
                        print(new_file_name)
                        file_list2s.append(new_file_name)
                        os.rename(os.path.join(root, file), os.path.join(root, new_file_name))
                                      
        for file in file_lists:
            self.lb1.insert('end',file)
        for file in file_list2s:
            self.lb2.insert('end',file)    
 
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
        # self.root = tk.Tk()    #本程式单独运行时,用本行语句
        self.root = tk.Toplevel()
        self.root.title(string='MP3 文件重命名 管理')
        self.setCenter(self.root, 700, 300)
        self.setupUI()
        self.root.mainloop()
 
if __name__=='__main__':
    Tl_Rename_Screen()