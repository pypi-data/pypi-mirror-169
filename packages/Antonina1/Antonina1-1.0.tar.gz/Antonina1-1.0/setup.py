# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:03:37 2022
安冬妮娜助手1.0版本，功能非常简陋，仅供自己使用并等待升级
谨献给云图计划游戏中的安冬妮娜，我最信任的网络安全工程师
@author: Jinqk
"""

from setuptools import setup, find_packages

NAME = 'Antonina1'
VERSION = '1.0'
DESCRIPTION = "安冬妮娜助手1.0版本，功能非常简陋,用于显示具有安冬妮娜图片的提示弹窗和进度条",#包简介
AUTHOR = 'Jinqk'
REQUIRES_PYTHON = '>=3.6.0'
URL = 'https://github.com/Jinqk/Antonina.git'
setup(
    name= NAME,#包名
    version = VERSION,#版本
    description = DESCRIPTION,
    # long_description=open('README.md').read(),#读取文件中介绍包的详细内容
    include_package_data=True,#是否允许上传资源文件
    author=AUTHOR,#作者
    author_email='jinqk@mail2.sysu.edu.cn',#作者邮件
    maintainer='Jinqk',#维护者
    maintainer_email='jinqk@mail2.sysu.edu.cn',#维护者邮件
    license='MIT License',#协议
    url=URL,#github或者自己的网站地址
    packages=find_packages(),#包的目录
    python_requires=REQUIRES_PYTHON,#设置python版本要求
    install_requires=['PySimpleGUI'],#安装所需要的库
    entry_points={
        'console_scripts': [
            'Antonina.stpup = Antonina.stpop.py',
            'Antonina.endpup = Antonina.endpop.py'],
    },#设置命令行工具(可不使用就可以注释掉)
    
)