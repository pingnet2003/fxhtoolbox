# -*- coding:utf-8 -*-
import tkinter as tk

class View(tk.Frame):
    def __init__(self,master=None,kind='口',orient=tk.HORIZONTAL,**kw):
        tk.Frame.__init__(self,master,**kw)
        self.root=master
        self.kind=kind
        self.orient=orient
        self.m=1
        self.v=[]
        self.left=None
        self.right=None
        self.top=None
        self.top=None
        self.pack(fill=tk.BOTH,expand=1)
        if self.kind=='口':
            self.view1()
        elif self.kind=='日':
            if self.orient==tk.HORIZONTAL:
                self.view2a()
            else:
                self.view2b()
        elif self.kind=='目':
            if self.orient == tk.HORIZONTAL:
                self.view3a()
            else:
                self.view3b()

    def view1(self):
        self.m=1
        self.v1=self
        self.v1.pack(side=tk.TOP, fill=tk.BOTH, expand=1, ipady=1, pady=1, ipadx=1, padx=1)
        self.v.append(self.v1)

    def view2a(self):
        self.m=2
        self.v1=tk.Frame(self)
        self.v2=tk.Frame(self)
        self.top=self.v1
        self.bottom=self.v2
        # self.v1.pack(side=tk.TOP,fill=tk.BOTH,expand=1,ipady=1,pady=1,ipadx=1,padx=1)
        self.v1.pack(side=tk.TOP, fill=tk.X, ipady=1, pady=1, ipadx=1, padx=1)
        self.v2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1, ipady=1, pady=1, ipadx=1, padx=1)
        self.v.append(self.v1)
        self.v.append(self.v2)

    def view2b(self):
        self.m=2
        # self.v1=tk.Frame(self,width=200)
        self.v1 = tk.Frame(self)
        self.v2=tk.Frame(self)
        self.left=self.v1
        self.right=self.v2
        # self.v1.pack(side=tk.LEFT,fill=tk.BOTH,expand=1,ipady=1,pady=1,ipadx=1,padx=1)
        self.v1.pack(side=tk.LEFT,fill=tk.Y, ipady=1, pady=1, ipadx=1, padx=1)
        self.v2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1, ipady=1, pady=1, ipadx=1, padx=1)
        self.v.append(self.v1)
        self.v.append(self.v2)

    def view3a(self):
        self.m=3
        self.v1 = tk.Frame(self)
        self.v2 = tk.Frame(self)
        self.v3 = tk.Frame(self)
        self.top = self.v1
        self.center = self.v2
        self.bottom = self.v3
        self.v1.pack(side=tk.TOP, fill=tk.BOTH, expand=1, ipady=1, pady=1, ipadx=1, padx=1)
        self.v2.pack(side=tk.TOP, fill=tk.BOTH, expand=1, ipady=1, pady=1, ipadx=1, padx=1)
        self.v3.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1, ipady=1, pady=1, ipadx=1, padx=1)
        self.v.append(self.v1)
        self.v.append(self.v2)
        self.v.append(self.v3)

    def view3b(self):
        self.m=3
        self.v1 = tk.Frame(self)
        self.v2 = tk.Frame(self)
        self.v3 = tk.Frame(self)
        self.left = self.v1
        self.center = self.v2
        self.right = self.v3
        self.v1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, ipady=1, pady=1, ipadx=1, padx=1)
        self.v2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, ipady=1, pady=1, ipadx=1, padx=1)
        self.v3.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1, ipady=1, pady=1, ipadx=1, padx=1)
        self.v.append(self.v1)
        self.v.append(self.v2)
        self.v.append(self.v3)
