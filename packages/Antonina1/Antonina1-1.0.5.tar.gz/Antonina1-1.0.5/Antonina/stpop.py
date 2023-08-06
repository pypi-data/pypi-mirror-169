# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:23:19 2022

@author: Jinqk
"""
import requests
from PIL import Image
from io import BytesIO
import PySimpleGUI as sg

def stpop():
    response = requests.get('https://pic1.imgdb.cn/item/63357deb16f2c2beb16d81f3.png')
    image = Image.open(BytesIO(response.content))
    image.save('./1.png')
    title = '安冬妮娜小助手'
    sg.popup_ok('又要上班了吗？',title =title,keep_on_top = True,grab_anywhere = True,image = './1.png')
    

