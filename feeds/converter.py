# coding: utf8
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

class Converter():

  def convert(self, nameToClean):
    if (nameToClean == None):
        return None

    h = HTMLParser()
    s = h.unescape(nameToClean)
    s = s.replace('<', '{').replace('>', '}')
    s = s.replace('\n', ' ').replace('\r', '').replace('\t', ' ')
    return s
