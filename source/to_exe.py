#!/usr/bin/env python
# -*- coding:UTF-8 -*-
__author__ = 'miaochenliang'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# import++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ↓+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
import os
from PyInstaller.__main__ import run


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
file_path = os.path.dirname(os.path.dirname(__file__))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def openUI():
    opts = ['MPlayer.py',
            '--noconsole',
            '--distpath=%s' % os.path.join(file_path, 'dist').replace('\\', '/'),
            '--workpath=%s' % os.path.join(file_path, 'build').replace('\\', '/'),
            '--specpath=%s' % os.path.dirname(__file__),
            '-y',
            '--clean',
            '--icon=%s' % os.path.join(file_path, 'source/UI/icons/exe_icon.ico').replace('\\', '/')
            ]
    run(opts)


if __name__ == '__main__':
    openUI()

"""
    图片引用路径可以设置为相对路径。

　　代码中，opts= 后面的列表里的就是一系列参数，详解如下：

    file_path = os.path.dirname(__file__)
　　第一个***.py就是你要编译的文件名，必填 [之后的参数全部为选填]

　　第二个-F就是生成单文件的参数

    第三个--noconsole取消cmd窗口

　　第四个--distpath=**意思是dist文件夹（最后输出文件所在地）的路径，**为路径，比如os.path.join(file_path, 'dist').replace('\\', '/')，默认为当前目录下的dist文件夹内

　　第五个--workpath=**意思是build文件夹（临时文件）的路径，**为路径，比如os.path.join(file_path, 'build').replace('\\', '/')，默认为当前目录下的build文件夹内

　　第六个--specpath=**意思是***.spec文件（临时文件）的路径，**为路径，比如file_path，默认为当前目录

　　第七个--icon=**意思是输出的exe文件的图标路径，**为路径，比如E:/tools/VHQLauncher/source/icons/VHQLuncher_exe_icon.ico
"""
