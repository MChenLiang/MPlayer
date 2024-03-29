#!/usr/bin/env python
# -*- coding:UTF-8 -*-
__author__ = 'miaochenliang'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
H_slider = """QSlider::groove:horizontal {
    border: 1px solid #4A708B;
    background: #C0C0C0;
    height: 5px;
    border-radius: 1px;
    padding-left:-1px;
    padding-right:-1px;
}

QSlider::sub-page:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #B1B1B1, stop:1 #c4c4c4);
    background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
        stop: 0 #5DCCFF, stop: 1 #1874CD);
    border: 1px solid #4A708B;
    height: 10px;
    border-radius: 2px;
}

QSlider::add-page:horizontal {
    background: #575757;
    border: 0px solid #777;
    height: 10px;
    border-radius: 2px;
}

QSlider::handle:horizontal
{
    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
    stop:0.6 #45ADED,
    stop:0.778409 rgba(255, 255, 255, 255),
    stop:0.99 rgba(0, 0, 0, 0));

    width: 23px;
    margin-top: -9px;
    margin-bottom: -9px;
    border-radius: 10px;
}

QSlider::handle:horizontal:hover {
    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.6, fx:0.5, fy:0.5,
    stop: 0.6 #2A8BDA, /*rgba(98, 98, 98, 255),*/
    stop:0.778409 rgba(255, 255, 255, 255),
    stop:0.92 rgba(0, 0, 0, 0));

    width: 23px;
    margin-top: -9px;
    margin-bottom: -9px;
    border-radius: 10px;
}

QSlider::sub-page:horizontal:disabled {
    background: #00009C;
    border-color: #999;
}

QSlider::add-page:horizontal:disabled {
    background: #eee;
    border-color: #999;
}

QSlider::handle:horizontal:disabled {
    background: #eee;
    border: 1px solid #aaa;
    border-radius: 4px;
}"""

S_slider = """QSlider::groove:vertical {
    border: 1px solid #4A708B;
    background: #C0C0C0;
    width: 5px;
    border-radius: 1px;
    padding-left:-1px;
    padding-right:-1px;
    padding-top:-1px;
    padding-bottom:-1px;
}

QSlider::sub-page:vertical {
    background: #575757;
    border: 1px solid #4A708B;
    border-radius: 2px;
}

QSlider::add-page:vertical {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #c4c4c4, stop:1 #B1B1B1);
    background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
        stop: 0 #5DCCFF, stop: 1 #1874CD);
    border: 0px solid #777;
    width: 10px;
    border-radius: 2px;
}

QSlider::handle:vertical
{
    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
    stop:0.6 #45ADED,
    stop:0.778409 rgba(255, 255, 255, 255),
    stop:0.99 rgba(0, 0, 0, 0));

    height: 12px;
    margin-left: -4px;
    margin-right: -4px;
    border-radius: 10px;
}

QSlider::handle:vertical:hover {
    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.6, fx:0.5, fy:0.5,
    stop: 0.6 #2A8BDA, /*rgba(98, 98, 98, 255),*/
    stop:0.778409 rgba(255, 255, 255, 255),
    stop:0.92 rgba(0, 0, 0, 0));

    height: 12px;
    margin-left: -4px;
    margin-right: -4px;
    border-radius: 10px;
}

QSlider::sub-page:vertical:disabled {
    background: #00009C;
    border-color: #999;
}

QSlider::add-page:vertical:disabled {
    background: #eee;
    border-color: #999;
}

QSlider::handle:vertical:disabled {
    background: #eee;
    border: 1px solid #aaa;
    border-radius: 4px;
}"""

QLabel_list = """
QLabel{
    border-radius: 1px;
    border: 1px solid #aaa;
    height: 19pt;
    font: 12pt Monospaced;
}

"""

