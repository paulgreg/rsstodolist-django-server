# coding: utf8
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
import re

# https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
"]+", flags=re.UNICODE)

class Converter():

  def convert(self, nameToClean):
    if (nameToClean == None):
        return None

    try:
        s = nameToClean.decode('utf8')
    except UnicodeDecodeError:
        s = nameToClean
    except UnicodeEncodeError:
        s = nameToClean

    s = emoji_pattern.sub(r'', s)
    s = HTMLParser().unescape(s)
    s = s.replace('<', '{').replace('>', '}')
    s = s.replace('\n', ' ').replace('\r', '').replace('\t', ' ')

    return s
