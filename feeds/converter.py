# coding: utf8
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

class Converter():

  def convert(self, nameToClean):
    if (nameToClean == None):
        return None

    try:
        s = nameToClean.decode('utf8')
    except UnicodeEncodeError:
        s = nameToClean

    s = HTMLParser().unescape(s)
    s = s.replace('<', '{').replace('>', '}')
    s = s.replace('\n', ' ').replace('\r', '').replace('\t', ' ')

    return s
