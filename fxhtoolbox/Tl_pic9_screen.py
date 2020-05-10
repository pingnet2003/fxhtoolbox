# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
import os
import time
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from Tl_pic9 import *

root = tk.Tk()
root.title(string='图片分割成九宫格')
width1 = 150
height1 = 150

fr_top = tk.LabelFrame(root)
fr_top.grid(row=0, column=0, columnspan=2)


def getfile():  # 选择图片
    xx = tk.filedialog.askopenfilename()
    file1.set(xx)
    show_pic()


def show_pic():  # 显示到左边图片区中
    img_left = Image.open(file1.get())  # 打开图片
    img_png_left = ImageTk.PhotoImage(image=img_left)
    button_imgx.config(image=img_png_left)  # 配置
    button_imgx.image = img_png_left  # 再配置,必须做这双重配置,否则不会动态更新


def split_pic():
    yy = file1.get()
    print(yy)
    Start_split(yy)

def show_pic_detail():  # 显示到右边图片区中(明细)
    img_png_list = []
    for i in range(9):
        x = str(i+1)+'.png'
        print(x)
        img = Image.open(x)  # 打开图片
        img_png_list.append(ImageTk.PhotoImage(image=img))

    i = 0
    for x in range(9):
        button_img_list[x].config(image=img_png_list[x])
        button_img_list[x].image=img_png_list[x]

    # img = Image.open(file1.get())  # 打开图片
    # img_png = ImageTk.PhotoImage(image=img)
    # button_img.config(image=img_png)  # 配置
    # button_img.image = img_png  # 再配置,必须做这双重配置,否则不会动态更新    


# 增加Label
tk.Label(fr_top, text='图片文件路径:').pack(side=tk.LEFT)
file1 = tk.StringVar()
tk.Entry(fr_top, width=50, textvariable=file1).pack(side=tk.LEFT)
vButton = tk.Button(fr_top, text='...', width=3, command=getfile)
vButton.pack(side=tk.LEFT)
vButton = tk.Button(fr_top, text='分割成九宫格', command=split_pic,
                    width=20)
vButton.pack(side=tk.LEFT)
vButton = tk.Button(fr_top, text='Show', command=show_pic_detail,
                    width=10)
vButton.pack(side=tk.LEFT)

fr_bottom2 = tk.LabelFrame(root)
fr_bottom2.grid(row=1, column=0)

img_left = Image.open('11.png')  # 打开图片
img_png_left = ImageTk.PhotoImage(image=img_left)

button_imgx = tk.Button(fr_bottom2, image=img_png_left, width=200, height=200)
button_imgx.grid(row=0, column=0)

fr_bottom = tk.LabelFrame(root)
fr_bottom.grid(row=1, column=1)

img_png_list = []
for i in range(9):
    x = str(i+1)+'.png'
    print(x)
    img = Image.open(x)  # 打开图片
    img_png_list.append(ImageTk.PhotoImage(image=img))

i = 0
button_img_list = []
for x in range(3):
    for y in range(3):
        button_img = tk.Button(fr_bottom, image=img_png_list[i],
                                width=width1, height=height1)
        button_img.grid(row=x, column=y)
        i = i+1
        button_img_list.append(button_img)

# img = Image.open('1.png')  # 打开图片
# img_png1 = ImageTk.PhotoImage(image=img)
# img = Image.open('2.png')  # 打开图片
# img_png2 = ImageTk.PhotoImage(image=img)
# img = Image.open('3.png')  # 打开图片
# img_png3 = ImageTk.PhotoImage(image=img)
# img = Image.open('4.png')  # 打开图片
# img_png4 = ImageTk.PhotoImage(image=img)
# img = Image.open('5.png')  # 打开图片
# img_png5 = ImageTk.PhotoImage(image=img)
# img = Image.open('6.png')  # 打开图片
# img_png6 = ImageTk.PhotoImage(image=img)
# img = Image.open('7.png')  # 打开图片
# img_png7 = ImageTk.PhotoImage(image=img)
# img = Image.open('8.png')  # 打开图片
# img_png8 = ImageTk.PhotoImage(image=img)
# img = Image.open('9.png')  # 打开图片
# img_png9 = ImageTk.PhotoImage(image=img)

# button_img2 = tk.Button(fr_bottom, text="WIFI", image=img_png1,
#                         width=width1, height=height1)
# button_img2.grid(row=0, column=0)
# button_img2 = tk.Button(fr_bottom, text="WIFI", image=img_png2,
#                         width=width1, height=height1)
# button_img2.grid(row=0, column=1)
# button_img2 = tk.Button(fr_bottom, text="WIFI", image=img_png3,
#                         width=width1, height=height1)
# button_img2.grid(row=0, column=2)
# button_img2 = tk.Button(fr_bottom, text="WIFI", image=img_png4,
#                         width=width1, height=height1)
# button_img2.grid(row=1, column=0)
# button_img2 = tk.Button(fr_bottom, text="WIFI", image=img_png5,
#                         width=width1, height=height1)
# button_img2.grid(row=1, column=1)
# button_img2 = tk.Button(fr_bottom, text="WIFI", image=img_png6,
#                         width=width1, height=height1)
# button_img2.grid(row=1, column=2)
# button_img2 = tk.Button(fr_bottom, text="WIFI", image=img_png7,
#                         width=width1, height=height1)
# button_img2.grid(row=2, column=0)
# button_img2 = tk.Button(fr_bottom, text="WIFI", image=img_png8,
#                         width=width1, height=height1)
# button_img2.grid(row=2, column=1)
# button_img2 = tk.Button(fr_bottom, text="WIFI", image=img_png9,
#                         width=width1, height=height1)
# button_img2.grid(row=2, column=2)


root.mainloop()