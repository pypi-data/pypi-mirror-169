# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:41:01 2022

@author: Jinqk
"""
import requests
from PIL import Image
from io import BytesIO
import PySimpleGUI as sg

def endpop():
    response = requests.get('https://pic1.imgdb.cn/item/63357deb16f2c2beb16d81ef.png')
    image = Image.open(BytesIO(response.content))
    image.save('./2.png')
    title = '安冬妮娜小助手'
    sg.popup_ok('已经算完了哦，可以下班了吧',title =title,keep_on_top = True,grab_anywhere = True,image = './2.png')
    
# if __name__ == '__main__':
#     main()
