# -*- coding: utf-8 -*-
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def join(png1, png2, flag='horizontal'):
    with open('w.txt','w') as f:
        f.write('wqw')
        f.close()
    """
    :param png1: path
    :param png2: path
    :param flag: horizontal or vertical
    :return:
    """
    img1, img2 = Image.open(png1), Image.open(png2)
    size1, size2 = img1.size, img2.size


    if flag == 'horizontal':
        joint = Image.new('RGB', (size1[0]+size2[0], size1[1]))
        loc1, loc2 = (0, 0), (size1[0], 0)
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('./yubiao/img/horizontal.png')
    elif flag == 'vertical':
        joint = Image.new('RGB', (size1[0], size1[1]+size2[1]))
        loc1, loc2 = (0, 0), (0, size1[1])
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('./yubiao/img/vertical.png')

def img_main(code_name):
    png1 = './yubiao/img/code_white.png'
    png2 = './yubiao/img/code.png'
    join(png1, png2, flag='vertical')
    # 打开底版图片
    imageFile = r'./yubiao/img/vertical.png'
    img = Image.open(imageFile)
    # 选择字体与大小
    font = ImageFont.truetype("C:\Windows\Fonts\msyh.ttc", 14)
    # 在图片上添加文字
    word = "请在下图依次点击：{}".format(code_name[0])
    width = img.width
    height = img.height
    # 查看图片宽高
    # print(width, height)
    position = (3, 10)
    color = (0, 0, 0)
    draw = ImageDraw.Draw(img)
    draw.text(position, word, color, font=font)
    # 保存图片
    img.save(r'./yubiao/img/wj.png')