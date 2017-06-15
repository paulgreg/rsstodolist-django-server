# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulStoneSoup

class Converter():

  def convert(self, nameToClean):
    if (nameToClean == None):
        return None

    nameToConvert = nameToClean.replace('&#x2605;'.decode('utf8'), '')
    sanitizedName = BeautifulStoneSoup(nameToConvert, convertEntities=BeautifulStoneSoup.HTML_ENTITIES )
    return unicode(sanitizedName).replace('»'.decode('utf8'), '\'').replace('«'.decode('utf8'), '\'').replace('&', 'and').replace('<', '{').replace('>', '}').replace('\n', ' ').replace('\r', '').replace('\t', ' ')
