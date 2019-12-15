#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  16:21
# Email    : spirit_az@foxmail.com
# File     : editConf.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import ConfigParser

import dirPath

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
playMode = {'playSingle': 0,
            'playLoop': 1,
            'playOrder': 2,
            'playRandom': 3}


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class conf(object):
    _in_path = os.path.join(dirPath.__dirPath__, 'configuration.ini').replace('\\', '/')

    def __init__(self):
        self.cf = ConfigParser.ConfigParser()

    def get(self, field, key):
        try:
            self.cf.read(self._in_path)
            result = self.cf.get(field, key)
        except:
            result = ""

        return result

    def set(self, field, key, val):
        if self.find(field, key):
            self.cf.remove_option(field, key)

        self.cf.set(field, key, val)
        self.write()

    def has_op(self, section):
        self.cf.read(self._in_path)
        return self.cf.has_section(section)

    def find(self, field, key):
        self.cf.read(self._in_path)
        return self.cf.has_option(field, key)

    def write(self):
        with open(self._in_path, 'wb') as f:
            self.cf.write(f)

    @classmethod
    def getName(cls):
        return cls().get('configuration', 'name')

    @classmethod
    def getVersion(cls):
        return cls().get('configuration', 'version')

    @classmethod
    def getFlag(cls):
        return eval(cls().get('configuration', 'flag'))

    @classmethod
    def getPlayMode(cls):
        return cls().get('configuration', 'playmode')

    @classmethod
    def setPlayMode(cls, val):
        return cls().set('configuration', 'playmode', val)

    def __getAuthor__(self):
        return self.get('@Copyright', '1011111 1011111 1100001 1110101 1110100 1101000 1101111 1110010 1011111 1011111')

    def __getEmail__(self):
        return self.get('@Copyright', '1011111 1011111 1000101 1101101 1100001 1101001 1101100 1011111 1011111')


if __name__ == '__main__':
    cc = conf()
    print cc.set('configuration', 'playMode', 'playLoop')
