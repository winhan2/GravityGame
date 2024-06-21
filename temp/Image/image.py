# coding: utf-8

from PIL import Image, ImageDraw, ImageFont

# 用PIL画图

# 创建一个空白图像
img = Image.new('RGB', (800, 600), 'white')

# 创建一个绘图对象
draw = ImageDraw.Draw(img)

# 画一个矩形
# draw.rectangle((50, 50, 150, 150), fill='blue')

# 画一个圆形
# draw.ellipse((100, 100, 150, 150), fill='red')

# spacing = 40
# # 画一条线
# for i in range(600 // spacing):
#     draw.line([(0, spacing * i), (600, spacing * i)], fill='black')
# for i in range(600 // spacing):
#     draw.line([(spacing * i, 0), (spacing * i, 600)], fill='black')
#
# # # 添加文字
# # font = ImageFont.truetype('arial.ttf', 36)
# # draw.text((50, 50), 'Hello, World!', fill='black', font=font)
#
# # 保存图像
# img.save('bg.jpg')

from PIL import Image

# 打开图像文件
img = Image.open('cance.png')

# 获取图像的宽度和高度
width, height = img.size

# 创建一个新的图像，大小为原始图像的1/4
new_img = img.resize((50, 50))

# 保存新的图像文件
new_img.save('cance2.png')
