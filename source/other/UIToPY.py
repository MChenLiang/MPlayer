# coding:utf-8
__author__ = 'miaochenliang'
from PyQt4 import uic

import os
import glob


def uicToPY(name):
    with open(str(name).replace('.ui', '.py'), 'w') as f:
        uic.compileUi(name, f)

if __name__ == '__main__':
    dir_name = os.path.dirname(os.path.dirname(__file__))
    filepath = '{}/UI/*.ui'.format(dir_name)
    func = lambda x: uicToPY(x)
    map(func, glob.glob(filepath))
