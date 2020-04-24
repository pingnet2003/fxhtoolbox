import tkinter  as tk
from Tl_baidu_Scan import *

class Tl_baidu_scan_screen:
    def __init__(self,father_win,Screen_width,Screen_height):
        self.master = tk.Toplevel(father_win)
        self.master.title('Baidu图片识别')
        # self.master.resizable(0, 0)  # 大小不可变
        # 创建的Toplevel对象 在最上层
        self.master.attributes("-toolwindow", 1)
        self.master.wm_attributes("-topmost", 1)
        self.master.grid()
        width = 660
        
        height = 420
        x = Screen_width / 2 - width / 2
        y = Screen_height / 2 - height / 2
        self.master.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.master.grid()

        self.SetupUI()

    def SetupUI(self):

        fm1=tk.LabelFrame(self.master,text='图片网址',padx=5,pady=5,width=600,height=100)
        fm1.grid(row=0,column=1,padx=5,pady=5)

        lb1=tk.Label(fm1,text='图片网址')
        lb1.grid(row=0,column=1)
        # 设定默认值
        web_site = tk.StringVar()
        web_site.set('https://www.python.org/static/img/python-logo.png')
        web_site_value = tk.Entry(fm1, textvariable=web_site, font=('Arial', 12),width=50)
        web_site_value.grid(row=0,column=2)

        button1=tk.Button(fm1,text='识别',command=lambda:self.Call_baidu_Scan(web_site,lb1))
        button1.grid(row=0,column=3)

        button2 = tk.Button(fm1, text='返回', command=self.master.quit)
        button2.grid(row=0, column=4)

        fm3 = tk.LabelFrame(self.master,text='结果', padx=5, pady=5, width=400, height=250)
        fm3.grid(row=1, column=1,padx=5, pady=5,sticky='w')

        lb1 = tk.Listbox(fm3,height=9)
        lb1.place(x=10,y=10,width=300,height=200)

        self.master.mainloop()

    def Call_baidu_Scan(self,website,lb1):
        # Tl_badiu_Scan.Tl_badiu_Scan(website)
        lb_value = Tl_badiu_Scan(website)
        for i in lb_value:
            lb1.insert(tk.END,i)


