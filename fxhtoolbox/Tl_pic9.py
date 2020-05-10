
# 程序思路
#
# 此次程序主要是利用 PIL（Python Image Libraty）这库，来进行图片的处理。
#
# PIL 是一个功能非常强大的 Python 图像处理标准库，但由于 PIL 只支持 Python2.7。如今很多 python 程序员都使用 Python 3.x，所以 PIL 在之前的基础上分离出来一个分支，另外创建一个 Pillow 库，以便支持 Python3.x。本程序在使用之前请确保已经安装了 Pillow 库。
#
# 程序首先把你要分隔的图像读取到一个变量中，然后我们定义了一个 fill_image() 方法，用来填充图像让原本大小不一的图像，重新变为一个长宽相同的正方形图像，方便之后处理。
#
# 通过 fill_image() 方法，我们就会得到新的一张正方形图像。随后我们在利用 cut_image() 方法，把图像分隔成 9 张，因为微信朋友圈最多发 9 张图片。
#
# 最后把这 9 张图片保存到本地文件中，发送到手机，就可以发到朋友圈了。
#
# 程序源码
 
from PIL import Image
import sys

# 先将 input image 填充为正方形
def fill_image(image):
    width, height = image.size
    # 选取长和宽中较大值作为新图片的
    new_image_length = width if width > height else height
    # 生成新图片[白底]
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')  # 注意这个函数！
    # 将之前的图粘贴在新图上，居中
    if width > height:  # 原图宽大于高，则填充图片的竖直维度 #(x,y)二元组表示粘贴上图相对下图的起始位置,是个坐标点。
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (0, int((new_image_length - width) / 2)))
    # new_image.show()
    return new_image
 
 
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)  # 因为朋友圈一行放3张图。
    box_list = []
    # (left, upper, right, lower)
    for i in range(3):
        for j in range(3):
            # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)
 
    image_list = [image.crop(box) for box in box_list]
 
    return image_list
 
 
# 保存
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save(str(index) + '.png', 'PNG')
        index += 1
 

def Start_split(pic_file):
    # file_path = "11.png"
    file_path = pic_file
    image = Image.open(file_path)
    # image.show()
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)
    