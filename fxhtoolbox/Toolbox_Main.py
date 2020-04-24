import tkinter  as tk
import tkinter.messagebox
from Tl_baidu_scan_screen import *
from Tl_ip_scan_screen import *
from Tl_wifi_scan_screen import *
from Tl_Opencv_screen01 import *
from Tl_Opencv_screen02 import *

class Win_Program:
    def __init__(self):
        self.master = tk.Tk()
        # self.master.state("zoomed") # 窗口最大化
        self.master.geometry('600x300')
        self.master.title("Xiaohong's Toolbox")
        self.master.grid()
        self.SetupUI()

    def SetupUI(self):
        # 获取屏幕长/宽
        Screen_width = self.master.winfo_screenwidth()
        Screen_height = self.master.winfo_screenheight()
        print(Screen_height,Screen_width)

        fm1=tk.LabelFrame(self.master,text='爬取部分',padx=5,pady=5,width=800,height=100)
        # fm1 = tk.LabelFrame(self.master, text='爬取部分', width=1800, height=300)
        # fm1 = tk.Frame(self.master, padx=15, pady=5, width=300, height=100,borderwidth=1,bg='blue')
        # fm1.pack(side=tk.LEFT,fill=tk.X)
        fm1.grid(row=0,column=1,padx=10,pady=10)

        button1=tk.Button(fm1,text='baidu图片识别',command=lambda:self.Call_baidu_scan_win(self.master,Screen_width,Screen_height))
        # button1.pack(side=tk.RIGHT)
        button1.grid(row=0,column=1,padx=5,pady=0)


        fm2=tk.LabelFrame(self.master,text='其他部分',padx=5,pady=5,width=800,height=100)
        fm2.grid(row=1,column=1,padx=10,pady=10)

        button2=tk.Button(fm2,text='IP 地址扫描',command=lambda:self.Call_ip_scan_win(self.master,Screen_width,Screen_height))
        button2.grid(row=0,column=1,padx=5,pady=0)

        button2 = tk.Button(fm2, text='Wifi 密码扫描',
                            command=lambda: self.Call_wifi_scan_win(self.master))
        button2.grid(row=0, column=2, padx=5, pady=0)

        fm3=tk.LabelFrame(self.master,text='OpenCV部分',padx=5,pady=5,width=800,height=100)
        fm3.grid(row=2,column=1,padx=10,pady=10)

        button3=tk.Button(fm3,text='二维码条形码识别01',command=lambda: self.Call_opencv01_scan_win(self.master))
        button3.grid(row=0,column=1,padx=5,pady=0)

        button4=tk.Button(fm3,text='二维码条形码识别02',command=lambda: self.Call_opencv02_scan_win(self.master))
        button4.grid(row=0,column=2,padx=5,pady=0)

        button4=tk.Button(fm3,text='二维码条形码识别03',command=lambda: self.Call_opencv03_scan_win(self.master))
        button4.grid(row=0,column=3,padx=5,pady=0)

    def Call_baidu_scan_win(self,father_win,Screen_width,Screen_height):
        Tl_baidu_scan_screen(father_win,Screen_width,Screen_height)
        pass

    def Call_ip_scan_win(self,father_win,Screen_width,Screen_height):
        Tl_ip_scan_screen(father_win,Screen_width,Screen_height)
        pass

    def Call_wifi_scan_win(self,father_win):
        Tl_wifi_scan_screen(father_win)
        pass

    def Call_opencv01_scan_win(self,father_win):
        Tl_Opencv_screen01(father_win)
        pass    

    def Call_opencv02_scan_win(self,father_win):
        errmsg ="Tl_Opencv_screen02 会提示 Frame not defined 错误,还须再处理"
        tkinter.messagebox.showerror(
            title='操作失败', message=errmsg)
        # Tl_Opencv_screen02(father_win)
        pass    

    def Call_opencv03_scan_win(self,father_win):
        errmsg ="Tl_Opencv_screen02 会提示 Frame not defined 错误,还须再处理"
        tkinter.messagebox.showerror(
            title='操作失败', message=errmsg)
        # Tl_Opencv_screen02(father_win)
        pass    

if __name__ == "__main__":
    win_program = Win_Program()
    tk.mainloop()
