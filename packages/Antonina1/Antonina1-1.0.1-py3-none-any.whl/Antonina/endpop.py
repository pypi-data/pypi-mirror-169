# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:41:01 2022

@author: Jinqk
"""
_version_ = '1.0.1'
import PySimpleGUI as sg
def endpop():
    title = '安东尼娜小助手'
    sg.popup_ok('已经算完了哦，可以下班了吧',title =title,keep_on_top = True,grab_anywhere = True,image = '.\\Antonina.png')
    
# if __name__ == '__main__':
#     main()
