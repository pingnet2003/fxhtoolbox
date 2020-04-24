import tkinter  as tk
import re
import tkinter.messagebox
from Tl_ip_scan import *

class Tl_ip_scan_screen:
    def __init__(self,father_win,Screen_width,Screen_height):
        self.master = tk.Toplevel(father_win)
        self.master.title('IP 地址扫描')

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
        entry_validate=self.master.register(self.check_vaild)
        fm1=tk.LabelFrame(self.master,text='IP 地址段',padx=5,pady=5,width=600,height=100)
        fm1.grid(row=0,column=1,columnspan=2,padx=5,pady=5)

        lb1=tk.Label(fm1,text='IP 从')
        lb1.grid(row=0,column=1)
        # 设定默认值
        web_site = tk.StringVar()
        web_site.set('192.168.101.26')
        web_site_value = tk.Entry(fm1, textvariable=web_site, font=('Arial', 10),width=15,validate='focusout',vcmd=(entry_validate,'%P'))
        web_site_value.grid(row=0,column=2)

        lb1=tk.Label(fm1,text='到')
        lb1.grid(row=0,column=3)

        web_site_to = tk.StringVar()
        web_site_to.set('192.168.101.30')
        web_site_to_value = tk.Entry(fm1, textvariable=web_site_to, font=('Arial', 10), width=15, validate='focusout',
                                  vcmd=(entry_validate, '%P'))
        web_site_to_value.grid(row=0,column=4)

        button1=tk.Button(fm1,text='扫描',command=lambda :self.Call_ip_Scan(web_site_value.get(),web_site_to_value.get(),lb1=lb1,lb2=lb2))
        button1.grid(row=0,column=5,padx=2)

        button2 = tk.Button(fm1, text='返回', command=self.master.quit)
        button2.grid(row=0, column=6)

        fm3 = tk.LabelFrame(self.master,text='OK结果', padx=5, pady=5, width=400, height=250)
        fm3.grid(row=1, column=1,padx=5, pady=5,sticky='w')

        lb1 = tk.Listbox(fm3,height=9)
        lb1.grid(row=0,column=1)

        fm4 = tk.LabelFrame(self.master,text='NO结果', padx=5, pady=5, width=400, height=250)
        fm4.grid(row=1, column=2,padx=5, pady=5,sticky='w')

        lb2 = tk.Listbox(fm4,height=9)
        lb2.grid(row=0,column=2)

        self.master.mainloop()

    def check_vaild(self,content):
        if content=="":
            return true
        #用正则表达式来判断是否是IPV4的地址
        if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                        content):
            return True
        else:
            tkinter.messagebox.showerror(title='操作失败', message='无效的IP地址:' + content)
            return False

    def Call_ip_Scan(self,ip_from,ip_to,lb1,lb2):
        if self.check_vaild(ip_from):
            if self.check_vaild(ip_to):
                # 找到ip地址的最后一部分,如192.168.101.26 ,取出26
                # ip_from_end = ip_from[ip_from.rfind('.')+1:]
                # ip_to_end = ip_to[ip_to.rfind('.') + 1:]
                ip_from_end=ip_from.split('.')[-1]
                ip_to_end=ip_to.split('.')[-1]
                print(ip_from_end)
                print(ip_to_end)
                # 找到ip地址的前3部分,如192.168.101.26 ,取出 192.168.101.
                ip_from_begin = ip_from[:ip_from.rfind('.') + 1]

                ip_list=[]
                # 生成待扫描的IP地址列表
                for i in range(int(ip_from_end),int(ip_to_end)+1):
                    ip_list.append(ip_from_begin+str(i))

                reachlb,unreachlb=Tl_ip_scan(ip_list)

                for i in reachlb:
                    lb1.insert(tk.END,i)

                for i in unreachlb:
                    lb2.insert(tk.END, i)


